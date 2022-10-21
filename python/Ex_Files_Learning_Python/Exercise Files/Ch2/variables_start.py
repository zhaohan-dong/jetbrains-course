# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# # re-declaring the variable works

#f="blah"
#print(f)

# # ERROR: variables of different types cannot be combined

print("this is a string" + str(123) + str(f))

# Global vs. local variables in functions


def someFunction():
    global f
    f="local"
    print(f)

someFunction()
print(f)
