if-elif-else Statement in Python
Introduction

The if-elif-else statement is used when we need to check multiple conditions in a program.

Python checks conditions one by one:

If the first condition is true → that block runs

Otherwise, Python checks the next condition (elif)

If none are true → else block runs

🔹 Syntax
if condition1:
    # code block 1
elif condition2:
    # code block 2
elif condition3:
    # code block 3
else:
    # default block
🔹 Basic Example
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
Output
Grade B
🔹 Example with User Input
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
