# Write a program that will sum up numbers between 1 and 100 and print the answer.
# Please use some form of loop (iteration) to complete this assignment.
# Remember there is more than one way of iterating in Python. There is the for statement and the while statement.

t=0
for x in range(101):
    if not(x % 2):
        t+=x
print(x)
print(t)

t=0
for x in range(2,101,2):
    t+=x
print(x)
print(t)

t=0
i=2
while i <= 100:
    t+=i
    i+=2
print(x)
print(t)

t=0
i=2
while True:
    t+=i
    i+=2
    if i > 100:
        break
print(x)
print(t)

print(sum(range(2,101,2)))
