# book.py

class Book:
    total_books_borrowed = {}     # class-level analytics

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        """Borrow the book if available."""
        if not self.available:
            return False

        self.available = False
        
        # Track borrow count
        Book.total_books_borrowed[self.book_id] = (
            Book.total_books_borrowed.get(self.book_id, 0) + 1
        )
        return True

    def return_book(self):
        """Return a previously borrowed book."""
        if self.available:
            return False
        self.available = True
        return True

    def to_string(self):
        return f"{self.book_id},{self.title},{self.author},{self.available}"

    @staticmethod
    def from_string(line):
        book_id, title, author, available = line.strip().split(',')
        return Book(book_id, title, author, available == "True")
