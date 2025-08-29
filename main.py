from book import Book
from member import Member
from library import Library

# Book
"""
from book import Book

book23 = Book("Crime & Punishment", "Dostoyevsky", 3)

a_book_dict: dict = {
    "title": "CS: Distilled",
    "author": "Wladston",
    "in_stock": 1
}

print(book23)
print(book23.author)

results = book23.to_dict()

print(type(results), "\n", results)

book24 = Book.from_dict(a_book_dict)

print(book24)

print(book24.title)
"""



# Member
"""
user_mike = Member("Mike")
print(vars(user_mike))
user_mike.borrow_book("CS: Distilled")
user_mike.borrow_book("Crime & Punishment")
print(vars(user_mike))
user_mike.return_book("Pride and Prejudice")
print(vars(user_mike))
"""


# Library
data_file = "./data.json"
sample_library = Library.load_from_file(data_file)

#print(sample_library)

user_mark = Member("Mark")
crime_n_punishment = Book("Crime & Punishment", "Dostoyevsky", 3)
pride_n_prejudice = Book("Pride & Prejudice", "Austin", 1)

sample_library.add_book(pride_n_prejudice)
sample_library.add_book(crime_n_punishment)

sample_library.add_member(user_mark)
sample_library.lend_book("Crime & Punishment", "Mark")
sample_library.lend_book("Pride & Prejudice", "Mark")

#print("Mark's", user_mark.list_books())

#print(sample_library)

sample_library.save_to_file(data_file)

