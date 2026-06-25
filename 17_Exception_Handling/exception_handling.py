# Exercises:

# 1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, es, ru = names
print(nordic_countries) # ['Finland', 'Sweden', 'Norway','Denmark','Iceland']
print(es) # Estonia
print(ru) # Russia

# Exception Handling in Python

# try:
    # code in this block if things go well
# except:
    # code in this block run if things go wrong

try:
    print(10 + '5')
except:
    print('Something went wrong')

# output: 'Something went wrong'

try:
    name = input('Enter your name:')
    years_born = input('Years you were born:')
    age = 2026 - int(years_born)
    print(f'You are {name}, and your age is {age}.')
except:
    print('Something went wrong')


try:
    name2 = input('Enter your name:')
    year_born2 = input('Year you born:')
    age2 = 2026 - int(year_born2)
    print(f'You are {name2}. And your age is {age2}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

# Packing and Unpacking Arguments in Python

# Unpacking

# def sum_of_five_nums(a, b, c, d, e):
    # return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15 becouse we are unpacking

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Kal', 'country':'España', 'city':'Galicia', 'age':34}
print(unpacking_person_info(**dct)) # Kal lives in España, Galicia. He is 34 years old.

# Packing

# Packing Lists

def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum_all(1, 2, 4))
print(sum_all(3, 4, 6, 2, 5, 8))

# Packing Dictionaries

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packing_person_info(name="Kal", country="España", City="Pontevedra", age=34))

# Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst4 = [0, *lst_one, *lst_two]
print(lst4)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerate

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

# Zip

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)