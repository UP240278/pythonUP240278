#01 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
#You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age=int(input('Enter your age: '))
if age>=18:
    print('You are old enough to learn to drive.')
else:
    difference=18-age
    print('You need', difference, 'more years to learn to drive.')

#02 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input
#(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year
#difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age=int(input('Enter my age: '))
your_age=int(input('Enter your age: '))
difference=my_age-your_age
if difference==0:
    print('We are the same age')
elif difference>0:
    if difference==1:
        print('I am 1 year older than you')
    else:
        print('I am', difference, 'years older than you')
else:
    if difference==-1:
        print('You are 1 year older than me')
    else:
        print('You are', int(difference/-1), 'years older than me')

#03 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#if a is less b return a is smaller than b, else a is equal to b. Output:
a=int(input('Ingrese un numero: '))
b=int(input('Ingrese un numero: '))
if a>b:
    print(a, 'is greater than', b)
elif a<b:
    print(a, 'is smaller than', b)
else:
    print(a, 'is equal to', b)