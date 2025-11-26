# Name: Diya Das
# Date: 26/11/25
# Assignment 3 - Library Management System

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def register_member(self, member):
        self.members.append(member)
        self.save_data()

    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            member.borrow_book(book)
            self.save_data()
        else:
            print("Invalid member ID or book ISBN!")

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            member.return_book(book)
            self.save_data()
        else:
            print("Invalid return request!")

    # File persistence 🎯
    def save_data(self):
        try:
            with open("books.json", "w") as f:
                json.dump([b.to_dict() for b in self.books], f)
            with open("members.json", "w") as f:
                json.dump([m.to_dict() for m in self.members], f)
        except Exception as e:
            print("Error saving data:", e)

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]
            with open("members.json", "r") as f:
                self.members = [Member.from_dict(m) for m in json.load(f)]
        except:
            self.books = []
            self.members = []

    # Task 5 - Analytics 📊
    def library_report(self):
        borrowed_books = sum(1 for b in self.books if not b.available)
        most_borrowed = max(self.books, key=lambda b: b.borrow_count, default=None)

        print("\n📌 Library Report 📌")
        print(f"Total Active Members : {len(self.members)}")
        print(f"Total Books Borrowed : {borrowed_books}")
        if most_borrowed:
            print(f"Most Borrowed Book : {most_borrowed.title} ({most_borrowed.borrow_count} times)")
        print("--------------------------------")
