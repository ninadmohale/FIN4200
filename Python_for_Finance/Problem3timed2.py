# Write a program that will sum up numbers between 1 and 100 and print the answer.
# Please use some form of loop (iteration) to complete this assignment.
# Remember there is more than one way of iterating in Python. There is the for statement and the while statement.

# pip install ttictoc

from ttictoc import TicToc

def sum1(a):
    t=0
    for x in range(a+1):
        t+=x
    return(t)

def sum2(a):
    t=0
    i=1
    while i <= a:
        t=t+i
        i=i+1
    return(t)

def sum3(a):
    t=0
    i=1
    while 1:
        t+=i
        i+=1
        if i > a:
            break
    return(t)

def sum4(a):
    return(sum(range(a+1)))

for test_value in [100,500,1000,5000]:
    print("Summation test value: ",test_value)
    with TicToc("sum1"):
        sum1(test_value)
    with TicToc("sum2"):
        sum2(test_value)
    with TicToc("sum3"):
        sum3(test_value)
    with TicToc("sum4"):
        sum4(test_value)
