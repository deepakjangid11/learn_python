Difference Between List and Tuple in Python

Both List and Tuple are used to store multiple values, but they have important differences.

Basic Difference
Feature	List	Tuple
Syntax	[ ]	( )
Mutable	✔ Yes	❌ No
Performance	Slower	Faster
Methods	Many	Few
Memory Usage	More	Less
Use Case	Data that changes	Fixed data
1️⃣ Syntax Difference
List
li = [10, 20, 30]
Tuple
t = (10, 20, 30)
2️⃣ Mutability
List (Mutable)
li = [10, 20, 30]
li[0] = 100
print(li)

Output:

[100, 20, 30]
Tuple (Immutable)
t = (10, 20, 30)
t[0] = 100   # Error
3️⃣ Methods
List Methods

append()

insert()

remove()

pop()

sort()

reverse()

Tuple Methods

count()

index()

4️⃣ Performance

Tuple is faster because it cannot be changed.

List is slightly slower due to flexibility.

5️⃣ When to Use?
Use List when:

✔ Data changes frequently
✔ Need add/remove operations

Use Tuple when:

✔ Data should not change
✔ Better performance required

Example
# List example
students = ["Ram", "Shyam"]

# Tuple example
colors = ("Red", "Blue", "Green")
Interview One-Line Answer

➡️ List is mutable, Tuple is immutable.

Practice Tasks

Create list and tuple

Modify list element

Try modifying tuple (observe error)

Compare list and tuple speed

If you want, I can give you 🔥 List vs Tuple interview explanation (30-second answer) — very useful for mock interviews.
