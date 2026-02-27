Creating Lists in Python
What is a List?

A list is a collection of items stored in a single variable.
Lists are:

✔ Ordered
✔ Mutable (changeable)
✔ Allow duplicate values
✔ Can store different data types

1️⃣ Creating an Empty List
my_list = []
print(my_list)

OR

my_list = list()
print(my_list)
2️⃣ Creating a List with Elements
numbers = [10, 20, 30, 40]
print(numbers)
3️⃣ List with Different Data Types (Heterogeneous)
data = ["Deepak", 21, 75.5, True]
print(data)
4️⃣ Creating List Using list() Function
numbers = list((1, 2, 3, 4))
print(numbers)
5️⃣ Creating List from String
text = list("Python")
print(text)

Output:

['P', 'y', 't', 'h', 'o', 'n']
6️⃣ Creating List Using Range
numbers = list(range(1, 6))
print(numbers)

Output:

[1, 2, 3, 4, 5]
7️⃣ Nested List (List inside List)
data = [[1, 2], [3, 4], [5, 6]]
print(data)
