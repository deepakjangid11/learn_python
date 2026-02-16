'''
Type Casting in Python
Introduction

Type casting is the process of converting one data type into another data type.
Python provides built-in functions to perform type casting such as int(), float(), str(), and bool().

Type casting is useful when we need to perform operations on different types of data, for example converting user input (string) into numbers for calculations.

Types of Type Casting
1. Implicit Type Casting

In implicit type casting, Python automatically converts one data type into another to avoid data loss.

Example:

a = 5       # int
b = 2.5     # float

c = a + b   # Python converts int to float automatically
print(c)
print(type(c))


Output:

7.5
<class 'float'>

2. Explicit Type Casting

In explicit type casting, the programmer manually converts the data type using built-in functions.

Common Functions:

int() → converts to integer

float() → converts to float

str() → converts to string

bool() → converts to boolean

Example:

x = "10"
y = int(x)   # converting string to integer

print(y)
print(type(y))


Output:

10
<class 'int'>

Practical Example Program
# Practical example of type casting

# Taking input from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Converting string input to integer
num1 = int(num1)
num2 = int(num2)

# Performing calculation
sum_result = num1 + num2

print("Sum =", sum_result)'''
