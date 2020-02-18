# Write a program that will sum up numbers between 1 and 100 and print the answer.
# Please use some form of loop (iteration) to complete this assignment.
# Remember there is more than one way of iterating in Python. There is the for statement and the while statement.

# pip install ttictoc

from ttictoc import TicToc

def sum1():
    t=0
    for x in range(101):
        t+=x
    return(t)

def sum2():
    t=0
    i=1
    while i <= 100:
        t=t+i
        i=i+1
    return(t)

def sum3():
    t=0
    i=1
    while 1:
        t+=i
        i+=1
        if i > 100:
            break
    return(t)

def sum4():
    return(sum(range(101)))

with TicToc("sum1"):
    sum1()

with TicToc("sum2"):
    sum2()

with TicToc("sum3"):
    sum3()

with TicToc("sum4"):
    sum4()
