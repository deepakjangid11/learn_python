Creating Sets in Python
What is a Set?

A set is a collection of unique elements.

✔ Unordered
✔ Mutable (changeable)
✔ No duplicate values allowed
✔ Uses curly braces { }

1️⃣ Creating a Set
s = {1, 2, 3, 4}
print(s)
2️⃣ Set with Duplicate Values

Duplicates are automatically removed.

s = {1, 2, 2, 3, 3, 4}
print(s)

Output:

{1, 2, 3, 4}
3️⃣ Creating an Empty Set (Important)
s = set()
print(type(s))

⚠️ {} creates a dictionary, not a set.

4️⃣ Creating Set Using set() Function

From list:

s = set([1, 2, 3, 4])
print(s)

From string:

s = set("Python")
print(s)
5️⃣ Set with Different Data Types
s = {10, "Hello", 3.5, True}
print(s)
6️⃣ Accessing Set Elements

❌ Sets do NOT support indexing.

s = {1, 2, 3}
# print(s[0])   # Error

Use loop instead:

for i in s:
    print(i)
