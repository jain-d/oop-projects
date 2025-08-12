from __future__ import annotations

class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self).items()}

    @classmethod
    def from_dict(entry: dict) -> Book:
        return Book(**entry)
