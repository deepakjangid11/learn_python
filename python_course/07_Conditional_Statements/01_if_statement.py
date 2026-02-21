If Statement in Python
Introduction

The if statement is used to make decisions in a program.
It executes a block of code only when a condition is true.

Decision making is one of the most important concepts in programming.

🔹 Syntax
if condition:
    # code to execute

If the condition is True, the code runs.
If the condition is False, the code is skipped.

🔹 Basic Example
age = 18

if age >= 18:
    print("You are eligible to vote")
Output
You are eligible to vote
🔹 Example with User Input
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
