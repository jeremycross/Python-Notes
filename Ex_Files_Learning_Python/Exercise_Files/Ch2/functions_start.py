#
# Example file for working with functions
#

# define a basic function
def func1(): #def to define func1 ':' to show start of scope block
    print("i am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)
    #print(str(arg1) + "\t" + str(arg2))

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1): #second parameter is 1 unless specified as a different value
    result = 1
    for i in range(x):
        print(i)
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args): #'*' allows for a variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print (func1()) #executes func1 and then prints 'return value' which is 'None'
print (func1) #print value of func1 definition
func2(10,20)
print (func2(10, 20))
print (cube(3))
print (power(2))
print (power(2,3))
print (power(x=2, num=3))
print (multi_add(10, 4, 5, 10, 4)) #can use any number of parameters