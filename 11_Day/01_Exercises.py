#01 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

#02 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    PI = 3.14
    area = PI * r * r
    return area
print(area_of_circle(10))

#03 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num 
    return total  
print(add_all_nums(2, 3, 5)) 

#04 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
#Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(convert_celsius_to_fahrenheit(15))

#05 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    autumn=['september', 'october', 'november']
    winter=['december', 'january', 'february']
    spring=['march', 'april', 'may']
    if month in autumn:
        return 'Autumn'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    else:
        return 'Summer'
print(check_season('june'))

#06 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print(calculate_slope(2, 4, 7, 5))

#07 Quadratic equation is calculated as follows: ax² + bx + c = 0.
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    disc=(b**2)-(4*a*c)
    x1=(-b+(disc**0.5))/(2*a)
    x2=(-b-(disc**0.5))/(2*a)
    return x1, x2
print(solve_quadratic_eqn(1, 6, 9))

#08 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for item in list:
        print(item)
fruits=['banana', 'orange', 'mango', 'lemon']
print(print_list(fruits))

#09 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reverse_array=[]
    for item in array:
        reverse_array.insert(0, item)
    return reverse_array
print(reverse_list(fruits))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    for item in list:
        list[list.index(item)]=item.capitalize()
    return list
print(capitalize_list_items(fruits))

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list
print(add_item(fruits, 'Apple'))

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    list.remove(item)
    return list
print(remove_item(fruits, 'Apple'))

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(numbers):
    sum=0
    for i in range(numbers+1):
        sum+=i
    return sum
print(sum_of_numbers(5))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(numbers):
    odds=0
    for i in range(numbers+1):
        if i%2==1:
            odds+=i
    return odds
print(sum_of_odds(10))

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(numbers):
    even=0
    for i in range(numbers+1):
        if i%2==0:
            even+=i
    return even
print(sum_of_even(10))