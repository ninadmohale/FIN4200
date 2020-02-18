# Write a program that will sum up numbers between 1 and 100 and print the answer.
# Please use some form of loop (iteration) to complete this assignment.
# Remember there is more than one way of iterating in Python. There is the for statement and the while statement.

# pip install ttictoc

from ttictoc import TicToc

def sum1(a,b):
    t=0
    for x in range(a,b+1):
        t+=x
    return(t)

def sum2(a,b):
    t=0
    i=a
    while i <= b:
        t=t+i
        i=i+1
    return(t)

def sum3(a,b):
    t=0
    i=a
    while 1:
        t+=i
        i+=1
        if i > b:
            break
    return(t)

def sum4(a,b):
    return(sum(range(a,b+1)))


with TicToc("sum1"):
    print(sum1(25,200))    
with TicToc("sum2"):
    print(sum2(25,200))
with TicToc("sum3"):
    print(sum3(25,200))
with TicToc("sum4"):
    print(sum4(25,200))
