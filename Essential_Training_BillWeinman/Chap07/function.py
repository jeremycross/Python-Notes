#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = 5
    print(id(x))
    kitten(x)
    print(f'in main: x is {x}')
    y = [6]
    print(y)
    kitten(y)
    print(y)



# adding a '=' in the parameter list allows that parameter to have a default value
# if that parameter was not passed in the call it will take on that default
def kitten(a, b = 0, c = 0):
    print('Meow.')
    print(id(a))
    print(a)
    if isinstance(a, list):
        a[0] = 3
    print(b)
    print(c)

# call by value, when you pass a variable to a function, the function operates on a copy
# of that object, it will not change

# when passing an immutable object the id in the method will be the same as the passed value
# this means not really working with a 'copy' of the parameter in this case

# when assingning a mutable you are assinging a reference to the mutable
# its like a pointer, you change info from one ref it will change all of those refs info
# since they all point to the same location

# if you pass the function a mutable object same thing happens, call by reference
# you can change things about that object

if __name__ == '__main__': main()

# __name__ is the name of the current module