# Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.

import random, string

def random_user_id():
    combine_letter_digits = string.ascii_letters + string.digits
    user_id = ''
    for _ in range(6):
        user_id += random.choice(combine_letter_digits)
    return user_id
print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

number_of_characters_id = int(input('Enter Numbers of ID: '))
number_of_ids = int(input('Enter the number of IDS: '))

def user_id_gen_by_user():
    for _ in range(number_of_ids):
        id_generate = ''
        for _ in range(number_of_characters_id):
            id_generate += random.choice(string.ascii_letters + string.digits)
        print(id_generate)
print(user_id_gen_by_user())
# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    return f'El Color Generado es: rgb{random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)}'

print(rgb_color_gen())

import modules
print(modules.generate_full_name('Kal', 'Castillo')) # Kal Castillo

#from modules import generate_full_name, sum_two_nums, person, gravity
#print(generate_full_name('Asabneh','Yetayeh'))
#print(sum_two_nums(1,9))
#mass = 100
#weight = mass * gravity
#print(weight)
#print(person['firstname'])

#from modules import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
#print(fullname('Asabneh','Yetayeh'))
#print(total(1, 9))
#mass = 100 
#weight = mass * g
#print(weight)
#print(p)
#print(p['firstname'])

# Imports Built-in Modules

# OS Module

import os
# Creating a directory
#os.mkdir('directory_name')
# Changing the current directory
#os.chdir('path')
# Getting current working directory
#os.getcwd()
# Removing directory
#os.rmdir()

# Sys Module

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
#print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

# Statistics Module

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# Math Module

from math import *
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi as  PI
print(PI) # 3.141592653589793

# String Module

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random Module

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive