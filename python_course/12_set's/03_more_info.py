Union, Intersection, Difference in Python Sets

Sets are mainly used for mathematical operations like union, intersection, and difference.

Example Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
1️⃣ Union
Definition

Union combines all unique elements from both sets.

Method
print(A.union(B))

OR

print(A | B)
Output
{1, 2, 3, 4, 5, 6}
2️⃣ Intersection
Definition

Intersection returns common elements present in both sets.

Method
print(A.intersection(B))

OR

print(A & B)
Output
{3, 4}
3️⃣ Difference
Definition

Difference returns elements present in first set but not in second set.

Method
print(A.difference(B))

OR

print(A - B)
Output
{1, 2}
Difference (Reverse)
print(B - A)

Output:

{5, 6}

Try using operators (|, &, -)
