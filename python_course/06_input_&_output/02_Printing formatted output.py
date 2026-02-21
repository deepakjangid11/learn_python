Printing Formatted Output in Python
📌 Introduction

Formatted output means displaying data in a structured and readable way.
Python provides several methods to format output, making programs clean, professional, and easy to understand.

🔹 1. Using Comma in print()

You can print multiple values separated by commas.

Example
name = "Deepak"
age = 21

print("Name:", name, "Age:", age)
Output
Name: Deepak Age: 21
🔹 2. String Concatenation (+)

Strings can be joined using the + operator.

Example
name = "Deepak"
print("Hello " + name)
Note

Only strings can be concatenated. Convert numbers using str().

age = 21
print("Age: " + str(age))
🔹 3. Using format() Method

The format() method inserts values inside placeholders {}.

Example
name = "Deepak"
age = 21

print("My name is {} and I am {} years old.".format(name, age))
With Index Positions
print("Name: {0}, Age: {1}".format(name, age))
🔹 4. Using f-Strings (Recommended ⭐)

F-strings are the modern and easiest way to format output.

Syntax
f"Text {variable}"
Example
name = "Deepak"
age = 21

print(f"My name is {name} and I am {age} years old.")
Advantages

Easy to read

Faster

Clean and professional

🔹 5. Formatting Numbers
Decimal Precision
pi = 3.14159265
print(f"Pi value: {pi:.2f}")
Output
Pi value: 3.14
🔹 6. Text Alignment

You can align text using formatting.

text = "Python"

print(f"{text:<10}")   # Left align
print(f"{text:>10}")   # Right align
print(f"{text:^10}")   # Center align
🔹 7. Multiple Values in One Line
name = "Deepak"
marks = 95

print(f"Student: {name} | Marks: {marks}")
