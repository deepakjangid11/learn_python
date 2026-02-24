🔹 Pass Statement in Python

The pass statement means “do nothing”.

➡️ It is used when Python needs a statement syntactically, but you don’t want to write any code yet.

🔹 Syntax
pass
🔹 Example 1 (Empty Loop)
for i in range(5):
    pass

💡 Loop runs, but nothing happens.

🔹 Example 2 (Empty Function)
def my_function():
    pass

✔ Function is created
❌ No code inside yet

🔹 Example 3 (Condition)
x = 10

if x > 5:
    pass
else:
    print("Small number")
