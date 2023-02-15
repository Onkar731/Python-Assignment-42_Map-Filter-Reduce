"""
Write a python script to find number of digits in each of the element in a
given tuple of numbers. Use map function.
"""

# defining a function find_digits() which takes a tuple as an argument
# and returns number of digits
def find_digits(number):
    digits = 0
    
    # finding number of digits
    while number != 0:
        digits += 1
        number //= 10
        
    # returning number of digits
    return digits


# creating a tuple of numbers
number_tuple = (12,345,6, 4554, 345678, 34504, 7890, 3455, 2344135643, 34677, 2093,)

# finding number of digits using map() function
digits = map(find_digits, number_tuple)

# printing number of digits
for e in digits:
    print(e)