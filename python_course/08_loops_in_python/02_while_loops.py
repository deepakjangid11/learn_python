While Loop in Python – 

A while loop is used to execute a block of code repeatedly as long as a condition is True.

Simple meaning:
➡️ The loop keeps running until the condition becomes False.

🔹 Basic Syntax
while condition:
    # code block
🔹 Example 1 — Simple While Loop
i = 1

while i <= 5:
    print(i)
    i += 1

Output:

1
2
3
4
5
🔹 How it Works

The condition is checked (i <= 5)

If True → code executes

Value is updated (i += 1)

When the condition becomes False → loop stops

🔹 Example 2 — Countdown
num = 5

while num > 0:
    print(num)
    num -= 1
🔹 Important Point ⚠️

If the condition never becomes False, it creates an infinite loop.

Example (Wrong):

i = 1
while i <= 5:
    print(i)   # i is never updated
