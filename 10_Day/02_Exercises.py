#01 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(101):
    sum+=i
print('The sum of all numbers is', sum)

#02 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
evens=0
odds=0
for e in range(0, 101, 2):
    evens+=e
for o in range(1, 100, 2):
    odds+=o
print('The sum of all evens is', evens, '. And the sum of all odds is', odds)