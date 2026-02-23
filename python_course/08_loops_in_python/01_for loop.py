For Loop in Python – 

For loop ka use kisi sequence (list, string, range, etc.) ko repeat / iterate karne ke liye hota hai.

Simple words:
➡️ Jab hume koi kaam baar-baar karna ho, tab for loop use karte hain.

🔹 Basic Syntax
for variable in sequence:
    # code block
🔹 Example 1 — Simple For Loop
for i in range(5):
    print(i)

Output:

0
1
2
3
4
🔹 Example 2 — Loop with List
numbers = [10, 20, 30]

for num in numbers:
    print(num)
🔹 Example 3 — Loop with String
name = "Deepak"

for ch in name:
    print(ch)
🔹 Using range()

range() numbers generate karta hai.

range(start, stop, step)

Example:

for i in range(1, 6):
    print(i)

Output → 1 2 3 4 5
