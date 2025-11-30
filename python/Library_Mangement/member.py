# member.py
# Assignment 3

class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book):
        try:
            if book.borrow():
                self.borrowed_books.append(book.isbn)
                return True
            return False
        except Exception:
            return False

    def return_book(self, book):
        try:
            if book.isbn in self.borrowed_books and book.return_book():
                self.borrowed_books.remove(book.isbn)
                return True
            return False
        except Exception:
            return False

    def list_books(self):
        try:
            return self.borrowed_books
        except Exception:
            return []

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        try:
            return Member(
                data["name"],
                data["member_id"],
                data["borrowed_books"]
            )
        except KeyError:
            print("Error: Corrupted member record found. Skipped loading.")
            return None
