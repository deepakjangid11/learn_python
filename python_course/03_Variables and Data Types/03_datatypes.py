🔹 What are Data Types in Python?

Data Type tells Python what kind of value a variable is storing.

Example:

x = 10        # Integer
name = "Deepak"   # String


Python automatically detects the data type (Dynamic Typing).

🔹 Main Data Types in Python
1️⃣ Numeric Data Types

Used for numbers.

✔ Integer (int)

Whole numbers without decimal.

a = 10
b = -5

✔ Float (float)

Numbers with decimal point.

price = 99.5

✔ Complex (complex)

Numbers with imaginary part.

z = 3 + 4j

2️⃣ String (str)

Used to store text or characters.

name = "Deepak"
city = 'Jaipur'


Strings are written inside quotes.

3️⃣ Boolean (bool)

Represents True or False values.

is_student = True
is_logged_in = False


Used mostly in conditions.

4️⃣ List (list)

Ordered collection that can be changed (mutable).

numbers = [1, 2, 3, 4]


✔ Allows duplicates
✔ Can store different data types

5️⃣ Tuple (tuple)

Ordered collection but cannot be changed (immutable).

colors = ("red", "blue", "green")

6️⃣ Set (set)

Unordered collection of unique values.

data = {1, 2, 3, 4}


✔ No duplicates allowed

7️⃣ Dictionary (dict)

Stores data in key : value pair.

student = {
    "name": "Deepak",
    "age": 21
}

🔹 Check Data Type

Use type() function.

x = 10
print(type(x))


Output:

<class 'int'>
