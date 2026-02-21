If-Else Statement in Python
Introduction

The if-else statement is used for decision making in Python.
It allows a program to choose between two different blocks of code based on a condition.

If the condition is True → if block executes

If the condition is False → else block executes

🔹 Syntax
if condition:
    # code if condition is true
else:
    # code if condition is false
🔹 Basic Example
age = 20

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
Output
You are eligible to vote
🔹 Example with User Input
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
