from __future__ import annotations

class Book:
    def __init__(self, title: str, author: str, in_stock=1):
        self.title = title
        self.author = author
        self.in_stock = in_stock

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self).items()}

    @staticmethod
    def from_dict(data: dict) -> Book:
        return Book(**data)
