🔹 1. Allowed Characters

Variable names can contain:

Letters (A–Z, a–z)

Digits (0–9)

Underscore (_)

✔️ Examples:

name = "Deepak"
age1 = 21
student_name = "Rahul"

🔹 2. Must Start with Letter or Underscore

A variable name cannot start with a number.

✔️ Correct:

name1 = "Deepak"
_student = "Yes"


❌ Wrong:

1name = "Deepak"   # Error

🔹 3. No Spaces Allowed

Variable names cannot contain spaces.

❌ Wrong:

student name = "Deepak"


✔️ Correct:

student_name = "Deepak"

🔹 4. Case Sensitive

Python treats uppercase and lowercase as different variables.

age = 20
Age = 25


➡️ Both are different variables.

🔹 5. Keywords Cannot Be Used

Python reserved words (keywords) cannot be used as variable names.

❌ Wrong:

class = 10
for = 5
if = 3

🔹 6. Meaningful Names (Best Practice)

Always use clear and meaningful names.

✔️ Good:

total_marks = 450
student_age = 21


❌ Bad:

x = 450
a = 21

🔹 7. Use Snake Case (Recommended Style)

Python follows snake_case style.

✔️ Recommended:

total_price
user_name
mobile_number

🔹 8. Avoid Special Symbols

Special characters are not allowed.

❌ Wrong:

price@ = 100
total# = 50

🔹 Example Program
student_name = "Deepak"
age = 21
course_name = "Python"

print(student_name, age, course_name)
