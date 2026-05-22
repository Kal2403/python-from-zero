# Day 3 Operators

age = 34
height = 1.70
print('Complex number: ', 2 + 3j)

# Calculating the area of a triangle

base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

area_triangle = 0.5 * base * height

print('The area of the triangle is: ', area_triangle)

# Calculating the perimeter of a triangle

side_a = float(input('Enter the length of side a: '))
side_b = float(input('Enter the length of side b: '))
side_c = float(input('Enter the length of side c: '))

perimeter_triangle = side_a + side_b + side_c

print('The perimeter of the triangle is : ', perimeter_triangle)

# Calculating the area and perimeter of a rectangle

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

print('The area of the rectangle is: ', area_rectangle)
print('The perimeter of the rectangle is: ', perimeter_rectangle)

# Calculating the area and circumference of a circle

import math

radius = float(input('Enter the radius of the circle: '))

area_circle = math.pi * radius ** 2
circumference_circle = 2 * math.pi * radius

print('The area of the circle is: ', area_circle)
print('The circumference of the circle is: ', circumference_circle)

# Calculating the slope

slope1 = 2

y_intercept = (0, -2)
x_intercept = (1, 0)

print('Slope: ', slope1)
print('Y-intercept: ', y_intercept)
print('X-intercept: ', x_intercept)

# Calculating Euclidean distance

x1, y1 = 2, 2
x2, y2 = 6, 10

slope2 = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)

print('Slope: ', slope2)
print('Distance: ', distance)

# Comparing the slopes

if slope1 == slope2:
    print('The slopes are equal.')
else:
    print('The slopes are not equal.')

# Calculating the value of Y when X is zero (y = x**2 + 6x + 9)

for x in range(-10, 11):
    y = x ** 2 + 6 * x + 9

    if y == 0:
        print(f'When y is 0, x is: {x}')

# Falsy comparisons

py = 'python'
dr = 'dragon'

len(py) != len(dr)
'on' in py and 'on' in dr

sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

length_py = len(py)
float_len = float(length_py)
str_len = str(float_len) 

print('Length of python as a string: ', str_len)

# Even numbers

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')

# Check if the floor division of 7 by 3 is equal to the int conversion of 2.7

if 7 // 3 == int(2.7):
    print('The floor division of 7 by 3 is equal to the int conversion of 2.7.')
else:
    print('The floor division of 7 by 3 is not equal to the int conversion of 2.7.')

# Check if the type of '10' is equal to the type of 10

if type('10') == type(10):
    print('The type of "10" is equal to the type of 10.')
else:
    print('The type of "10" is not equal to the type of 10.')

# Check if int('9.8') is equal to 10

if int(float('9.8')) == 10:
    print('int("9.8") is equal to 10.')
else:
    print('int("9.8") is not equal to 10.')

# Calculate pay of the persons working hours and hourly rate

hours = float(input('Enter the number of hours worked: '))
hourly_rate = float(input('Enter the hourly rate: '))

pay = hours * hourly_rate

print('The pay of the person is: ', pay)

# Calculate the number of seconds a person can live. Enter the number of years.

years = int(input('Enter the number of years: '))
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('The number of seconds a person can live if they live for 100 years is: ', seconds)

# Write a Python Scrip that displays the following table

for i in range(1, 6):
    print(i, 1, i, i ** 2, i ** 3)