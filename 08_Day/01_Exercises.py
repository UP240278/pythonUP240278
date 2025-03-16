#01 Create an empty dictionary called dog
dog={}

#02 Add name, color, breed, legs, age to the dog dictionary
dog['Name']='Max'
dog['Color']='White'
dog['Breed']='Australian Shepherd'
dog['Legs']=4
dog['Age']=7

#03 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'Gael',
    'last_name':'Rodriguez',
    'gender':'Male',
    'age':19,
    'marital_status':'Single',
    'skills':['teamwork','problem-solving'],
    'country':'Mexico',
    'city':'Aguascalientes',
    'address':'Casasolida'
}

#04 Get the length of the student dictionary
print(len(student))

#05 Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

#06 Modify the skills values by adding one or two skills
student['skills'].append('communication')

#07 Get the dictionary keys as a list
print(student.keys())

#08 Get the dictionary values as a list
print(student.values())

#09 Change the dictionary to a list of tuples using items() method
print(student.items())

#10 Delete one of the items in the dictionary
student.popitem()

#11 Delete one of the dictionaries
del student