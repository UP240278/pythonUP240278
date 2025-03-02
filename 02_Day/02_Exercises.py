#01 Check the data type of all your variables using type() built-in function
nombre="Gael"
apellido="Rodríguez"
nombreCompleto=nombre+" "+apellido
pais="México"
ciudad="Aguascalientes"
edad=19
año=2025
is_married=False
is_true=True
is_light_on=False
num1, num2= 1, 3
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#02 Using the len() built-in function, find the length of your first name
print(len(nombre))
#03 Compare the length of your first name and your last name
print(len(apellido))
#04 Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4
#05 Add num_one and num_two and assign the value to a variable total
total=num_one+num_two
#06 Subtract num_two from num_one and assign the value to a variable diff
diff=num_one-num_two
#07 Multiply num_two and num_one and assign the value to a variable product
producto=num_two*num_one
#08 Divide num_one by num_two and assign the value to a variable division
division=num_one/num_two
#09 Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder=num_two%num_one
#10 Calculate num_one to the power of num_two and assign the value to a variable exp
exp=num_one**num_two
#11 Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division=num_one//num_two
#12.1 Calculate the area of a circle and assign the value to a variable name of area_of_circle
radio=30
area_del_circulo=3.14*(radio**2)
#12.2 Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circunferencia_del_circulo=3.14*(2*radio)
#12.3 Take radius as user input and calculate the area.
nuevo_radio=input("Ingrese el radio del circulo: ")
area=3.14*(int(nuevo_radio)**2)
#13 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
nombreUser=input("Ingrese su nombre: ")
apellidoUser=input("Ingrese su apellido: ")
paisUser=input("Ingrese su país: ")
edadUser=input("Ingrese su edad: ")
#14 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords