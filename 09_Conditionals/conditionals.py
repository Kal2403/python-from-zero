# Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 30
your_age = int(input('Enter your age: '))
if my_age > your_age:
    print(f'I am {my_age - your_age} years older than you.')
else:
    print(f'You are {your_age - my_age} years older than me.')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

number_a = int(input('Enter number a: '))
number_b = int(input('Enter number b: '))
if number_a > number_b:
    print(f'{number_a} is greater than {number_b}.')
elif number_a < number_b:
    print(f'{number_a} is smaller than {number_b}.')
else: 
    print(f'{number_a} is equal to {number_b}.')

# Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores: # 90-100, A; 80-89, B; 70-79, C; 60-69, D; 0-59, F

grade_student = int(input('Enter your grade: '))
if grade_student <= 100 and grade_student >= 90:
    print('The grade of the student is : A')
elif grade_student <= 89 and grade_student >= 80:
    print('The grade of the student is: B')
elif grade_student <= 79 and grade_student >= 70:
    print('The grade of the studen is: C')
elif grade_student <= 69 and grade_student >= 60:
    print('The grade of the studen is: D')
else:
    print('The grade of the studen is: F')

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
    # September, October or November, the season is Autumn. 
    # December, January or February, the season is Winter. 
    # March, April or May, the season is Spring 
    # June, July or August, the season is Summer

month = input('Enter the month of the year: ')

if month == 'September' or month == 'November' or month == 'October':
    print(f'Is month is {month} the season of the year is: Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print(f'Is month is {month} the season of the year is: Winter')
elif  month == 'March' or month == 'April' or month == 'May':
    print(f'Is month is {month} the season of the year is: Spring')
else:
    print(f'Is month is {month} the season of the year is: Summer')

# 3. The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']
    # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_add = input('Enter the fruit: ')

if fruit_to_add in fruits:
    print(fruits)
else:
    fruits.append(fruit_to_add)
    print(fruits)

# Exercises level 3

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Kal',
    'last_name': 'Castillo',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    print(person['skills'][int(len(person['skills']) // 2)])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Yes it have Python skills')
    else:
        print('No does not have')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
    # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
elif 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
else:
    print('unknown title')

# If the person is married and if he lives in Finland, print the information in the following format:

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} lives in {person["country"]}. He is married')

# Conditionals

# syntax: if condition:

# if condition:
#     code to execute if condition is true

a = 3
if a > 0:
    print('A is a positive number') # output: A is a positive number

# syntax: if else condition:

# if condition:
#     code to execute if condition is true
# else:
#     code to execute if condition is false

a2 = 3
if a2 < 0:
    print('A2 is a negative number')
else:
    print('A2 is a positive number') # output: A2 is a positive number

# syntax: if elif else condition:

a3 = 0
if a3 > 0:
    print('A3 is a positive number')
elif a3 < 0:
    print('A3 is negative number')
else:
    print('A3 is Zero')  # output: A3 is Zero

# Shorthand if else condition:
# condition_if_true if condition else condition_if_false

a4 = 3
print('A4 is a positive number') if a4 > 0 else print('A4 is negative number') # output: A4 is a positive number

# Nested conditions:
# if condition:
#     code
#     if condition:
#         code

a5 = 0
if a5 > 0:
    if a5 % 2 == 0:
        print('A5 is positive and even integer')
    else:
        print('A5 is positive and odd integer')
elif a5 < 0:
    if a5 % 2 == 0:
        print('A5 is negative and even integer')
    else:
        print('A5 is negative and odd integer')
else:
    print('A5 is zero') # output: A5 is zero

# If Condition and Logical Operators
# if condition and condition:
#     code

a6 = 0
if a6 > 0 and a6 % 2 == 0:
    print('A6 is a positive and even number')
elif a6 > 0 and a6 % 2 != 0:
    print('A6 is a positive integer')
elif a6 == 0:
    print('A6 is zero') # output: A6 is zero
else:
    print('A6 is a negative number')

# If Condition and Logical Operators
# if condition or condition:
#     code

user = 'Kal'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied') # output: Access denied