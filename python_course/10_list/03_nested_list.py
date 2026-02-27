Nested Lists in Python
What is a Nested List?

A nested list is a list that contains another list as its element.

➡️ Simply: List inside another list.

Example of Nested List
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data)
Accessing Elements in Nested List

First index → outer list
Second index → inner list

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(data[0])      # [1, 2, 3]
print(data[1][2])   # 6
Example with Different Data Types
student = [
    ["Deepak", 21],
    ["Rahul", 22],
    ["Amit", 20]
]

print(student[0][0])   # Deepak
Modifying Nested List
data = [[1, 2], [3, 4]]

data[0][1] = 10
print(data)

Output:

[[1, 10], [3, 4]]
Looping Through Nested List
data = [[1, 2], [3, 4], [5, 6]]

for row in data:
    for item in row:
        print(item, end=" ")

Output:

1 2 3 4 5 6
