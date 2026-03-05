# Python Reference Doc

variable = 'lowercase_snake_case'
CONSTANT = 'UPPERCASE_SCREAMING_SNAKE_CASE'

# single line comment
''' multiline 
comment '''

string = 'string'
integer = 2
floating_point = 3.1415926535
boolean = True
none_type = None

# str(obj)        # Converts object to a string
# int(obj, base)  # Converts object to an integer with the provided `base`
# float(obj)      # Converts object to a floating-point number
# hex(int)        # Converts integer to a hexadecimal string
# oct(int)        # Converts integer to an octal string
# tuple(obj)      # Converts object to a tuple
# list(obj)       # Converts object to a list
# dict(obj)       # Converts object to a dictionary

# Data Types

# 



## Performing operators

""" Math

Addition                +
Subtraction             -
Multiplication          *
Division                /
Modulo                  %
Exponentiation          **
Truncated division      //

"""

# shortcut operators

num = 0

num = num + 1
# can be
num += 1

num = num / 5
# can be
num /= 5

num = num * 3
# can be
num *= 3

# and so on with other operators

# Python does not use ++ or -- like JS does



# STRINGS

my_string = "A double-quoted string"
your_string = 'A single quoted string'
multiline_string = '''This is my string that
                      goes on multiple lines
                      for whatever reason'''
multiline_string = """This is another string that
                      goes on multiple lines
                      for whatever reason"""

# Concatenation

state = "Hawaii"
year = 1959
message = f"{state} joined the U.S. in {year}."
print(message)  # prints: Hawaii joined the U.S. in 1959.

print("this thang".split(" "))
print("this.thang".split("."))  # prints: ['this', 'thang']


# String Methods


# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()  	Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

# Arrays & Iteration Basics
## List Comprehension

# for loop

a=[]
for x in a:
    print (x)

# [ expression for item in iterable if condition ]
# [ EXPRESSION  for  VARIABLE  in  LIST  if CONDITION ]

a = []
[x for x in a if x < 5]

# first x → what you want to put into the new list
# second x → the temporary variable representing each item as you loop
# a → the list you're looping over
# x < 5 → the filter condition

# ex: print the numbers in a that are less than 5.

a = [1, 2, 3, 5, 8, 13, 21, 55]
print([x for x in a if x < 5])

# aka:
for x in a:
    if x < 5:
        print(x)


# List Methods

# append()	    Adds an element at the end of the list              ## modifies actual list (would return: None)
# clear()	    Removes all the elements from the list              ## modifies actual list (would return: None)
# copy()	    Returns a copy of the list                          ## creates new list
# count()	    Returns the number of elements with the specified value     ## does nothing to list
# extend()	    Add the elements of a list (or any iterable), to the end of the current list        ## modifies actual list (would return: None)
# index()	    Returns the index of the first element with the specified value ## does nothing to list
# insert()	    Adds an element at the specified position           ## modifies actual list (would return: None)
# pop()	        Removes the element at the specified position       ## modifies actual list (would return: None)
# remove()	    Removes the item with the specified value           ## modifies actual list (would return: None)
# reverse()	    Reverses the order of the list                      ## modifies actual list (would return: None)
# sort()	    Sorts the list                                      ## modifies actual list (would return: None)


# Sets

# set: a collection of unique values (no duplicates) + order doesn't matter

a_list = [1, 1, 2, 3]
set(a_list)
print(set(a_list))
# => {1, 2, 3}

# convert back into list
print(list(set(a_list)))
# => [1, 2, 3]


# Conditionals / Logic

#   ==          equal to                checks if two things are the same
#   !=          not equal to            checks if two things are different
#   >           greater than            left value bigger than right
#   <           less than               left value smaller than right
#   >=          greater or equal        left >= right
#   <=          less or equal           left <= right

#   and         both must be true       condition1 AND condition2
#   or          one must be true        condition1 OR condition2
#   not         opposite                flips true → false 

#   in          exists in               checks if value is inside list/string/set
#   not in      does not exist in       checks if value NOT inside

# Sets / list comparisons

#   &           intersection            what both sets have in common
#   |           union                   everything from both sets combined
#   -           difference              what's in first set but not second        
