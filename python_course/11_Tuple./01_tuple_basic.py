Tuple Basics in Python
What is a Tuple?

A tuple is a collection of multiple values stored in a single variable.

✔ Ordered
✔ Immutable (cannot be changed)
✔ Allows duplicate values
✔ Can store different data types

Creating a Tuple

Tuples are created using round brackets ( ).

t = (10, 20, 30)
print(t)
Tuple with Different Data Types
data = ("Deepak", 21, 75.5, True)
print(data)
Single Element Tuple (Important)
t = (5,)
print(type(t))

⚠️ Comma is required, otherwise it is not a tuple.

Accessing Tuple Elements

Index starts from 0.

t = (10, 20, 30)

print(t[0])   # 10
print(t[2])   # 30
Negative Indexing
print(t[-1])   # 30
Tuple Slicing
t = (10, 20, 30, 40, 50)

print(t[1:4])

Output:

(20, 30, 40)
Tuple is Immutable

❌ You cannot change values:

t = (10, 20, 30)
t[0] = 100  
