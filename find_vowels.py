"""
Write a python script to find number of vowels in each of the string in a given
list of Strings. Use map function.
"""

# defining a function to find vowels in a string 
def find_vowels(string):
    count = 0
    # finding number of vowels in string
    for e in string:
        if e in "aeiouAEIOU":
            count += 1
    
    # returning count of vowels
    return count
            

# creating a list of strings
string_list = ["Onkar", "Raj", "Yogesh", "Nikhilkumar", "Rohan", "Akshay", "Vijay",]

# finding number of vowels using map() function
# Syntax - map(function, iterable)
list_of_vowels = map(find_vowels, string_list)

# printing list of vowels
i = 1
for e in list_of_vowels:
    print("String %d :" %(i), e)
    i += 1