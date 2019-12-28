# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
# print(f)

# # # re-declaring the variable works
# f="abc"
# print(f)

# # # ERROR: variables of different types cannot be combined
# print("this is a string" + str(123))

# Global vs. local variables in functions
def someFunction():
    global f #tells program that we are using f found as a global
    f="def"
    print(f)

print(f) #prints f = 0
someFunction() #changes and prints f
print(f) #prints new value of f

del f #deletes the definition of a variable that was previously declared 
print(f) #f is no longer defined here