# Exercises

# 1. Filter only negative and zero in the list using list comprehension

numbers3 = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_nums = [i for i in numbers3 if i > 0]
print(positive_nums)

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatt_list = [num for row in list_of_lists for num in row]
print(flatt_list) # output [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using list comprehension create the following list of tuples
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

result = [(n,) + tuple(n**p for p in range(6)) for n in range(11)]

print(result)


# List Compregension

# [expression for i in iterable if condition]

language = 'Python'
lst = list(language) # Changing the string to list
print(type(lst)) # type list
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

lst2 = [i for i in language]
print(lst2) # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers2 = [(i, i * i) for i in range(11)]
print(numbers2) 

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a Lambda Function

# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5

# Lets change the above function to a lambda function

add_two_nums2 = lambda a, b: a + b
print(add_two_nums2(3, 3)) # 6

# Self invoking lambda function
(lambda a, b: a + b)(5, 5) # 10 need to encapsulate it in print() to see the result in the console

square = lambda x: x**2
print(squares(3)) # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variables = lambda a, b, c: a ** 2 - 3 * b + 3 * c
print(multiple_variables)

# Lambda function inside another function

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32