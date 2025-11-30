# library.py
# Assignment 3

import json
import os
from book import Book
from member import Member

BOOK_FILE = "data/books.json"
MEMBER_FILE = "data/members.json"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    # ---------------- FILE HANDLING ---------------- #

    def load_data(self):
        # Load books
        try:
            if os.path.exists(BOOK_FILE):
                with open(BOOK_FILE, "r") as f:
                    data = json.load(f)
                    for b in data:
                        bk = Book.from_dict(b)
                        if bk:
                            self.books[bk.isbn] = bk
        except json.JSONDecodeError:
            print("Error: books.json is corrupted. Starting with empty data.")
        except Exception as e:
            print("Unexpected error loading books:", e)

        # Load members
        try:
            if os.path.exists(MEMBER_FILE):
                with open(MEMBER_FILE, "r") as f:
                    data = json.load(f)
                    for m in data:
                        mb = Member.from_dict(m)
                        if mb:
                            self.members[mb.member_id] = mb
        except json.JSONDecodeError:
            print("Error: members.json is corrupted. Starting with empty data.")
        except Exception as e:
            print("Unexpected error loading members:", e)

    def save_data(self):
        try:
            # save books
            with open(BOOK_FILE, "w") as f:
                json.dump([b.to_dict() for b in self.books.values()], f, indent=4)

            # save members
            with open(MEMBER_FILE, "w") as f:
                json.dump([m.to_dict() for m in self.members.values()], f, indent=4)

        except Exception as e:
            print("Error saving data:", e)

    # ---------------- LIBRARY METHODS ---------------- #

    def add_book(self, book):
        try:
            self.books[book.isbn] = book
            self.save_data()
            return True
        except Exception:
            return False

    def register_member(self, member):
        try:
            self.members[member.member_id] = member
            self.save_data()
            return True
        except Exception:
            return False

    def lend_book(self, member_id, isbn):
        try:
            member = self.members.get(member_id)
            book = self.books.get(isbn)

            if member and book:
                if member.borrow_book(book):
                    self.save_data()
                    return True
            return False
        except Exception:
            return False

    def take_return(self, member_id, isbn):
        try:
            member = self.members.get(member_id)
            book = self.books.get(isbn)

            if member and book:
                if member.return_book(book):
                    self.save_data()
                    return True
            return False
        except Exception:
            return False

    # ---------------- ANALYTICS ---------------- #

    def most_borrowed_book(self):
        try:
            if not Book.borrow_count:
                return None
            most = max(Book.borrow_count, key=Book.borrow_count.get)
            return self.books.get(most)
        except Exception:
            return None

    def analytics_report(self):
        try:
            total_members = len(self.members)
            borrowed_books = sum(not book.available for book in self.books.values())
            most = self.most_borrowed_book()

            report = f"""
------------ LIBRARY REPORT ------------
Total Members: {total_members}
Books Currently Borrowed: {borrowed_books}
Most Borrowed Book: {most.title if most else 'None'}
----------------------------------------
"""
            return report
        except Exception:
            return "Error generating report."
