🔹 What is Explicit Casting?

Explicit Casting means manual type conversion done by the programmer.

➡️ We use built-in functions to change one data type into another.

Python does NOT do this automatically — we must write it ourselves.

🔹 Why Use Explicit Casting?

✔ To convert user input into required type
✔ To perform calculations
✔ To change data format
✔ To avoid type errors

🔹 Common Explicit Casting Functions
1️⃣ int() → Convert to Integer
x = "100"
y = int(x)

print(y)
print(type(y))


Output:

100
<class 'int'>

2️⃣ float() → Convert to Float
a = "10"
b = float(a)

print(b)


Output:

10.0

3️⃣ str() → Convert to String
num = 25
text = str(num)

print(type(text))


Output:

<class 'str'>

4️⃣ bool() → Convert to Boolean
print(bool(1))   # True
print(bool(0))   # False
print(bool(""))  # False

5️⃣ list(), tuple(), set()
t = (1,2,3)
print(list(t))

l = [1,2,3]
print(tuple(l))

a = [1,2,2,3]
print(set(a))

🔹 Example Program
x = "50"
y = int(x)

result = y + 10
print(result)


Output:

60
