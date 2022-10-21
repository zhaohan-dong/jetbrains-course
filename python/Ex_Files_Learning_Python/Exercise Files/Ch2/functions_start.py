#
# Example file for working with functions
#

# define a basic function

def function():
    print("I am a function")

# function that takes arguments

def func2(t, j):
    print(str(t) + " " + str(j))

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments

def multi_add(*y):
    result = 0
    for x in y:
        result = result + x
    return result



function()
print(function())
print(function)
func2(10,20)
print(func2(10,20))
print(cube(3))

print(power(2))
print(power(2,3))
print(power(x=3, num=2))


print (multi_add(1,3,4,7))