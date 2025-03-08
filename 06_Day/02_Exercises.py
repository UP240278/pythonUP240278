#01 Unpack siblings and parents from family_members
family_members=('Leonardo', 'Matías', 'Gael', 'Gabriela', 'Lucía', 'Roberto', 'Maria')
familia=list(family_members)
siblings=familia[:5]
parents=familia[5:]

#02 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Orange', 'Watermelon', 'Apple', 'Lemon')
vegetables=('Carrot', 'Onion', 'Potato', 'Lettuce')
animal_products=('Milk', 'Fish', 'Eggs', 'Beef Steak')
food_stuff_tp=fruits+vegetables+animal_products

#03 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)

#04 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items=food_stuff_lt[int(len(food_stuff_lt)/2-1):int(len(food_stuff_lt)/2+1)]
print(middle_items)

#05 Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[:3]+food_stuff_tp[-3:])

#06 Delete the food_staff_tp tuple completely
del food_stuff_tp

#07 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#7.1 Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#7.2 Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)