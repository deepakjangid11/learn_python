# SET DATATYPE :- set is a datatype in Python that represents an 
# unordered collection of unique elements. Sets are mutable, meaning you can add 
# or remove elements after the set has been created. They are commonly used for
#  membership testing, removing duplicates from a sequence, and performing mathematical
#  set operations like union, intersection, and difference.

# set is unordfered collection of unique elements

# example 
# s1 = {} if you check the type of s1 it will be dictionary
s1 = set()  # correct way to create an empty set
print(type(s1))  # <class 'set'>

# if you want to create a empty set. then you have to use set() function
# the set stores the unique elements 
s2 = {1, 2, 3, 4, 5, 1, 2}
print(s2)  # output will be {1, 2, 3, 4, 5} duplicate values will be removed

li = [1,2,3,4,5,4,3,3,2]
s3 = set(li)
print(s3)  # output will be {1, 2, 3, 4, 5} duplicate values will be removed

# UNORDERED collection means the items stored in set are not in any particular order    
s = {1,2,3,4,5}
s[0] # this will give error because set is unordered collection

s = {1,2,3,4,5,5,7}
for i in s:
    print(i) # output will be 1 2 3 4 5 7 order may vary

# how to add elements in set
s = {1,2,3,}
s.add(4) # this will add 4 in set s

# update() function is used to add multiple elements in set
s.update([5,6,7]) # this will add 5,6,7 in set s
# update method is used to add multipule elements into existing set

# write a program to create a set using list of the elemenets
li = [1,2,3,4,5,5,4,3,2,1]
st = set(li)
print(st) 

# write a take 5 input from user and add the each element into the set
user = set()
for i in range(5):
    ele = int(input("enter the element: "))
    user.add(ele)
    print(user)

# remove() function is used to remove an element from the set
s = {1,2,3,4,5}
s.remove(3) # this will remove 3 from the set s

# DISCARD() function is used to remove the perticular element from
#  the set if the element is present into the set 
# then it will remove otherwise it will not give error
s = {1,2,3,4,5}
s.discard(6) # this will not give error because 6 is not present in the set s

# POP() function is used to remove and return an arbitrary element from the set
# pop method is used to remove any random element from the set and return that elements
s = {1,2,3,4,5}
print(s.pop()) # this will remove and return an arbitrary element from the set s

