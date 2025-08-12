from book import Book
from member import Member

class Library:
    def __init__(self, books: list[Book], members: list[Member]):
        self.books: list[Book] = books
        self.members = members

    def add_book(self, book: Book):
        self.books.append(book)

    def lend_book(self, title: str, member: Member):
        book_found = False
        for book in self.books:
            if book.title == title:
                book_found = True
                if book.available:
                    member.borrow_book(book)
                    book.available ^= True
                    return
        if book_found:
            raise Exception("Book Unavailable") 
        raise Exception("Book not found!")

    def return_book(self, title: str, member: Member):
        for book in self.books:
            if book.title == title and not book.available:
                member.return_book(book)
                book.available ^= True

