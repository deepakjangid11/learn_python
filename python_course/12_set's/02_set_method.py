Set Methods in Python
What are Set Methods?

Set methods are built-in functions used to add, remove, and perform operations on sets.

Sets store unique elements only.

1️⃣ add()

Adds a single element to the set.

s = {1, 2, 3}
s.add(4)
print(s)
2️⃣ update()

Adds multiple elements.

s = {1, 2, 3}
s.update([4, 5, 6])
print(s)
3️⃣ remove()

Removes an element (error if not found).

s = {1, 2, 3}
s.remove(2)
print(s)
4️⃣ discard()

Removes element without error.

s = {1, 2, 3}
s.discard(5)   # No error
5️⃣ pop()

Removes a random element.

s = {10, 20, 30}
s.pop()
print(s)
6️⃣ clear()

Removes all elements.

s = {1, 2, 3}
s.clear()
print(s)
7️⃣ union()

Combines two sets.

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
8️⃣ intersection()

Common elements between sets.

print(a.intersection(b))
9️⃣ difference()

Elements present in first set only.

print(a.difference(b))
🔟 symmetric_difference()

Elements not common in both sets.

print(a.symmetric_difference(b))
