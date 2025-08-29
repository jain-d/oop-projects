from __future__ import annotations
from member import Member
from book import Book
import json


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book: Book):
        if book.title in self.books:
            self.books[book.title].in_stock += book.in_stock
            return
        self.books[book.title] = book

    def add_member(self, member: Member):
        if member.name in self.members:
            raise ValueError(f"The member '{member.name}' already exists.")
        self.members[member.name] = member

    def lend_book(self, title: str, member_name: str):
        # making sure stock exists
        if title not in self.books:
            raise LookupError(f"The book {title} is not in library")
        elif not self.books[title].in_stock:
            raise ValueError(f"The book {title} is out of stock")
        # making sure member exists
        elif member_name not in self.members:
            raise LookupError(f"Member not found! no member named '{member_name}' exists")
        self.members[member_name].borrow_book(title)        # declaring to mark the book borrowed book
        self.books[title].in_stock -= 1                     # decreasing the stock

    def return_book(self, title: str, member_name: str):
        if title not in self.books:
            raise LookupError(f"No records of book '{title}'")
        elif member_name not in self.members:
            raise LookupError(f"Member not found! no member named '{member_name}' exists")
        self.members[member_name].return_book(title)        # declaring to return the book
        self.books[title].in_stock += 1                     # restocking the book

    def save_to_file(self, filename: str):
        dict_to_dump: dict = {"books": [], "members": []}

        for book in self.books.values():
            dict_to_dump["books"].append(book.to_dict())

        for member in self.members.values():
            dict_to_dump["members"].append(member.to_dict())

        with open(filename, "w") as file:
            json.dump(dict_to_dump, file)

    @classmethod
    def load_from_file(cls, filename: str) -> Library:
        # reading file data
        with open(filename, "r") as file:
            file_data = json.load(file)

        lib = cls()
        # mapping data
        for data_type, data_list in file_data.items():
            if data_type == "books":
                for book in data_list:
                    lib.add_book(Book.from_dict(book))
            elif data_type == "members":
                for member in data_list:
                    lib.add_member(Member.from_dict(member))
            else:
                raise ValueError("Found un-mappable data while reading json file")
        return lib

    def __str__(self):
        return f"\n{[f'{book.title} | {book.in_stock}' for book in self.books.values()]}\n{[member for member in self.members.keys()]}\n"
