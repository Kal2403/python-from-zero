# Exercises

from functools import reduce 

countries_exercises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names_exercises = ['Kal', 'Lidiya', 'Fernando', 'Abraham']
numbers_exercises = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Explain the difference between map, filter, and reduce.

# Map transform every element
print(list(map(lambda x: x * 2, numbers_exercises)))

# Filter select element by condition
print(list(filter(lambda x: x % 2 == 0, numbers_exercises)))

# Reduce just reduce by one element
print(reduce(lambda a, b: a + b, numbers_exercises))

# 2. Explain the difference between higher order function, closure and decorator

# Higher-order function: acept or return a function
def apply_func(func, value):
    return func(value)

# Clousure: inner function remembers variables from outer scope
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)

# Decorator: modifies or extends another function
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# 3. Define a call function before map, filter or reduce, see examples.

def square(n):
    return n ** 2

square = list(map(square, numbers_exercises))
print(square)

# 4. Print each country using a for loop

for country in countries_exercises:
    print(country)


# 5. Print each name using a for loop

for name in names_exercises:
    print(name)


# 6. Print each number using a for loop

for number in numbers_exercises:
    print(number)


# 7. Convert countries to uppercase using map

countries_upper = list(map(str.upper, countries_exercises))


# 8. Create a list of squared numbers using map

numbers_squared = list(map(lambda n: n ** 2, numbers_exercises))


# 9. Convert names to uppercase using map

names_upper = list(map(str.upper, names_exercises))


# 10. Filter countries containing 'land'

countries_with_land = list(
    filter(lambda country: 'land' in country.lower(), countries_exercises)
)


# 11. Filter countries with exactly six characters

countries_six_chars = list(
    filter(lambda country: len(country) == 6, countries_exercises)
)


# 12. Filter countries with six or more characters

countries_six_or_more = list(
    filter(lambda country: len(country) >= 6, countries_exercises)
)


# 13. Filter countries starting with 'E'

countries_starting_e = list(
    filter(lambda country: country.startswith('E'), countries_exercises)
)


# 14. Chain map, filter and reduce

result = reduce(
    lambda a, b: a + b,
    filter(
        lambda n: n > 10,
        map(lambda n: n ** 2, numbers_exercises)
    )
)

print(result)


# 15. Return only string items from a list

def get_string_lists(items):
    return list(
        filter(lambda item: isinstance(item, str), items)
    )


# Example
print(get_string_lists([1, "Kal", True, "Python", 5]))


# 16. Sum all numbers using reduce

total = reduce(
    lambda a, b: a + b,
    numbers_exercises
)

print(total)


# 17. Concatenate countries into a sentence using reduce

sentence = (
    reduce(
        lambda a, b: a + ", " + b,
        countries_exercises[:-1]
    )
    + ", and "
    + countries_exercises[-1]
    + " are north European countries"
)

print(sentence)


# 18. Return countries matching a given pattern

def categorize_countries(countries, pattern):
    return list(
        filter(
            lambda country: pattern.lower() in country.lower(),
            countries
        )
    )


# Example
print(categorize_countries(countries_exercises, "land"))


# 19. Count countries by starting letter

def count_countries_by_starting_letter(countries):
    result = {}

    for country in countries:
        first_letter = country[0]

        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result


# Example
print(count_countries_by_starting_letter(countries_exercises))


# 20. Return the first ten countries

def get_first_ten_countries(countries):
    return countries[:10]


# 21. Return the last ten countries

def get_last_ten_countries(countries):
    return countries[-10:]

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