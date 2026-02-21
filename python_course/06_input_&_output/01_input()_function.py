Input and Output in Python
📌 Introduction

Input and Output (I/O) are basic concepts in programming.

Input means taking data from the user or another source.

Output means displaying data to the user.

In Python, input and output are mainly handled using the input() and print() functions.

🔹 Input in Python

The input() function is used to take user input from the keyboard.

Syntax
input("message")
Example
name = input("Enter your name: ")
print("Hello", name)
Important Point

The input() function always returns data as a string.

Example:

age = input("Enter your age: ")
print(type(age))   # <class 'str'>
🔹 Type Casting with Input

Since input is always a string, we often convert it into other data types.

Integer Input
num = int(input("Enter a number: "))
print(num)
Float Input
price = float(input("Enter price: "))
print(price)
