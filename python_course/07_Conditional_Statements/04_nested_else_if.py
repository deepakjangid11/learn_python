Nested else if (Nested if-else) – 

Nested else if means using an if-else statement inside another if or else block.
Simple words: ek condition ke andar dusri condition check karna.

🔹 Basic Structure
if condition1:
    if condition2:
        # code block
    else:
        # code block
else:
    # code block
🔹 Example (Easy)
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")
🔹 How it works (Step by Step)

First condition check hoti hai → num > 0

Agar True hai, to andar wali condition check hogi → num % 2 == 0

Uske according output print hoga.

🔹 Real-life Example
age = 20

if age >= 18:
    if age >= 21:
        print("Eligible for voting and driving")
    else:
        print("Eligible for voting only")
else:
    print("Not eligible")
🔹 Difference (Normal vs Nested)

Normal if-else → ek level ki condition

Nested if-else → multiple levels ki conditions
