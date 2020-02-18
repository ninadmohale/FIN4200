# Write a program that will sum up numbers between 1 and 100 and print the answer.
# Please use some form of loop (iteration) to complete this assignment.
# Remember there is more than one way of iterating in Python. There is the for statement and the while statement.

t=0
for x in range(101):
    t+=x
print(x)
print(t)

t=0
i=1
while i <= 100:
    t=t+i
    i=i+1
print(x)
print(t)

t=0
i=1
while 1:
    t=t+i
    i+=1
    if i > 100:
        break
print(x)
print(t)

print(sum(range(101)))
