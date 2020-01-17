#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 82
y = 73

if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
else:
    print('x >= y')
# print('z is {}'.format(z)) #blocks do not define scope
# you can still print z here even though it was defined in the if block
# functions, objects and modules define scope
