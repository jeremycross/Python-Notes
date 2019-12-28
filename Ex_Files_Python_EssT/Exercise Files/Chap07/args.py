#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')
    x = ('meow', 'grrr', 'purr')
    kitten(*x) # if you have a tuple or a list you can call it with the '*'
    # this passes a reference of that object (list or tuple)


# '*' infront of args symbolizes a variable length argument list
# args is common name for this type of parameter
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
