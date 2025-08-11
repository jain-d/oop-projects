import random

class Dict:
    def __init__(self, sides):
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def roll_multiple(self, times) -> list[int]:
        return [self.roll() for _ in range(times)]


standard_dice = Dict(6)
print(standard_dice.roll_multiple(6))

