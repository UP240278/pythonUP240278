#01 Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count = count + 1
for i in range(11):
    print(i)

#02 Iterate 10 to 0 using for loop, do the same using while loop.
count = 10
while count >= 0:
    print(count)
    count = count - 1
for i in range(10, -1, -1):
    print(i)

#03 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    print('#'*i)

#04 Use nested loops to create the following:
for i in range(0,8):
    print('#  '*8)

#05 Print the following pattern:
for i in range(11):
    print(i, 'x', i, '=', i*i)

#06 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list=['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

#07 Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)

#08 Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 100, 2):
    print(i)