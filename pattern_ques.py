# num = int(input("enter : "))
# for i in range (2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#      print("prime")


# num = int(input("ENter any number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# print(fact)

# num = int(input("Enter any number :"))

# for i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# num = int(input("enter number :"))
# sum = 0

# for i in range(num):
#     if num % i == 0:
#         sum +=i
#     if sum == num:
#         print("perfect number")
#     else:
#         print("not")

# num = int(input("enter number:"))
# temp = num 
# rev = 0

# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 +digit 
#     temp = temp // 10
# if rev == num:
#     print("palindrome")
# else :
#     print("not")


# num = int(input("enter number: "))
# temp = num
# sum = 0                     
# digit_count = len(str(num))

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digit_count
#     temp = temp // 10

# if sum == num:
#     print("armstrong")
# else:
#     print("not")

#F
# num = int(input("enter number :"))

# a = 0
# b = 1

# for i in range(num):
#     print(a,end= ' ')
#     a, b=b , a+b

# num = int(input("Enter number: "))
# fact = 1


# for i in range(1 ,num+1):
#     fact *= i
# print(fact)

# num = int(input("Enter number: "))


# for i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else : 
#     print("prime")


# for i in range(0,5):
#     for j in range(i+1):
#         print("*",end = ' ')
#     print()

# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*",end = ' ')
#     print()

# num = int(input("Enter number: "))
# temp = num 
# digit_count= len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digit_count
#     temp = temp // 10

# if sum == num:
#     print("amstro,me")
# else:
#     print("not")

# for i in range(5, 0, -1):
#      print(" "*(5-i),end = ' ')
#      print("*"*i)
 
# for i in range(1,6):
#      print(" "*(5-i), end = ' ')
#      print("*"*(2*i-1))

# for i in range(5, 0 ,-1):
#      print(" "*(5-i),end = ' ')
#      print("*"*(2*i-1))


# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2*i - 1))
# for i in range(n-1, 0, -1):
#     print(" " * (n - i) + "*" * (2*i - 1))

# for i in range(1,6):
#     print(" "*(5-i),end = ' ')
#     print("*"*(2*i-1))
# for i in range(5,0,-1):
#     print(" "*(5-i),end = ' ')
#     print("*"*(2*i-1))




# ASSGNMENT

# 1.

#  * * * *
#   * * * *
#    * * * *
#     * * * *

# for i in range(4):
#     print(" " * i + "* " * 4)


# 2.

#  *****
#  *   *
#  *   *
#  *****

# for i in range(5):
#     if i == 0 or i == 4:
#         print("*" * 6)
#     else:
#         print("*" + " " * 4 + "*")

# 3.

# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65 + j), end="")
#     print()

# 4. 

# A
# BB
# CCC
# DDDD
# EEEEE

# for i in range(5):
#     ch = chr(65 + i)
#     print(ch * (i + 1))

# 5.

#     E
#    D E
#   C D E
#  B C D E
# A B C D E

# for i in range(5):
#     print(" " * (4 - i), end="")
#     for j in range(i, 5):
#         print(chr(65 + j), end=" ")
#     print()

# 6.

# *       |    1
# **      |    1 2
# * *     |    1 2 3
# *  *    |    1 2 3 4
# *****   |    1 2 3 4 5

# n = 5
# Left side stars
# for i in range(1, n+1):
#     if i == 1:
#         print("*", end="")
#     elif i == n:
#         print("*" * n, end="")
#     else:
#         print("*" + " " * (i-2) + "*", end="")

#     print("   |   ", end="")

# Right side numbers
# for j in range(1, i+1):
#     print(j, end=" ")
# print()

# 7.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# A
# A B
# A B C
# A B C D
# A B C D E

# n = 5
# Left numbers
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# print()

# Right alphabets
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

# 8.

# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1

# A B C D E
#   A B C D
#     A B C
#       A B
#         A

# for i in range(5, 0, -1):
#     print("  " * (5 - i), end="")  
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(5, 0, -1):
#     print("  " * (5 - i), end="")
#     ch = 65
#     for j in range(i):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()

# 9.

#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *

# for i in range(5, 0, -1):
#     print(" " * i, end="")
#     for j in range(5):
#         print("*", end=" ")
#     print()

# 10.

#         1 2 3 4 5
#       1 2 3 4 5
#     1 2 3 4 5
#   1 2 3 4 5
# 1 2 3 4 5

# for i in range(5, 0, -1):
#     print("  " * (i - 1), end="")
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()

# 11.

#         A B C D E
#       A B C D E
#     A B C D E
#   A B C D E
# A B C D E

# for i in range(5, 0, -1):
#     print("  " * (i - 1), end="")
#     ch = 65
#     for j in range(5):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()

# 12.

#     *
#    ***
#   *****
#  *******

# n = 4
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))

# 13.

#     *
#    *  *
#   *    *
#  ********

# n = 4
# print(" "*(n-1) + "*")    
# for i in range(1, n-1):
#     print(" "*(n-i-1) + "*" + " "*(2*i-1) + "*")
# print("*"*(2*n))      


# 14.

# *************
#   *********
#    *******
#      ***
#       *

# n = 5
# stars = 11 
# for i in range(n):
#     print(" "*(2*i) + "*"*(stars - 2*i))

# 15.

# *
# **
# ***
# ****
# ***
# **
# *

# n = 4
# for i in range(1, n+1):
#     print("*" * i)
# for i in range(n-1, 0, -1):
#     print("*" * i)

# 16.

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# n = 5
# # increasing triangle
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*i)

# # decreasing triangle
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "*"*i)

# 17.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2*i - 1))
# for i in range(n-1, 0, -1):
#     print(" " * (n - i) + "*" * (2*i - 1))

# 18.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5

# n = 5
# for i in range(1, n+1):
#     if i == 1:
#         print(1)
#     elif i == n:
#         for j in range(1, n+1):
#             print(j, end=" ")
#         print()
#     else:
#         print("1" + " "*(2*i-3) + str(i))

#     1
#    2 3
#   3 4 5
#  4 5 6 7
# 5 6 7 8 9

# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     num = i
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

#     1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5

# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     if i == 1:
#         print(1)
#     elif i == n:
#         for j in range(1, n+1):
#             print(j, end=" ")
#         print()
#     else:
#         print("1" + " "*(2*i-3) + str(i))


# 1 2 3 4 5
# 1     5
# 1   4
# 1 3
# 1

# n = 5
# for i in range(n, 0, -1):
#     if i == n:
#         for j in range(1, n+1):
#             print(j, end=" ")
#         print()
#     elif i == 1:
#         print(1)
#     else:
#         print("1" + " "*(2*i-3) + str(i))

# 19.

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input("Enter rows: "))
# for i in range(1, n+1):
#     print(" "*(n-i) + "* " * i)
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "* " * i)

#          1
#       1 2 3
#     1 2 3 5 7
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1

# n = int(input("Enter rows: "))
# for i in range(1, n+1):
#     print(" "*(n-i) + " ".join(str(x) for x in range(1, 2*i)))
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + " ".join(str(x) for x in range(1, 2*i)))

# 20.

# 1 2 3 4 5 6 7 8 9  
#   1 2 3 4 5 6 7  
#     1 2 3 4 5  
#       1 2 3  
#         1  
#       1 2 3  
#     1 2 3 4 5  
#   1 2 3 4 5 6 7  
# 1 2 3 4 5 6 7 8 9

# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i) + " ".join(str(x) for x in range(1, 2*i)))
# for i in range(2, n+1):
#     print(" " * (n - i) + " ".join(str(x) for x in range(1, 2*i)))

# A B C D E F G H I
#   A B C D E F G
#     A B C D E
#       A B C
#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I

# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i) + " ".join(chr(64 + x) for x in range(1, 2*i)))
# for i in range(2, n+1):
#     print(" " * (n - i) + " ".join(chr(64 + x) for x in range(1, 2*i)))

# 21.

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

#  n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 1 2 3 4 5
# 1       5
# 1       5
# 1       5
# 1 2 3 4 5

# n = 5
# for i in range(n):
#     for j in range(1, n+1):
#         if i == 0 or i == n-1 or j == 1 or j == n:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# A B C D E
# A       E
# A       E
# A       E
# A B C D E

# n = 5
# for i in range(n):
#     for j in range(1, n+1):
#         ch = chr(64 + j)   # 65 = 'A'
#         if i == 0 or i == n-1 or j == 1 or j == n:
#             print(ch, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 22.

#     *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#     *

# n = 4
# for i in range(1, n+1):
#     print(" "*(n-i) + "*" + " "*(2*i-3) + ("*" if i>1 else ""))
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "*" + " "*(2*i-3) + ("*" if i>1 else ""))

#     A
#   A   C
#  A     E
# A       G
#  A     E
#   A   C
#     A

# n = 4
# alphabet = ["A","C","E","G"]
# for i in range(1, n+1):
#     print(" "*(n-i) + alphabet[i-1] + " "*(2*i-3) + (alphabet[i-1] if i>1 else ""))
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + alphabet[i-1] + " "*(2*i-3) + (alphabet[i-1] if i>1 else ""))

# 23.

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# n = 5
# for i in range(n):
#     print(" "*(n-i), end="")
#     num = 1
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i-j) // (j+1)
#     print()

# 1. Square of stars

# *****
# *****
# *****
# *****
# *****

# for i in range(6):
#     for j in range(6):               
#         print("*",end =' ')
#     print()

# 2. Right-angled triangle

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()

# 3. Inverted right-angled trianglex

# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=' ')
#     print()

# 4. Triangle with numbers

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# 5. Same number triangle

# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end = ' ')
#     print()

# 6. Square of numbers

# 11111
# 22222
# 33333
# 44444
# 55555

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end= ' ')
#     print()

# 7. Triangle of alphabets

# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(1,6):
#     for j in range(65,65+i):
#         print(chr(j),end=' ')
#     print()

# 8. Square of alphabets

# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE

# for i in range(6):
#     for j in range(6):
#         print(chr(65+i),end = ' ')
#     print()

# 9. Decreasing number pattern

# 12345
# 1234
# 123
# 12
# 1

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end=' ')
#     print()

# 10. Continuous number triangle

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# temp = 1
# for i in range(1,5):
#     for j in range(i):
#         print(temp,end=' ')
#         temp += 1
#     print()

# 19.Mirrored right triangle

#     *
#    **
#   ***
#  ****
# *****

# n = 5
# for i in range(1,n+1):
#     print(" " * (n-i) + "*" * i)
# print()

# 20.Inverted Right-Aligned Triangle

#  * * * * 
#    * * * 
#      * *
#        *

# n = 4
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" ",end = ' ')
#     # printing the stars

#     for j in range(n+1-i):
#         print("*",end=' ')
#     print()
















































































    