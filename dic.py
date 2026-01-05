# Dictionary is a built-in data type in Python that stores data in key-value pairs.
# It is mutable, meaning its contents can be changed after creation.
# Dictionaries are defined using curly braces {}.
# Keys must be unique and immutable (string, number, tuple).
# Values can be of any data type and can be duplicated.

# Creating a dictionary
student_data = {
    "name": "Deepak Jangid",
    "roll_number": 101,
    "class": "A23"
}

# Adding a new key-value pair
student_data["age"] = 21

print("Student Data:", student_data)

# Accessing value using key
print("Student Name:", student_data["name"])

# Updating a value
student_data["age"] = 31

# Adding another key
student_data["country"] = "India"

# Iterating through dictionary
print("\nIterating through dictionary:")
for key, value in student_data.items():
    print(f"{key}: {value}")

# Sum of numeric values in dictionary
sum_values = 0
for value in student_data.values():
    if isinstance(value, int):
        sum_values += value

print("\nSum of numeric values:", sum_values)

# Maximum numeric value in dictionary
max_value = max(
    value for value in student_data.values() if isinstance(value, int)
)
print("Maximum numeric value:", max_value)

# Print key-value pairs where value is greater than 50
print("\nValues greater than 50:")
for key, value in student_data.items():
    if isinstance(value, int) and value > 50:
        print(key, value)
