# Name: Jhalak Choudhary
# Date: 26/11/25
# Assignment 3 - Library Management System

class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.isbn)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available!")

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            print(f"{self.name} returned {book.title}")

    def list_books(self):
        return self.borrowed_books

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(data["name"], data["member_id"], data["borrowed_books"])
