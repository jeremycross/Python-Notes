#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import Decimal

#### string types ####
x = 'seven {} {}'.format(8, 9)
y = '''

hello

''' # using triple quotes for mutli-line strings!!
z = '"{:>5}"'.format(6) # algn value in format to take on 5 characters total in string
print('x is "{}"'.format(x))
print(type(x))
print(f'y is "{y}"')
# duck typing, dynamic typing, if it walks like a duck its a duck
# all types are classes in python 3, even int and string
# no difference between single and double quotes

# we can use numbers in a formatting string so that we can adjust which argument goes where
# x = '{1} {0}'.format(8, 9) => turns into => '9 8' as a string

# we can use ':' inside {} with < for left align of spaces and > for right align of spaces when formatting
print('start {:>10} end'.format(z))
print('start {:>9} end'.format(7))

# leading zeroes
print('{:>04}'.format(12)) # 4 spaces for the whole number

# trailing zeroes
print('{:<04}'.format(13)) # 4 spaces for the whole number

# instead of using the .format(...) we can use an 'f' string
a = f'five {x}' # put variable in the curly braces to add it to the string format
print(a)
######################

### numerics ###
x = 7 * 3.14159 # turns x to a float because of using a float in calc
print(x)
x = 7.0 # float
print(x)
x = 7 # int
print(x)

# diving two ints = a float
x = 7/3 # float
print(x)

# weird issue with floats
x = .1 + .1 + .1 - .3
print(x) # should print a 0 but its actually a very small value

# handling money so that we can us floats properly with a work around
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print(x) # this is now zero!

### Bool type ###
x = False
print(x)
print(type(x))
x = 7 > 5
print(x)
print(type(x))

x = None # None is basically a no value for python
if x:
    print("True")
else:
    print("False")
# x = None evaluates as false
# x = 0 also evaluates to false
# x = '' also evaluates to false, empty string
# x = 'h' evaluates as true
# x = 1 evaluates as true
# if a basic type is evaluated as bool it will be considered false if it is nothing or 0 in value
# other wise it will evaluate as true
x = 12
if x:
    print("True")
else:
    print("False")

# creating a mix type tuple
x = (1 , 'two', 3.0, [4, 'four'], 5 )
y = (1 , 'two', 3.0, [4, 'four'], 5 )
print(x)
print(type(x))

print(type(x[0])) # type int
print(type(x[1])) # str
print(type(x[2])) # float
print(x[3]) # [4, 'four'], this is a list with two items, 4 and string 'four'
print(x[3][0]) # this is the int = 4
print(x[3][1]) # this is the string = 'four'

# id function - prints a unique number for two tuples
print(id(x))
print(id(y))

# these two are equal value int so they will print the same id number
# we don't need to make multple '1' objects
print(id(x[0])) 
print(id(y[0]))

if x[0] is y[0]: # checks if they are the exact same object
    print('yep')
else:
    print('nope')

if isinstance(x, tuple):
    print('yep')
else:
    print('nope')

if(type(x) == type(y)):
    print('yeah')

if(x == y):
    print('yo')

# if these tuples did not have lists in them they would be the same object and have the same id
