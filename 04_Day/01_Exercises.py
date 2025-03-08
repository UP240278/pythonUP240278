#01 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1='Thirty'
string2='Days'
string3='Of'
string4='Python'
space=' '
cadenaCompleta=string1+space+string2+space+string3+space+string4
print(cadenaCompleta)

#02 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1='Coding'
string2='For'
string3='All'
space=' '
cadenaCompleta=string1+space+string2+space+string3
print(cadenaCompleta)

#03 Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"

#04 Print the variable company using print().
print(company)

#05 Print the length of the company string using len() method and print().
print(len(company))

#06 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#07 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#08 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize().title().swapcase())

#09 Cut(slice) out the first word of Coding For All string.
print(company[6:])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
cadena='Python for Everyone'
print(cadena.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
redes="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(redes.split(','))

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(company[13])

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'. 
print(cadena[0], cadena[7], cadena[11])

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
cadenaAll='Coding For All'
print(cadenaAll[0], cadenaAll[7], cadenaAll[11])

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(cadenaAll.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(cadenaAll.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
cadenaAll='Coding For All People'
print(cadenaAll.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because',''))

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because',''))

#28 Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.}
spaces='   Coding For All      '
print(spaces.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
oracion1='30DaysOfPython'
oracion2='thirty_days_of_python'
if oracion1.isidentifier()==True:
    print(oracion1)
else:
    print(oracion2)

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
librerias=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(librerias))

#33 Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

#34 Use a tab escape sequence to write the following lines.
print('\tName      \tAge     \tCountry   \tCity\n\tAsabeneh  \t250     \tFinland   \tHelsinki')

#35 Use the string formatting method to display the following: area de círculo de radio 10
radio=10
area=3.14*radio**2
print('The area of a circle with radius {} is {} meters square.'.format(radio, area))

#36 Make the following using string formatting methods:
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))