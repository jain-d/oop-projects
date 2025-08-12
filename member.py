from book import Book

class Member:
    def __init__(self, name: str, borrowed_books: list[Book]):
        self.name: str = name
        self._borrowed_books: set = set(borrowed_books)
    
    def borrow_book(self, book: Book):
        if book in self._borrowed_books:
            raise ValueError("Can not borrow additional copies of a borrowed book.")
        self._borrowed_books.add(book)

    def return_book(self, book: Book):
        if book not in self._borrowed_books:
            raise ValueError("Can not return un-borrowed book.")
        self._borrowed_books.remove(book)

    @property
    def borrowed_books(self) -> list[Book]:
        return list(self._borrowed_books)
