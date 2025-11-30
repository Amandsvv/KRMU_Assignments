# book.py
# Author: Aman Kumar
# Assignment 3 – Library Inventory System

class Book:
    borrow_count = {}   # class-level analytics

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        try:
            if not self.available:
                return False
            self.available = False
            Book.borrow_count[self.isbn] = Book.borrow_count.get(self.isbn, 0) + 1
            return True
        except Exception:
            return False

    def return_book(self):
        try:
            if self.available:
                return False
            self.available = True
            return True
        except Exception:
            return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        try:
            return Book(
                data["title"],
                data["author"],
                data["isbn"],
                data["available"]
            )
        except KeyError:
            print("Error: Corrupted book record found. Skipped loading.")
            return None
