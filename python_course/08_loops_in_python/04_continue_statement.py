Continue Statement in Python

The continue statement is used to skip the current iteration of a loop and move to the next iteration.

➡️ Loop stops only for that step, not completely.

🔹 Syntax
for / while condition:
    if condition:
        continue
🔹 Example (For Loop)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
Output:
1
2
4
5

💡 Number 3 is skipped.

🔹 Example (While Loop)
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
Output:
1
2
4
5
🔹 Real Life Meaning

Imagine you are checking students:

➡️ If one student is absent → you skip him and check the next student.

That skipping = continue
