# library.py

from book import Book
from member import Member

BOOK_FILE = "data/books.txt"
MEMBER_FILE = "data/members.txt"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    # --- File Persistence --- #

    def load_data(self):
        # Load books
        try:
            with open(BOOK_FILE, "r") as f:
                for line in f:
                    book = Book.from_string(line)
                    self.books[book.book_id] = book
        except FileNotFoundError:
            pass

        # Load members
        try:
            with open(MEMBER_FILE, "r") as f:
                for line in f:
                    member = Member.from_string(line)
                    self.members[member.member_id] = member
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(BOOK_FILE, "w") as f:
            for book in self.books.values():
                f.write(book.to_string() + "\n")

        with open(MEMBER_FILE, "w") as f:
            for member in self.members.values():
                f.write(member.to_string() + "\n")

    # --- Operations --- #

    def add_book(self, book):
        self.books[book.book_id] = book
        self.save_data()

    def add_member(self, member):
        self.members[member.member_id] = member
        self.save_data()

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            if member.borrow_book(book):
                self.save_data()
                return True
        return False

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            if member.return_book(book):
                self.save_data()
                return True
        return False

    # --- Class-Level Analytics --- #

    def most_borrowed_book(self):
        if not Book.total_books_borrowed:
            return None
        most = max(Book.total_books_borrowed, key=Book.total_books_borrowed.get)
        return self.books.get(most)
