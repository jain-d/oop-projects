from dataclasses import dataclass, field

@dataclass
class Expense:
    id: int = field(init=False)
    name: str
    amount: float
    payer: str
    beneficiaries: set[str]

    _id_counter: int = 0

    def __post_init__(self):
        type(self)._id_counter += 1
        self.id = type(self)._id_counter

    def __str__(self):
        return f"--------------\n --- {self.name} --- {self.amount} --- {self.payer.title()}\n --- {self.beneficiaries}\n--------------"
