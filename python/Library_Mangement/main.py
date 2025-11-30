# main.py

from library import Library
from book import Book
from member import Member

lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Most Borrowed Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        lib.add_book(Book(id, title, author))
        print("Book added!")

    elif choice == "2":
        id = input("Member ID: ")
        name = input("Name: ")
        lib.add_member(Member(id, name))
        print("Member added!")

    elif choice == "3":
        mid = input("Member ID: ")
        bid = input("Book ID: ")
        if lib.borrow_book(mid, bid):
            print("Book borrowed!")
        else:
            print("Borrowing failed.")

    elif choice == "4":
        mid = input("Member ID: ")
        bid = input("Book ID: ")
        if lib.return_book(mid, bid):
            print("Book returned!")
        else:
            print("Return failed.")

    elif choice == "5":
        book = lib.most_borrowed_book()
        if book:
            print(f"Most Borrowed: {book.title} by {book.author}")
        else:
            print("No books borrowed yet.")

    elif choice == "6":
        break

    else:
        print("Invalid choice!")
