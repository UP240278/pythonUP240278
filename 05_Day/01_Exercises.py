#01 Declare an empty list
lista=list()

#02 Declare a list with more than 5 items
items=[1, 2, 3, 4, 5, 6, 7]

#03 Find the length of your list
print(len(items))

#04 Get the first item, the middle item and the last item of the list
print(items[0], items[3], items[6])

#05 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Gael', 19, 78, 'single', 'casasolida']

#06 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#07 Print the list using print()
print(it_companies)

#08 Print the number of companies in the list
print(len(it_companies))

#09 Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[6])

#10 Print the list after modifying one of the companies
it_companies[0]='Instagram'
print(it_companies)

#11 Add an IT company to it_companies
it_companies.append('Intel')

#12 Insert an IT company in the middle of the companies list
it_companies.insert(3, 'OpenAI')

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2].upper()

#14 Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

#15 Check if a certain company exists in the it_companies list.
print(it_companies.index('IBM'))

#16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18 Slice out the first 3 companies from the list
print(it_companies[3:])

#19 Slice out the last 3 companies from the list
print(it_companies[:6])

#20 Slice out the middle IT company or companies from the list
print(it_companies[:4]+it_companies[5:])

#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22 Remove the middle IT company or companies from the list
it_companies.pop(3)
it_companies.pop(3)
print(it_companies)

#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24 Remove all IT companies from the list
del it_companies[:]
print(it_companies)

#25 Destroy the IT companies list
del it_companies

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)