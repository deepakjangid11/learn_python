# write a program to print the cubes of number from 1 to 5:

num = 1
while num<=5:
    print(num**3, end= ' ')
    num+=1

# WRITE A PROGRAM TO PRINT ALL ODD NUMBERS FROM 1 TO 10:

num = 1
while num <= 20:
    if num % 2 != 0:
        print(num, end=' ')
    num += 1

# WRITE A PROGRAM TO CALCULATE THE PRODUCT OF NUMBER FROM 1 TO 5: (FACTORIAL NUMBER IN WHILE LOOPS)

num = 1 
mlt = 1
while num <=5:
    mlt*=num
    num+=1
print(mlt)

# WRITE A PROGRAM TO REVERSE EACH WORD IN THE SENTENCE "HELLO WORLD" USING WHILE LOOPS:

sentence = input("enter sentence: ")
i = len(sentence)-1
while i>=0:
    print(sentence[i],end=' ')
    i-=1

# WRITE A PROGRAM TO CHECK THE NUMBER IS A PALINDROME OR NOT:
num = int(input("Enter Any Number : "))
temp = num
rev = 0 
while (num != 0 ):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)

if temp == rev:
    print("this is a palindrome number.")
else:
    print("not a palindrome number")

# WRITE A PROGRAM TO REVERSE THE PROVIDED INPUT NUMBER:

num = int(input("Enter Any Number: "))
temp = num
rev = 0
while(num != 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)

# WRITE A PROGRAM TO PRINT FACTORIAL NUMBER:
num = int(input("Enter Any Number : "))
fact = 1

while (num > 0):
    fact = fact * num 
    num = num - 1 
print (fact)

# WRITE A PROGRAM TO PRINT AMSTROME NUMBER:
n = 153
temp = n
order = n
sum = 0
count = 0
while n != 0:
    n = n//10
    count += 1

while temp != 0:
    m = temp%10
    sum += m**count
    temp = temp//10

if sum == order:
    print("armstrome number")
else:
    print("not armstrome number")

