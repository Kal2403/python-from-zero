# Exercises: Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
# Find the length of the set it_companies

print(len(it_companies)) # output: 7

# Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies) # output: {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}

# Insert multiple IT companies at once to the set it_companies

it_companies.update(['LinkedIn', 'Netflix', 'Tesla'])
print(it_companies) # output: {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'LinkedIn', 'Netflix', 'Tesla'}

# Remove one of the companies from the set it_companies

it_companies.remove('Google')
print(it_companies) # output: {'Facebook', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'LinkedIn', 'Netflix', 'Tesla'}

# What is the difference between remove and discard

    # Difference between remove and discard
    # remove() gives an error if the item does not exist
    # discard() does not give an error

    # Example:
    # it_companies.remove('Netflix')   # KeyError
    # it_companies.discard('Netflix')  # No error

# Level 2
# Join A and B

print(A.union(B)) # output: {19, 20, 22, 24, 25, 26, 27, 28}

# Find A intersection B

print(A.intersection(B)) # output: {19, 20, 22, 24, 25, 26}

# Is A subset of B

print(A.issubset(B)) # output: True since all items in A are also in B

# Are A and B disjoint sets

print(A.isdisjoint(B)) # output: False since A and B have common items

# Join A with B and B with A

print(A.union(B)) # output: {19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A)) # output: {19, 20, 22, 24, 25, 26, 27, 28}

# What is the symmetric difference between A and B

print(A.symmetric_difference(B)) # output: {27, 28} since these items are in either A or B but not in both

# Delete the sets completely

del A
del B

# Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages_set = set(age)
print("Length of ages list:", len(age))
print("Length of ages set:", len(ages_set))
if len(age) > len(ages_set):
    print("The list has more items than the set.")
else:
    print("The set has more items than the list.")

# Explain the difference between the following data types: string, list, tuple and set

# String: Ordered collection of characters, inmutable.
# List: Ordered collection of items, mutable, allows duplicates.
# Tuple: Ordered collection of items, inmutable, allows duplicates.
# Set: Unordered collection of unique items, mutable, does not allow duplicates.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print("Unique words in the sentence:", unique_words) # output: {'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people.'}
print("Number of unique words:", len(unique_words)) # output: Number of unique words: 10 (Note: 'people.' is considered a unique word due to the period at the end)

# Creating a set

st = set()
print(st) # output: set()

# Creating a set with some values

st2 = {'item1', 'item2', 'item3', 'item4'}
print(st2) # output: {'item1', 'item2', 'item3', 'item4'}

fruits = {'apple', 'banana', 'orange', 'grape'}
print(fruits) # output: {'apple', 'banana', 'orange', 'grape'}

# Getting the length of a set

st3 = {'item1', 'item2', 'item3', 'item4'}
print(len(st3)) # output: 4

grocery_list = {'milk', 'bread', 'eggs', 'cheese'}
print(len(grocery_list)) # output: 4

# Checking if an item is in a set

st4 = {'item1', 'item2', 'item3', 'item4'}
print('Does set st4 contain item3? ', 'item3' in st4) # output: True

grocery_list2 = {'milk', 'bread', 'eggs', 'cheese'}
print('mango' in grocery_list2) # output: False

# Adding an item to a set

st5 = {'item1', 'item2', 'item3'}
st5.add('item4')
print(st5) # output: {'item1', 'item2', 'item3', 'item4'}

fruits2 = {'apple', 'banana', 'orange'}
fruits2.add('lime')
print(fruits2) # output: {'apple', 'banana', 'orange', 'lime'}

# Adding multiple items to a set

st6 = {'item1', 'item2', 'item3'}
st6.update(['item4', 'item5', 'item6'])
print(st6) # output: {'item1', 'item2', 'item3', 'item4', 'item5', 'item6'}

fruits3 = {'apple', 'banana', 'orange'}
vegetables = ('carrot', 'broccoli', 'spinach')
fruits3.update(vegetables)
print(fruits3) # output: {'apple', 'banana', 'orange', 'carrot', 'broccoli', 'spinach'}

# Removing an item from a set

st7 = {'item1', 'item2', 'item3', 'item4'}
st7.remove('item2')
print(st7) # output: {'item1', 'item3', 'item4'}

fruits4 = {'apple', 'banana', 'orange', 'grape'}
fruits4.remove('orange')
print(fruits4) # output: {'apple', 'banana', 'grape'}

# Removing an item with pop()

st8 = {'item1', 'item2', 'item3', 'item4'}
removed_item = st8.pop()
print('Removed item: ', removed_item) # output: Removed item:  item1 (or any other item, since sets are unordered)
print(st8) # output: {'item2', 'item3', 'item4'}

# Clearing a set

st9 = {'item1', 'item2', 'item3', 'item4'}
st9.clear()
print(st9) # output: set()

fruits5 = {'apple', 'banana', 'orange', 'grape'}
fruits5.clear()
print(fruits5) # output: set()

# Deleting a set

st10 = {'item1', 'item2', 'item3', 'item4'}
del st10
# print(st10) # This will raise a NameError since st10 has been deleted

fruits6 = {'apple', 'banana', 'orange', 'grape'}
del fruits6
# print(fruits6) # This will raise a NameError since fruits6 has been deleted

# Converting a list to a set

lst = ['item1', 'item2', 'item3', 'item4']
st11 = set(lst)
print(st11) # output: {'item1', 'item2', 'item3', 'item4'}

grocery_list3 = ['milk', 'bread', 'eggs', 'cheese']
grocery_set = set(grocery_list3)
print(grocery_set) # output: {'milk', 'bread', 'eggs', 'cheese'} 

# Joining Sets (union, update, | operator)

st12 = {'item1', 'item2', 'item3'}
st13 = {'item4', 'item5', 'item6'}
joined_set = st12.union(st13)
print(joined_set) # output: {'item1', 'item2', 'item3', 'item4', 'item5', 'item6'}

fruits7 = {'apple', 'banana', 'orange'}
vegetables2 = {'carrot', 'broccoli', 'spinach'}
food = fruits7.union(vegetables2)
print(food) # output: {'apple', 'banana', 'orange', 'carrot', 'broccoli', 'spinach'}

st14 = {'item1', 'item2', 'item3'}
st15 = {'item4', 'item5', 'item6'}
st14.update(st15)
print(st14) # output: {'item1', 'item2', 'item3', 'item4', 'item5', 'item6'}

fruits8 = {'apple', 'banana', 'orange'}
vegetables3 = {'carrot', 'broccoli', 'spinach'}
food2 = fruits8 | vegetables3
print(food2) # output: {'apple', 'banana', 'orange', 'carrot', 'broccoli', 'spinach'}

# Finding the intersection Items

st16 = {'item1', 'item2', 'item3'}
st17 = {'item2', 'item3', 'item4'}
intersection_set = st16.intersection(st17)
print(intersection_set) # output: {'item2', 'item3'}

fruits9 = {'apple', 'banana', 'orange'}
vegetables4 = {'carrot', 'broccoli', 'spinach'}
intersection_food = fruits9.intersection(vegetables4)
print(intersection_food) # output: set() since there are no common items between fruits and vegetables

python = {'p','y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
intersection_letters = python.intersection(dragon)
print(intersection_letters) # output: {'o', 'n'} since 'o' and 'n' are the common letters in both sets

# Checking if a set is a subset of another set

st18 = {'item1', 'item2', 'item3', 'item4'}
st19 = {'item1', 'item2'}
print(st19.issubset(st18)) # output: True since st19 is a subset of st18

fruits10 = {'apple', 'banana', 'orange'}
citrus_fruits = {'orange'}
print(citrus_fruits.issubset(fruits10)) # output: True since citrus_fruits is a subset of fruits10

# Checking the difference between two sets

st20 = {'item1', 'item2', 'item3', 'item4'}
st21 = {'item3', 'item4', 'item5', 'item6'}
difference_set = st20.difference(st21)
print(difference_set) # output: {'item1', 'item2'} since these items are in st20 but not in st21

python2 = {'p','y', 't', 'h', 'o', 'n'}
dragon2 = {'d', 'r', 'a', 'g', 'o', 'n'}
difference_letters = python2.difference(dragon2)
difference_letters2 = dragon2.difference(python2)
print(difference_letters) # output: {'p', 'y', 't', 'h'} since these letters are in python2 but not in dragon2
print(difference_letters2) # output: {'d', 'r', 'a', 'g'} since these letters are in dragon2 but not in python2

# Finding the symmetric difference between two sets

st22 = {'item1', 'item2', 'item3', 'item4'}
st23 = {'item3', 'item4'}
symmetric_difference_set = st22.symmetric_difference(st23)
print(symmetric_difference_set) # output: {'item1', 'item2'} since these items are in st22 but not in st23

python3 = {'p','y', 't', 'h', 'o', 'n'}
dragon3 = {'d', 'r', 'a', 'g', 'o', 'n'}
symmetric_difference_letters = python3.symmetric_difference(dragon3)
print(symmetric_difference_letters) # output: {'p', 'y', 't', 'h', 'd', 'r', 'a', 'g'} since these letters are in either python3 or dragon3 but not in both

# Joining sets

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # output: True since even_numbers and odd_numbers have no common items

python4 = {'p','y', 't', 'h', 'o', 'n'}
dragon4 = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python4.isdisjoint(dragon4)) # output: False since python4 and dragon4 have common items 'o' and 'n'