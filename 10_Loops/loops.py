# 1. Iterate 0 to 10 using for loop, do the same using while loop.

for number in range(11):
    print(number) # output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

count = 0
while count < 11:
    print(count)
    count += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(11, -1, -1):
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######

for hash in range(8):
    print('#' * hash)

# 4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for hash in range(9):
    print('# ' * 8)

# 5. Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for hash in range(11):
    print(hash, 'x', hash, '=', hash * hash)

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list_skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in list_skills:
    print(skill)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

for number in range(101):
    if number % 2 == 0:
        print(number)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for number in range(101):
    if number % 2 == 1:
        print(number)

# Exercises level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050.

numbers = list(range(101))
total = sum(numbers)
print(total)

total1 = 0

for number in range(101):
    total1 += number

print(total1)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. The sum of all evens is 2550. And the sum of all odds is 2500.

total_even = 0
for number in range(101):
    if number % 2 == 0:
        total_even += number
print(total_even)

total_Odd = 0
for number in range(101):
    if number % 2 == 1:
        total_Odd += number
print(total_Odd)

# While Loop

    # While condition:
    #     # Code to execute

count = 0
while count < 5:
    print(count) # output: 0, 1, 2, 3, 4
    count = count + 1

    # While condition:
    #       # Code to execute
    # else:
            # Code to execute

count2 = 0
while count2 < 5:
    print(count2) # output: 0, 1, 2, 3, 4
    count2 = count2 + 1
else:
    print(count2) # output: 5

# Break and Continue - Part 1

    # While condition:
    #     # Code to execute
    #     if condition:
    #         break

count3 = 0
while count3 < 5:
    print(count3) # output: 0, 1, 2
    count3 = count3 + 1
    if count3 == 3:
        break
    
    # While condition:
        # Code to execute
        # if condition:
        # continue

count4 = 0
while count4 < 5:
    if count4 == 3:
        count4 += 1
        continue
    print(count4) # output: 0, 1, 2, 4
    count4 = count4 + 1

# For Loop

    # For variable in iterable:
        # Code to execute

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number) # output: 0, 1, 2, 3, 4, 5

# Loops in string

    # For variable in string:
        # Code to execute

language = "Python"
for letter in language:
    print(letter) # output: P, y, t, h, o, n

for i in range(len(language)):
    print(language[i]) # output: P, y, t, h, o, n

# loop in tuple

    # For variable in tuple:
        # Code to execute

numbers_tuple = (0, 1, 2, 3, 4, 5)
for number in numbers_tuple:
    print(number) # output: 0, 1, 2, 3, 4, 5

# loop in dictionary
    # For variable in dictionary:
        # Code to execute

person = {
    'first_name':'Kal',
    'last_name':'Castillo',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key) # output: first_name, last_name, age, country, is_marred, skills, address

for key, value in person.items():
    print(key, value) # output: first_name Kal, last_name Castillo, age 250, country Finland, is_marred True, skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], address {'street': 'Space street', 'zipcode': '02210'}

# Loops in set

    # For variable in set:
        # Code to execute
        # Note: Set is an unordered collection of unique elements

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company) # output: Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon

# Break and Continue - Part 2
# Break
numbers2 = (0, 1, 2, 3, 4, 5)
for number in numbers2:
    print(number) # output: 0, 1, 2
    if number == 3:
        break

# Continue
numbers3 = (0, 1, 2, 3, 4, 5)
for number in numbers3:
    print(number) 
    if number == 3:
        continue
    print('Net number should be ', number + 1) if number != 5 else print('loop`s end')
    print('outside the loop')

# Range Function

lst = list(range(11))
print(lst) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st= set(range(11))
print(st) # output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst2 = list(range(0, 11, 2))
print(lst2) # output: [0, 2, 4, 6, 8, 10]
st= set(range(0, 11, 2))
print(st) # output: {0, 2, 4, 6, 8, 10}

lst3 = list(range(11, 0, -2))
print(lst3) # output: [11, 9, 7, 5, 3, 1]

# for variable in range(start, end, step):

for number in range(11):
    print(number) # output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Nested Loops

    # for x in y:
        # for t in x:
            # print(t)

person2 = {
    'first_name': 'Kal',
    'last_name': 'Castillo',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person2:
    if key == 'skills':
        for skill in person2[key]:
            print(skill) # output: JavaScript, React, Node, MongoDB, Python

# For else

    # for variable in iterable:
        # Code to execute
    # else:
        # Code to execute

for number in range(11):
    print(number) # output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
else:
    print('The loop stop at ', number) # output: The loop stop at 10