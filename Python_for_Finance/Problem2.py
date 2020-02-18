# Write a function that will return the maximum value of two numbers.
# The test program that will access your function could look like this:

# determine max value - using a fall through approach
def maxvalue1(a,b):
    if a > b:
        return a
    return b

# dtermine max value using if - else
def maxvalue2(a,b):
    if a > b:
        return a
    else:
        return b

# determine max value using ternary statement
def maxvalue3(a,b):
    return a if a > b else b

def maxvalue4(a,b):
    return max(a,b)


a=100
b=200

print("The maximum value is: ", maxvalue1(a,b))
print("The maximum value is: ", maxvalue2(a,b))
print("The maximum value is: ", maxvalue3(a,b))
print("The maximum value is: ", maxvalue4(a,b))
