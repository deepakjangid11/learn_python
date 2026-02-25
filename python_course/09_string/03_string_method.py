String Methods in Python
What are String Methods?

String methods are built-in functions used to perform operations on strings such as changing case, searching, replacing, splitting, etc.

👉 Strings are immutable, so methods return a new string (they do not modify the original string).

1️⃣ Case Conversion Methods
upper()
text = "hello"
print(text.upper())

Output:

HELLO
lower()
text = "HELLO"
print(text.lower())
title()
text = "hello world"
print(text.title())
capitalize()
text = "python"
print(text.capitalize())
2️⃣ Removing Spaces
strip() – removes spaces from both sides
text = "  hello  "
print(text.strip())
lstrip() – removes left spaces
rstrip() – removes right spaces
3️⃣ Searching Methods
find()

Returns index of first occurrence.

text = "Python"
print(text.find("t"))
count()

Counts occurrences.

text = "banana"
print(text.count("a"))
startswith()
text = "Python"
print(text.startswith("Py"))
endswith()
print(text.endswith("on"))
4️⃣ Replace Method
replace()
text = "Hello World"
print(text.replace("World", "Python"))
5️⃣ Splitting and Joining
split()

Converts string into list.

text = "a,b,c"
print(text.split(","))
join()

Joins list into string.

data = ["Python", "is", "easy"]
print(" ".join(data))
6️⃣ Checking Methods
isalpha()
print("Hello".isalpha())
isdigit()
print("123".isdigit())
isalnum()
print("Hello123".isalnum())
