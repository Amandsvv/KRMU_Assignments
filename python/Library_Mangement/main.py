# main.py
# Author: Aman Kumar
# Assignment 3 – OOP Library Inventory System

print("Welcome to the Library Inventory System (Assignment 3)\n")

from library import Library
from book import Book
from member import Member

lib = Library()

while True:
    try:
        print("\n1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                lib.add_book(Book(title, author, isbn))
                print("Book Added Successfully!")
            except Exception:
                print("Error adding book.")

        elif choice == "2":
            try:
                name = input("Member Name: ")
                member_id = input("Member ID: ")
                lib.register_member(Member(name, member_id))
                print("Member Registered!")
            except Exception:
                print("Error registering member.")

        elif choice == "3":
            try:
                member_id = input("Member ID: ")
                isbn = input("Book ISBN: ")
                if lib.lend_book(member_id, isbn):
                    print("Book Borrowed!")
                else:
                    print("Borrowing Failed!")
            except Exception:
                print("Error processing borrow request.")

        elif choice == "4":
            try:
                member_id = input("Member ID: ")
                isbn = input("Book ISBN: ")
                if lib.take_return(member_id, isbn):
                    print("Book Returned!")
                else:
                    print("Return Failed!")
            except Exception:
                print("Error processing return request.")

        elif choice == "5":
            print(lib.analytics_report())

        elif choice == "6":
            print("Exiting Program...")
            break

        else:
            print("Invalid Option! Try again.")

    except Exception:
        print("Unexpected error occurred at menu.")
