# Mini Splitwise

There are people(**PERSON**). Some of them come together to form a group(**GROUP**). In that group, a particular person purchases good or services with his/her own personal money for (some) the members of the group. So the members of the group who consumed the service/product own the purchasing member some money.
With this the aim is to build a service that at the end of it all settle up everything, and gives us a list of who owns whom, how much.

Initial thoughts
So I have worked out that I will most certainly need the following classes-
1. Person
2. Group

I started with these 2, but then I kindof realized that there needs to be an `Expense` class as well.

So, Person class has a person's name, and a list of the groups he is a part of. No methods for the person as of yet.

A group, will have a name and then most importantly, the records of people that are in the group. I was thinking a list, but then I thought a dict will be much more practical(with the key: str being the name of the person, and value being the associated Person object). This will make the membership check easy and fast.

In retrospect, I can have the same format on the Person class as well, where I can make the list of Group that a person is a part of, a dict too, keys being the name of the group and values being the associated Group object. But I am not sure weather this is necessary or not. Perhaps that entire list of Group a member is a part of is not required at all.

The third thing the group will have is a list of Expenses.


The Expenses class as I can think of now, is more fitting as a data class, because all the Expenses class will have is the amount: float, the payee: Person, and the members of group among whom the expense should be split(if not specified, it will be split between all members of the group equally).
Now with the Expense class, it needs to have a sense of who the members of the group are. Any arbitrary number of people may exist, but it should only know of the members that are in the group. In other words, it should be aware only of the environment it was created in. So this expense should have access to the data attribute of the group that keep tracks of all its members.
Since Expense objects will be created inside the group, I can have this sent to for __init__.


These are some general observations that I have noted. Still too early to get into the specifics. So there is just my thought process and the areas where I am having conflicting opinions. OOP design thinking is a different kind of hard.
