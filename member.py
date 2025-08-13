from __future__ import annotations, with_statement

class Member:
    def __init__(self, name: str, borrowed: dict[str, int]):
        self.name = name
        self._borrowed: dict[str, int] = borrowed

    def borrow_book(self, title: str):
        if title in self._borrowed:
            self._borrowed[title] += 1
            return
        self._borrowed[title] = 1

    def return_book(self, title: str):
        if title in self._borrowed:
            self._borrowed[title] -= 1
            if self._borrowed[title] == 0:
                self._borrowed.pop(title)
        else:
            raise ValueError(f"the book '{title}' is not borrowed by '{self.name}'")

    @property
    def borrowed(self):
        return self._borrowed

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self).items()}

    @staticmethod
    def from_dict(data: dict) -> Member:
        return Member(**data)
