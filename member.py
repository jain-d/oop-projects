from __future__ import annotations

class Member():
    def __init__(self, name: str, borrowed: dict[str, int]={}):
        self.name = name
        self.borrowed: dict[str, int] = borrowed

    def borrow_book(self, title: str):
        if title in self.borrowed:
            self.borrowed[title] += 1
            return
        self.borrowed[title] = 1

    def return_book(self, title: str):
        if title in self.borrowed:
            self.borrowed[title] -= 1
            if self.borrowed[title] == 0:
                self.borrowed.pop(title)
        else:
            raise LookupError(f"{self.name} doesn't have a book issued by the name '{title}'")

    def list_books(self) -> list:
        return [f"'{name}' | {count}" for name, count in self.borrowed.items()]

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self).items()}

    @classmethod
    def from_dict(cls, data) -> Member:
        return cls(**data)

