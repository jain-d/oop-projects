from book import Book
from member import Member


class Library:
    def __init__(self, books: dict[str, Book], members: dict[str, Member]):
        self._books: dict[str, Book] = books
        self._members: dict[str, Member] = members

    def add_book(book: Book):
        if (title := book.title) in self._books:
            self._books[title].in_stock += 1
        else:
            self._books.update({title: book})

    def add_member(self, member: Member):
        if (name := member.name) in self._members:
            raise ValueError(f"a member named '{name}' already exists.")
        else:
            self._members.update({name: member})
