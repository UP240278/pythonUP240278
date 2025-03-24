from collections import Counter
#01 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    odds=0
    evens=0
    for i in range(num+1):
        if i%2==1:
            odds+=1
        else:
            evens+=1
    return odds, evens
print(evens_and_odds(10))

#02 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    factorial=1
    for i in range(1, num+1):
        factorial*=i
    return factorial
print(factorial(5))

#03 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(parameter):
    if len(parameter)==0:
        return 'Is empty'
    else:
        return 'Is not empty'
list=[]
print(is_empty(list))

#04 Write different functions which take lists. They should calculate_mean, calculate_median, 
#calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
grades=[5, 9, 9, 7, 9, 7, 10]
def calculate_mean(list):
    sum=0
    for i in list:
        sum+=i
    mean=sum/len(list)
    return mean
print('Mean:', round(calculate_mean(grades), 2))

def calculate_median(list):
    list.sort()
    median=list[int(len(list)/2+1)]
    return median
print('Median:', calculate_median(grades))

def calculate_mode(list):
    cout=Counter(list)
    mode=cout.most_common(1)
    mode=mode[0]
    mode=mode[0]
    return mode
print('Mode:', calculate_mode(grades))

def calculate_range(list):
    list.sort()
    range=list[-1]-list[0]
    return range
print('Range:', calculate_range(grades))

def calculate_variance(list):
    sum=0
    for i in list:
        sum+=i
    mean=sum/len(list)
    n=[]
    for i in list:
        n.append((i-mean)**2)
    sum_n=0
    for i in n:
        sum_n+=i
    return sum_n/len(list)
print('Variance:', round(calculate_variance(grades), 2))

def calculate_std(list):
    sum=0
    for i in list:
        sum+=i
    mean=sum/len(list)
    n=[]
    for i in list:
        n.append((i-mean)**2)
    sum_n=0
    for i in n:
        sum_n+=i
    variance=round(sum_n/len(list), 2)
    return variance*0.5
print('Standard deviation:', calculate_std(grades))