# Recursion : its a process in which the function calls itself until the conditions not made
# def func()
#   base conditional /case
#   recursion calls
# func()

def greet(n):
  # base case
  if n == 0:
    return
  print('hello')
  # recursion call
  greet(n-1)
greet(5)

# increment method
def greet(n):
  # base case
  if n == 6:
    return
  print('hello')
  # recursion call
  greet(n+1)
greet(1)

#  print the numbers from 1 to 10 using the recursion
def print_numbers(n):
    if n == 11:
      return
    print(n)
    print_numbers(n + 1)

print_numbers(1)

#  print the numbers from 10 to 1 using the recursion
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(10)

#  write a program to ptint the sum of the 1 to 10 using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(10))
# recursion work on lifo concept = last in first out

# print the factorial using the recursion ->5
def sum_numbers(n):
    if n == 1:
        return 1
    return n * sum_numbers(n - 1)

print(sum_numbers(5))

# print the fibbonacci sequence using recursion ->
def fibbonacci(n):
  if n == 0:
    return 0
  elif n==1:
      return 1
  else:
      return fibbonacci(n-1) + fibbonacci(n-2)

print(fibbonacci(10))

# print the power of a given (number,power)
def power(n,p):
  if p == 0:
    return 1
  else:
    return n * power(n,p-1)

print(power(2,3))

# count the digits of number 123 using recursion
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(123))

# print the sum of all the digits of a number using recursion
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))
