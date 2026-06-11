# Higher order functions

# Function as a parameter

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) # 15

# Function as a return value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function2(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result_square = higher_order_function2('square')
print(f'The result to square is: {result_square(5)}') # 25

result_cube = higher_order_function2('cube')
print(f'The result to cube is: {result_cube(5)}') # 125

result_absolute = higher_order_function2('absolute')
print(f'The result to absolute is: {result_absolute(-5)}') # 5 positivo

# Python Closures

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(f'The result to closure is: {closure_result(10)}')
print(f'The result to closure is: {closure_result(20)}')

# Python Decorators

# Creating decorators

def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

# Examplo above with a decorator

'''This decorator function is a higher order function that takes a function as a parameter'''

def uppercase_decorator2(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator2
def greeting2():
    return 'Welcome to Python'
print(greeting2())   # WELCOME TO PYTHON

# Applying Multiple Decorators to a Single Function

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

# Accepting Parameters in Decorator Functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Kal", "Castillo",'Finland')

# Built-in Higher Order Functions

# Python - Map Function

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
# applying lambda
numbers_squared2 = map(lambda x : x ** 2, numbers)
print(list(numbers_squared2))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['kal', 'anggelo', 'carola', 'kim']

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# With lambda function
names_upper_cased2 = map(lambda name: name.upper(), names)
print(list(names_upper_cased2))

# Python filter function

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
names2 = ['Kal', 'Antonio', 'Fernando', 'Abraham']
def is_name_long(name):
    if len(name) > 5:
        return True
    return False

long_names = filter(is_name_long, names2)
print(list(long_names))

# Python - Reduce Function

from functools import reduce

numbers_str2 = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str2)
print(total)    # 15