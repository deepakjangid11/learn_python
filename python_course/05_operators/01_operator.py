🔹 What are Operators?

Operators are special symbols used to perform operations on variables and values.

Example:

a = 10
b = 5

print(a + b)


Here + is an operator.

🔹 Types of Operators in Python
1️⃣ Arithmetic Operators

Used for mathematical calculations.

Operator	Meaning	Example
+	Addition	a + b
-	Subtraction	a - b
*	Multiplication	a * b
/	Division	a / b
%	Modulus (remainder)	a % b
//	Floor division	a // b
**	Power	a ** b

Example:

a = 10
b = 3

print(a + b)
print(a % b)
print(a ** b)

2️⃣ Comparison (Relational) Operators

Used to compare values. Result is True / False.

Operator	Meaning
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater or equal
<=	Less or equal

Example:

a = 10
b = 5

print(a > b)
print(a == b)

3️⃣ Assignment Operators

Used to assign values.

Operator	Example	Same As
=	x = 5	
+=	x += 2	x = x + 2
-=	x -= 2	x = x - 2
*=	x *= 2	x = x * 2
/=	x /= 2	x = x / 2

Example:

x = 10
x += 5
print(x)

4️⃣ Logical Operators

Used with conditions.

Operator	Meaning
and	Both conditions true
or	Any one true
not	Reverse result

Example:

a = 10
b = 5

print(a > 5 and b < 10)

5️⃣ Membership Operators

Check if value exists in sequence.

Operator	Meaning
in	Present
not in	Not present

Example:

li = [1,2,3,4]

print(2 in li)
print(5 not in li)

6️⃣ Identity Operators

Check memory location (same object or not).

Operator	Meaning
is	Same object
is not	Different object

Example:

a = [1,2]
b = a

print(a is b)

7️⃣ Bitwise Operators

Work on binary numbers.

Operator	Meaning
&	AND
|	OR
^	XOR
~	NOT
<<	Left shift
>>	Right shift

Example:

a = 5
b = 3

print(a & b)
