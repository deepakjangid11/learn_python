Identifiers in Python:

What are Identifiers?

Identifiers are the names given to variables, functions, classes, modules, or other objects in Python.
They are used to identify these elements in a program.

Example:

name = "Deepak"   # name is an identifier
age = 21          # age is an identifier

def greet():      # greet is an identifier
    print("Hello")

Rules for Naming Identifiers

Python has some rules that must be followed:

Must start with a letter (A–Z or a–z) or underscore (_)

name = "Deepak"   # valid
_age = 21         # valid
1name = "abc"     # invalid


Cannot start with a number

123abc = 10   # invalid


Can contain letters, numbers, and underscores

student1 = "Ram"     # valid
total_marks_2024 = 90   # valid


Cannot use special characters

user-name = "abc"   # invalid (- not allowed)


Identifiers are case-sensitive

name = "Deepak"
Name = "Rahul"

print(name)  # Different from Name


Cannot use Python keywords

if = 10   # invalid
class = "A"  # invalid


To see keywords:

import keyword
print(keyword.kwlist)
