#01 Write a code which gives grade to students according to theirs scores:
score=int(input('Enter your score: '))
if score>=90:
    print('Your grade is A')
elif score>=70 and score<=89:
    print('Your grade is B')
elif score>=60 and score<=69:
    print('Your grade is C')
elif score>=50 and score<=59:
    print('Your grade is D')
else:
    print('Your grade is F')

#02 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or
#November, the season is Autumn. December, January or February, the season is Winter. March, April or May,
#the season is Spring June, July or August, the season is Summer
month=input('Enter the month: ')
autumn=['september', 'october', 'november']
winter=['december', 'january', 'february']
spring=['march', 'april', 'may']
summer=['june', 'july', 'august']
if month in autumn:
    print('The season is Autumn')
elif month in winter:
    print('The season is Winter')
elif month in spring:
    print('The season is Spring')
else:
    print('The season is Summer')

#03 The following list contains some fruits: If a fruit doesn't exist in the list add the fruit to the list
#and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Enter a fruit: ')
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)