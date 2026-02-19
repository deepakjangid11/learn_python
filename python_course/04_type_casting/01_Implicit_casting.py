🔹 What is Implicit Casting?

Implicit Casting means automatic type conversion done by Python.

➡️ Python automatically converts one data type into another without writing any extra code.

This happens mostly when different data types are used in the same expression.

🔹 Example 1 – int + float
a = 10      # int
b = 5.5     # float

c = a + b

print(c)
print(type(c))


Output:

15.5
<class 'float'>


✔ Python automatically converted int → float.

🔹 Example 2 – int + complex
x = 5
y = 2 + 3j

z = x + y
print(z)
print(type(z))


Output:

(7+3j)
<class 'complex'>


✔ int automatically converted into complex.
