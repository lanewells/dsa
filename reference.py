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

# Arrays & Iteration Basics
## List Comprehension

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