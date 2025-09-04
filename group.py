from person import Person
from expense import Expense
from settlement import Settlement

class Group:
    def __init__(self, name):
        self.name = name
        self.members: dict[str, Person] = {}
        self.expenses: dict[int, Expense] = {}

    def add_member(self, person: Person):
        if person.name in self.members:
            raise ValueError(f"'{person.name}' is already a member")
        self.members[person.name.lower()] = person

    def __str__(self):
        return f"\n\n{self.name}\n{[name for name in self.members.keys()]}\n\n{"\n".join([f"{key}\n{value}"for key, value in self.expenses.items()])}"

    def add_expense(self, name: str, amount: float, payer: str, beneficiaries=None):
        payer_normalized = payer.strip().lower()
        if payer_normalized not in (all_members := self.members.keys()):
            raise ValueError(f"{payer_normalized} is not a member.")
        beneficiaries_normalized: set[str] = set()
        if beneficiaries is None:
            beneficiaries_normalized = set(self.members.keys())
        else:
            for member in beneficiaries:
                if (member_normalized := member.strip().lower()) not in all_members:
                    raise ValueError(f"{member} is not a member.")
                beneficiaries_normalized.add(member_normalized)
        expense = Expense(name, amount, payer_normalized, beneficiaries_normalized)
        self.expenses[expense.id] = expense

    def settleup(self):
        settlement = Settlement(self.expenses.values())
        return settlement.settleup()
