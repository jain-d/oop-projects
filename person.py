from __future__ import annotations

class Person:
    def __init__(self, name: str):
        self.name: str = name.strip()

    def to_dict(self):
        return {key: value for key, value in vars(self).items()}

    @classmethod
    def from_dict(cls, data) -> Person:
        return cls(**data)
