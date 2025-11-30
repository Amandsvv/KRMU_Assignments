# member.py

class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.book_id)
            return True
        return False

    def return_book(self, book):
        if book.book_id in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book.book_id)
            return True
        return False

    def to_string(self):
        books = "|".join(self.borrowed_books)
        return f"{self.member_id},{self.name},{books}"

    @staticmethod
    def from_string(line):
        parts = line.strip().split(',')
        member_id, name = parts[:2]
        borrowed = parts[2].split('|') if parts[2] else []
        return Member(member_id, name, borrowed)
