# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Firulais'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
print(dog) # {'name': 'Firulais', 'color': 'Black', 'breed': 'Labrador', 'legs': 4}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'Carlos',
    'last_name': 'Fernandez',
    'gener': 'Masculine',
    'age': 27,
    'marital_status': 'Single',
    'skills': ['Puntual', 'Comunicativo', 'Resolutivo'],
    'location': {
        'country': 'Australia',
        'city': 'Sidney',
        'Address': '123 Wall Street'
    }
}

print(student) # {'first_name': 'Carlos', 'last_name': 'Fernandez', 'gener': 'Masculine', 'age': 27, 'marital_status': 'Single', 'skills': ['Puntual', 'Comunicativo', 'Resolutivo'], 'location': {'country': 'Australia', 'city': 'Sidney', 'Address': '123 Wall Street'}}

# Get the length of the student dictionary

print(len(student)) # 7

# Get the value of Location and check the data type, it should be a list

values = student['location'].values()
print(values) # dict_values(['Australia', 'Sidney', '123 Wall Street'])
print(type(values)) # <class 'dict_values'>

# Modify the skills values by adding one or two skills

student['skills'].append('Evolutivo')
print(student) # {'first_name': 'Carlos', 'last_name': 'Fernandez', 'gener': 'Masculine', 'age': 27, 'marital_status': 'Single', 'skills': ['Puntual', 'Comunicativo', 'Resolutivo', 'Evolutivo'], 'location': {'country': 'Australia', 'city': 'Sidney', 'Address': '123 Wall Street'}}

# Get the dictionary keys as a list

keys = student.keys()
print(keys) # dict_keys(['first_name', 'last_name', 'gener', 'age', 'marital_status', 'skills', 'location'])

# Get the dictionary values as a list

values1 = student.values()
print(values1) # dict_values(['Carlos', 'Fernandez', 'Masculine', 27, 'Single', ['Puntual', 'Comunicativo', 'Resolutivo', 'Evolutivo'], {'country': 'Australia', 'city': 'Sidney', 'Address': '123 Wall Street'}])

# Change the dictionary to a list of tuples using items() method

tuple_list = list(student.items())
print(tuple_list) # [('first_name', 'Carlos'), ('last_name', 'Fernandez'), ('gener', 'Masculine'), ('age', 27), ('marital_status', 'Single'), ('skills', ['Puntual', 'Comunicativo', 'Resolutivo', 'Evolutivo']), ('location', {'country': 'Australia', 'city': 'Sidney', 'Address': '123 Wall Street'})]

# Delete one of the items in the dictionary

del student['location']

# Delete one of the dictionaries

del student['first_name']

# Create a dictionary

empty_dict = {}
dct = { 'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Other example

person = {
    'first_name': 'Kal',
    'last_name': 'Castillo',
    'age': 250,
    'country': 'España',
    'is_married': False,
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python'],
    'address': {
        'street': 'Space Street',
        'zipcode': '12345'
    }
}

# Accessing values in a dictionary

print(len(dct)) # 4
print(len(person)) # 7

# Accessing dictionary items

print(dct['key1']) # value1
print(dct['key4']) # value4

print(person['first_name']) # Kal
print(person['country']) # España
print(person['skills']) # ['HTML', 'CSS', 'JavaScript', 'Python']
print(person['skills'][0]) # HTML
print(person['address']['street']) # Space Street
# print(person['city']) # KeyError: 'city' not found in the dictionary

# Using get() method to access values

print(person.get('first_name')) # Kal
print(person.get('country')) # None
print(person.get('skills')) # ['HTML', 'CSS', 'JavaScript', 'Python']
print(person.get('city')) # None

# Adding items to a dictionary

dct2 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct2['key5'] = 'value5'
print(dct2) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

person2 = {
    'first_name': 'Kal',
    'last_name': 'Castillo',
    'age': 250,
    'country': 'España',
    'is_married': False,
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python'],
    'address': {
        'street': 'Space Street',
        'zipcode': '12345'
    }
}

person2['job_title'] = 'Developer'
print(person2) # {'first_name': 'Kal', 'last_name': 'Castillo', 'age': 250, 'country': 'España', 'is_married': False, 'skills': ['HTML', 'CSS', 'JavaScript', 'Python'], 'address': {'street': 'Space Street', 'zipcode': '12345'}, 'job_title': 'Developer'}
person2['skills'].append('Django')
print(person2['skills']) # ['HTML', 'CSS', 'JavaScript', 'Python', 'Django']
print(person2) # {'first_name': 'Kal', 'last_name': 'Castillo', 'age': 250, 'country': 'España', 'is_married': False, 'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django'], 'address': {'street': 'Space Street', 'zipcode': '12345'}, 'job_title': 'Developer'}

# Modifying items in a dictionary

dct2['key1'] = 'new_value1'
print(dct2) # {'key1': 'new_value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
person2['age'] = 251
print(person2['age']) # 251
person2['first_name'] = 'Kal-El'
print(person2['first_name']) # Kal-El
print(person2) # {'first_name': 'Kal-El', 'last_name': 'Castillo', 'age': 251, 'country': 'España', 'is_married': False, 'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django'], 'address': {'street': 'Space Street', 'zipcode': '12345'}, 'job_title': 'Developer'}

# Checking if a key exists in a dictionary

dct3 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key1' in dct3) # True
print('key5' in dct3) # False
print('value1' in dct3) # False
print('value1' in dct3.values()) # True

# Removing items from a dictionary

dct4 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct4.pop('key1')
print(dct4) # {'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct4.popitem()
print(dct4) # {'key2': 'value2', 'key3': 'value3'}
del dct4['key2']
print(dct4) # {'key3': 'value3'}

person3 = {
    'first_name': 'Kal',
    'last_name': 'Castillo',
    'age': 250,
    'country': 'España',
    'is_married': False,
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python'],
    'address': {
        'street': 'Space Street',
        'zipcode': '12345'
    }
}

person3.pop('first_name')
print(person3['first_name']) # KeyError: 'first_name' not found in the dictionary
person3.popitem()   # Remove the last item from the dictionary (in this case, 'address')
del person3['is_married'] # Delete the key 'is_married' from the dictionary

# Clearing a dictionary

dct5 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct5.clear()) # None

# Deleting a dictionary

dct6 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct6
# print(dct6) # NameError: name 'dct6' is not defined

# Copying a dictionary

dct7 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct8 = dct7.copy()
print(dct8) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Getting dictionary keys as a list

dct9 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct9.keys()
print(keys) # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting dictionary values as a list

dct10 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct10.values()
print(values) # dict_values(['value1', 'value2', 'value3', 'value4'])