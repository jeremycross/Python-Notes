#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    def f2():
        print('this is f2')
    return f2
# f2 only exists within the scope of f1

f1() # when we run this nothing really happens since no print statements or assingments occur

x = f1() # when we run this we make x a reference to f2 so now we can call f2 directly using x as the reference

x() # calling f2 via its reference
# f1 can be considered a wrapper for f2

# weird meta stuff with replacing refs and stuff

def f4(f):
    def wrapped():
        print('f4: this is before the function call')
        f()
        print('this is after the function call')
    return wrapped
# f2 only exists within the scope of f1

def f3():
    print('this is f3')

x = f4(f3)
x()

# this creates a refence to wrapped using the variable name x
# this reference kinda saves, f3 as an arg since it was defined like that when it was returned

# decorator of this whole thing is:
print('decorator')
f3 = f4(f3) # this replaces f3 now with def of wrapped()
f3() # calling wrapped via its new reference

# this is self referential and really weird, so here is a diff. way to do this
def f6(f):
    def wrapped():
        print('f6: this is before the function call')
        f()
        print('this is after the function call')
    return wrapped

@f6 # this is a decorator and allows you to accomplish the same thing as what happened with f3 and f4
def f5():
    print('this is f5')


f5() # now when we call this we are calling f6(f5)