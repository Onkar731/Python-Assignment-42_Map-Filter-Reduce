"""
Write a python script to create a list of numbers greater than a given number N
(take from user) for each element in a given set of numbers.
Use filter function.
"""

# defining a function find_greater() which takes a set as an argument 
# and returns a greater number
N = int(input("Enter a number : "))

def find_greater(number):
    if number > N:
        return number

s1 = {1,2,3,4,5,6,7,8,9,10,11,121,123,453,765,78,954,9089,345,111,3,112,443,212,321,44,1432,}
x = list(filter(find_greater, s1))

for e in x:
    print(e, end=' ')