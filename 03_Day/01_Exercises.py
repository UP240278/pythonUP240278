#01 Declare your age as integer variable
edad=19

#02 Declare your height as a float variable
peso=78.5

#03 Declare a variable that store a complex number
complex=2+1j

#04 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=int(input('Ingrese la base del triángulo: '))
height=int(input('Ingrese la altura del triángulo: '))
area=0.5*base*height
print('El área del triángulo es: ', area)

#05 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA=int(input('Ingrese el lado a del triángulo: '))
sideB=int(input('Ingrese el lado b del triángulo: '))
sideC=int(input('Ingrese el lado c del triángulo: '))
perimeter=sideA+sideB+sideC
print('El perimetro del triángulo es: ', perimeter)

#06 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
baseR=int(input('Ingrese la base del rectángulo: '))
alturaR=int(input('Ingrese la altura del rectángulo: '))
areaR=baseR*alturaR
perimetroR=2*(baseR+alturaR)
print('El área del rectángulo es: ', areaR)
print('El perimetro del rectángulo es: ', perimetroR)

#07 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radioC=int(input('Ingrese el radio del círculo: '))
pi=3.14
areaC=pi*(radioC**2)
circunferenciaC=2*pi*radioC
print('El área del círculo es: ', areaC)
print('La circunferencia del circulo es: ', circunferenciaC)

#08 Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1, x2=0, 1
y1=(2*x1)-2
y2=(2*x2)-2
m=(y2-y1)/(x2-x1)
xIntercept=(y2+2)/2
yIntercept=y1
print('La pendiente de la recta es: ',m)
print('La intersección en el eje x es: ',xIntercept)
print('La intersección en el eje y es: ', yIntercept)

#09 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2=2, 6
y1, y2=2, 10
slope=(y2-y1)/(x2-x1)
euclideanDistance=((x2-x1)**2+(y2-y1)**2)**0.5
print('La pendiente de la recta es: ', slope)
print('La distancia entre los puntos dados es: ', euclideanDistance)

#10 Compare the slopes in tasks 8 and 9.
if m==slope:
    print('Las pendientes son iguales.')
else:
    print('Las pendientes son diferentes.')

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x=int(input('Ingrese el valor de x: '))
y= x**2 + 6*x + 9
if y==0:
    print('y vale 0 cuando x vale:', x)
else:
    print('cuando x vale', x, 'y no vale 0')

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
bool=len('python')!=len('dragon')
print('¿La longitud de "python" y "dragon" es diferente?', bool )

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
on= 'on' in 'python' and 'on' in 'dragon'
print('¿Está "on" en "python" y en "dragon"?', on)

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jargon= 'jargon' in ' I hope this course is not full of jargon'
print('¿Está "jargon" en la oración " I hope this course is not full of jargon"?', jargon)

#15 There is no 'on' in both dragon and python
notOn= 'on' not in 'dragon' and 'on' not in 'python'
print('¿No está "on" en "dragon" y en "python"?', notOn)

#16 Find the length of the text python and convert the value to float and convert it to string
entero=len('python')
flotante=float(entero)
texto=str(flotante)
print(entero, flotante, texto)

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numero=int(input('Ingresa un número: '))
if numero%2==0:
    print('El número', numero, 'es par.')
else:
    print('El número', numero, 'no es par.')

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floorDivision=7//3
result=int(2.7)
print('¿La división entera de 7//3 es igual al valor entero de 2.7?', floorDivision==result)

#19 Check if type of '10' is equal to type of 10
print('¿El tipo de "10" es igual al tipo de 10?', type('10')==type(10))

#20 Check if int('9.8') is equal to 10
print('¿El entero de "9.8" es igual a 10?', int(float('9.8'))==10)

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
horas=int(input("Ingrese la cantidad de horas trabajadas: "))
pago=int(input('Ingrese el pago por hora:'))
salario=horas*pago
print('Su salario es de: $', salario)

#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years=int(input('Ingrese la cantidad de años: '))
secPorHora=3600
horasAnuales=24*365
secVividos=years*horasAnuales*secPorHora
print('Una persona que viva', years, 'años puede vivir', secVividos, 'segundos.')

#23 Write a Python script that displays the following table
filas = 5
for num in range(1, filas+1):
    print(num, 1, num, num**2, num**3)