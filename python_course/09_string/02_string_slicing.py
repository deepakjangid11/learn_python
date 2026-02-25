String Slicing in Python
What is String Slicing?

String slicing is used to extract a part (substring) of a string using indexes.

Syntax:

string[start : end : step]

start → starting index (included)

end → ending index (excluded)

step → jump between characters (optional)

Example String
text = "Python"

Index positions:

P  y  t  h  o  n
0  1  2  3  4  5
Basic Slicing
1. Start to End
print(text[0:3])

Output:

Pyt
2. From Start Index to End
print(text[2:])

Output:

thon
3. From Beginning to End Index
print(text[:4])

Output:

Pyth
Using Step
print(text[0:6:2])

Output:

Pto

(Characters are skipped by 2 steps)

Negative Slicing

Negative indexing starts from the end.

print(text[-4:-1])

Output:

tho
Reverse String Using Slicing
print(text[::-1])

Output:

nohtyP
