#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
x[2] = 10 # a list is mutable and you can change a specific value in it
# its an array
for i in x:
    print('i is {}'.format(i))

x = ( 1, 2, 3, 4, 5 ) # tuple, immutable version of a list
# x [2] = 10 # gives an error, because immutable
print(type(x))
for i in x:
    print('i is {}'.format(i))

x = range(5) # generate a range, also immutable
print(type(x))
for i in x:
    print('i is {}'.format(i))

x = list(range(5)) # generate a list based on the range
x[2] = 30 # mutable
print(type(x))
for i in x:
    print('i is {}'.format(i))

x = range(4, 10) # generate range starting at 4 ending at 9 up by 1 each item
print(type(x))
for i in x:
    print('i is {}'.format(i))

x = range(5, 50, 5) # generate range starting at 5 upping by 5 each time ending at 45
print(type(x))
for i in x:
    print('i is {}'.format(i))

# creating a dictionary
x = { 'one' : 1, 'two' : 2, 'three' : 3, 'four': 4, 'five' : 5}
for i in x:
    print('i is {}'.format(i))

for k, v in x.items():
    print(f'key: {k}, value: {v}')

x['three'] = 42 # at key 'three' set value to 42

for k, v in x.items():
    print(f'key: {k}, value: {v}')

# key and value can be any type
