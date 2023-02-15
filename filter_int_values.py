"""
Write a python script to filter only int type values in a given list of elements.
Use filter function
"""

# defining a function filter_int() which filter's int values only 
def filter_int(number):
    if type(number) == int:
        return number

# creating a list elements with different types
elements = [123, 13.33, True, 4+2J, 'Z', 'a', "Onkar", 890, 433, 56.675, 33.33, 223, 890, 100, 90]

# filtering int values using filter function
int_values = filter(filter_int, elements)

# printing int_values
for e in int_values:
    print(e, end=' ')

