🔹 Break Statement in Python

The break statement is used to stop a loop immediately, even if the loop condition is still true.

➡️ When Python sees break, it exits the loop instantly.

🔹 Syntax
for / while condition:
    if condition:
        break
🔹 Example (For Loop)
for i in range(1, 6):
    if i == 3:
        break
    print(i)
Output:
1
2

💡 Loop stops when i becomes 3.

🔹 Example (While Loop)
num = 1

while num <= 5:
    if num == 4:
        break
    print(num)
    num += 1
Output:
1
2
3
