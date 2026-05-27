# Exercises: Level 1

# Create an empty tuple

tuple_empty = ()
tuple_empty2 = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

names_siblings = ('Pedro', 'Liz', 'Caro', 'Kal')
print(names_siblings)

# Join brothers and sisters tuples and assign it to siblings

sisters = ('Caro', 'Kim')
brothers = ('Pedro', 'Kal')
siblings = sisters + brothers
print(siblings)

# How many siblings do you have?

print(len(siblings)) # 4

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = list(siblings)
family_members.append('Maria')
family_members.append('Pedrote')
tuple(family_members)
print(family_members)

# Exercises: Level 2

# Unpack siblings and parents from family_members

family_members2 = ('Pedro', 'Kal', 'Caro', 'Kim', 'Maria', 'Pedrote')
brother1, brother2, sister1, sister2, mother, father = family_members2

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apple', 'orange', 'banana')
vegetables = ('onion', 'carrot', 'potato')
animal_products = ('milk', 'cheese', 'butter')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_item = len(food_stuff_lt) // 2 + 1
print(food_stuff_lt[middle_item])

# Slice out the first three items and the last three items from food_stuff_lt list

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

print('First three:', first_three_items)
print('Last three', last_three_items)

# Delete the food_stuff_tp tuple completely

del food_stuff_tp

# Check if 'Iceland' is a nordic country nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Creating a tuple

empty_tuple = ()
empty_tuple2 = tuple()

# Tuple with values

tpl = ('item1', 'item2', 'item3')

fruits = ('banana', 'apple', 'mango', 'orange')

# Tuple length

tpl2 = ('item1', 'item2', 'item3', 'item4')
print(len(tpl2))  # Output: 4

# Accessing tuple items

# ('banana', 'apple', 'mango', 'orange')
#     0         1        2        3

print(fruits[0])  # Output: 'banana'
print(fruits[1])  # Output: 'apple'
print(fruits[2])  # Output: 'mango'
print(fruits[3])  # Output: 'orange'

# Negative indexing

   # ('banana', 'apple', 'mango', 'orange')
   #    -4        -3       -2       -1

print(fruits[-1])  # Output: 'orange'
print(fruits[-2])  # Output: 'mango'
print(fruits[-3])  # Output: 'apple'
print(fruits[-4])  # Output: 'banana'

# Slicing tuples

tpl3 = ('item1', 'item2', 'item3', 'item4', 'item5')

print(tpl3[0:5])  # Output: ('item1', 'item2', 'item3', 'item4', 'item5') ALL ITEMS
print(tpl3[0:]) # Output: ('item1', 'item2', 'item3', 'item4', 'item5') ALL ITEMS
print(tpl3[1:3])  # Output: ('item2', 'item3') middle items does not include the index 3

# Range of negative indexes

print(tpl3[-5:])  # Output: ('item1', 'item2', 'item3', 'item4', 'item5') ALL ITEMS
print(tpl3[-5:-1])  # Output: ('item1', 'item2', 'item3', 'item4') middle items does not include the index -1

# Changing tuple to a list

tpl4 = ('item1', 'item2', 'item3')
tpl4_list = list(tpl4)
print(tpl4_list)  # Output: ['item1', 'item2', 'item3']

tpl4_list[0] = 'new_item1'
print(tpl4_list)  # Output: ['new_item1', 'item2', 'item3']

# Checking if an item exists in a tuple

print('item2' in tpl4)  # Output: True
print('item4' in tpl4)  # Output: False

# Joining tuples

tpl5 = ('item1', 'item2')
tpl6 = ('item3', 'item4')
joined_tpl = tpl5 + tpl6
print(joined_tpl)  # Output: ('item1', 'item2', 'item3', 'item4')

# Deleting a tuple

tpl7 = ('item1', 'item2', 'item3')
del tpl7
print(tpl7)  # This will raise a NameError because the tuple no longer exists