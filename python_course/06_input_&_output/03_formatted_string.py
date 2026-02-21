f-Strings in Python
📌 Introduction

f-Strings (Formatted String Literals) are used to insert variables or expressions inside a string in a simple and readable way.

They were introduced in Python 3.6 and are the recommended method for string formatting because they are clean, fast, and easy to understand.

🔹 Syntax
f"Text {variable}"

Add f before the string.

Place variables or expressions inside { }.

🔹 Basic Example
name = "Deepak"
age = 21

print(f"My name is {name} and I am {age} years old.")
Output
My name is Deepak and I am 21 years old.
🔹 Using Expressions Inside f-Strings

You can directly perform operations inside {}.

a = 10
b = 5

print(f"Sum = {a + b}")
Output
Sum = 15
🔹 Calling Functions
name = "deepak"

print(f"Uppercase: {name.upper()}")
Output
Uppercase: DEEPAK
🔹 Number Formatting
Decimal Precision
pi = 3.14159265
print(f"Pi value: {pi:.2f}")
Output
Pi value: 3.14
🔹 Alignment in f-Strings
text = "Python"

print(f"{text:<10}")   # Left align
print(f"{text:>10}")   # Right align
print(f"{text:^10}")   # Center align
🔹 Adding Spaces or Padding
num = 25
print(f"{num:5}")    # width = 5
🔹 Multiple Variables
name = "Deepak"
marks = 95

print(f"Student: {name} | Marks: {marks}")
🔹 Why Use f-Strings? ⭐

Easy to read

Less code

Faster than format()

Supports expressions directly

Professional coding style

🔹 Practice Example
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, next year you will be {age + 1} years old.")
