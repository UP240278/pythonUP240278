#01 Create an empty tuple
empty_tuple=()

#02 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers=('Leonardo', 'Matías', 'Gael')
sisters=('Gabriela', 'Lucía')

#03 Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sisters

#04 How many siblings do you have?
print('How many siblings do you have?', len(siblings))

#05 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=('Roberto', 'Maria')
family_members=siblings+parents
print(family_members)