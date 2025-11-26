# Name: Diya Das
# Date: 26/11/25
# Assignment 3 - Library Management System

from library import Library
from book import Book
from member import Member

lib = Library()
print("\n📚 Welcome to Library Management System 📚")

while True:
    print("\n--------- MENU ---------")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        lib.add_book(Book(title, author, isbn))
        print("Book added successfully!")

    elif choice == "2":
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        lib.register_member(Member(name, member_id))
        print("Member Registered!")

    elif choice == "3":
        member_id = input("Enter member ID: ")
        isbn = input("Enter book ISBN: ")
        lib.lend_book(member_id, isbn)

    elif choice == "4":
        member_id = input("Enter member ID: ")
        isbn = input("Enter ISBN: ")
        lib.take_return(member_id, isbn)

    elif choice == "5":
        lib.library_report()

    elif choice == "6":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
