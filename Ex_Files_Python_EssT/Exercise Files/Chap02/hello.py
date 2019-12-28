#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
print('Hello, World. %d' % x) #you can use ''' for strings for '"' for strings, either works
# above line is legacy from python 2 and is deprecated
print('Hello, world. {}'.format(x))
# format is a function of the string object
print(f'Hello, world. {x}') # f-string here call format function
