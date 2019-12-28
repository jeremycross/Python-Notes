#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n = 1):
    print(n)

def multiply_by_2(n = 1):
    print(n)
    return n * 2

function()
# if you do not pass it a value n takes on the value 1
# otherwise it takes on the passed value
x = multiply_by_2(12)

print(x) # python functions return something, this case it returns 'None'
