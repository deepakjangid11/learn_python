'''
Operators in Python
 Introduction:

An operator is a symbol used to perform operations on variables or values.
For example, +, -, *, / are operators.

Example:

a = 10
b = 5
print(a + b)   # Output: 15


Here + is an operator that performs addition.

Types of Operators in Python
1. Arithmetic Operators

These operators are used to perform mathematical calculations.

Operator	Meaning	Example
+	Addition	5 + 2 = 7
-	Subtraction	5 - 2 = 3
*	Multiplication	5 * 2 = 10
/	Division	5 / 2 = 2.5
%	Modulus (remainder)	5 % 2 = 1
**	Power	2 ** 3 = 8
//	Floor division	5 // 2 = 2

Example:

a = 10
b = 3
print(a + b)
print(a % b)

2. Comparison Operators

These operators compare two values and return True or False.

Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to

Example:

a = 10
b = 5
print(a > b)   # True

3. Logical Operators

These operators are used to combine conditions.

Operator	Meaning
and	True if both conditions are true
or	True if at least one condition is true
not	Reverses the result

Example:

a = 10
print(a > 5 and a < 20)

4. Assignment Operators

These operators are used to assign values to variables.

Operator	Example
=	x = 5
+=	x += 2
-=	x -= 2
*=	x *= 2
/=	x /= 2

Example:

x = 5
x += 3
print(x)

5. Membership Operators

These operators check whether a value exists in a sequence (like a list or string).

Operator	Meaning
in	Value exists
not in	Value does not exist

Example:

numbers = [1, 2, 3, 4]
print(2 in numbers)   # True

6. Identity Operators

These operators compare the memory location of two objects.

Operator	Meaning
is	Same object
is not	Not the same object

Example:

a = [1, 2]
b = a
print(a is b)   # True '''
