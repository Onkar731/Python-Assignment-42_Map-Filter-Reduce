"""
Write a python function to calculate HCF(Highest Common Factor) of a list of numbers.
Use reduce function
"""
from functools import reduce 

# defining a function hcf() which returns hcf of two numbers
def hcf(num1, num2):
    if num1<num2:
        smallest = num1
    else:
        smallest = num2
        
    while smallest >= 1:
        if num1%smallest == 0 and num2%smallest == 0:
            gcd = smallest
            break
        smallest -= 1
    
    return smallest

# printing hcf of list of number using reduce() 
print(reduce(hcf, [54,12,24,300,400]))
