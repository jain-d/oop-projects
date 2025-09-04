from person import Person
from group import Group

person1 = Person("Mike Beltron") 
person2 = Person("Jason Herzog")
person3 = Person("Herb Dean")
person4 = Person("Marc Goddard")
person5 = Person("Herb Clove")

small_group = Group("UFC Library")

for person in (person1, person2, person3, person4, person5):
    small_group.add_member(person)

small_group.add_expense("Drinks", 400, "Mike Beltron")

small_group.add_expense("Food", 300, "Marc Goddard")

print(small_group.expenses)

print(small_group.settleup())
