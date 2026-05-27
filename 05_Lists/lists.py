# Exercises: Level 1

# 1: Declare an empty list

list_empty = list()
print(list_empty)

# 2: Declare a list with more than 5 items

my_list = ['Car', 'Bike', 'Bus', 'Train', 'Plane', 'Boat', 'Motocicly']

# 3: Find the length of your list

print(len(my_list)) # Output: 7

# 4: Get the first item, the middle item and the last item of the list

first_item_my_list = my_list[0]
middle_item_my_list = my_list[len(my_list) // 2]
last_item_my_list = my_list[-1]

print('First item:', first_item_my_list)  # Output: First item: Car
print('Middle item:', middle_item_my_list)  # Output: Middle item: Train
print('Last item:', last_item_my_list)  # Output: Last item: Motocicly

# 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Kal', 34, 1.70, 'Single', 'Pontevedra']

# 6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7: Print the list using print()

print(it_companies)

# 8: Print the number of companies in the list

print('Number of IT companies:', len(it_companies)) # Output: Number of IT companies: 7

# 9: Print the first, middle and last company

print('First company:', it_companies[0]) # Output: First company: Facebook
print('Middle company:', it_companies[len(it_companies) // 2]) # Output: Middle company: Apple
print('Last company:', it_companies[len(it_companies) - 1]) # Output: Last company: Amazon

# 10: Print the list after modifying one of the companies

changed_company = it_companies[1] = 'Firefox'
print(it_companies) # Output: ['Facebook', 'Firefox', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 11: Add an IT company to it_companies

it_companies.append('Twitter')
print(it_companies) # Output: ['Facebook', 'Firefox', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']

# 12: Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2 + 1, 'LinkedIn')
print(it_companies) # Output: ['Facebook', 'Firefox', 'Microsoft', 'Apple', 'LinkedIn', 'IBM', 'Oracle', 'Amazon', 'Twitter']

# 13: Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[1] = it_companies[1].upper()
print(it_companies) # Output: ['Facebook', 'FIREFOX', 'Microsoft', 'Apple', 'LinkedIn', 'IBM', 'Oracle', 'Amazon', 'Twitter']

# 14: Join the it_companies with a string '#;  '

joined_companies = '#;  '.join(it_companies)
print(joined_companies) # Output: Facebook#;  FIREFOX#;  Microsoft#;  Apple#;  LinkedIn#;  IBM#;  Oracle#;  Amazon#;  Twitter

# 15: Check if a certain company exists in the it_companies list.`

it_companies2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

if 'Google' in it_companies2:
    print(f'Google exists in the it_companies2 list.')
else:
    print(f'Google does not exist in the it_companies2 list.') 

# 16: Sort the list using sort() method

it_companies2.sort()
print(it_companies2) # Output: ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle']

# 17: Reverse the list in descending order using reverse() method

it_companies2.reverse()
print(it_companies2) # Output: ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

# 18: Slice out the first 3 companies from the list

first_three_companies = it_companies2[:3]
print(first_three_companies) # Output: ['Oracle', 'Microsoft', 'IBM']

# 19: Slice out the last 3 companies from the list

last_three_companies = it_companies2[-3:]
print(last_three_companies) # Output: ['Facebook', 'Apple', 'Amazon']

# 20: Slice out the middle IT company or companies from the list

middle_company = it_companies2[len(it_companies2) // 2 - 1:len(it_companies2) // 2]
print(middle_company) # Output: ['Google']

# 21: Remove the first IT company from the list

first_company_removed = it_companies2.pop(0)
print(f'Removed company: {first_company_removed}') # Output: Removed company: Oracle
print(it_companies2) # Output: ['Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

# 22: Remove the middle IT company or companies from the list

middle_company_removed = it_companies2.pop(len(it_companies2) // 2 - 1)
print(f'Removed company: {middle_company_removed}') # Output: Removed company: Google

# 23: Remove the last IT company from the list

last_company_removed = it_companies2.pop()
print(f'Removed company: {last_company_removed}') # Output: Removed company: Amazon
print(it_companies2) # Output: ['Microsoft', 'IBM', 'Facebook', 'Apple']

# 24: Remove all IT companies from the list

it_companies2.clear()
print(it_companies2) # Output: []

# 25: Destroy the IT companies list

del it_companies2

# 26: Join the following lists: front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'], back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack) # Output: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# 27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack) # Output: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']

# Exercises: Level 2

 # 1: The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
min = ages.pop(0)
max = ages.pop(-1)
print(ages)
print(min, max)

# Add the min age and the max age again to the list

ages.insert(0, min)
ages.insert(-1, max)
print(ages)

# Find the median age (one middle item or two middle items divided by two)

median_age = ages[len(ages) // 2]
print(median_age)

# Find the average age (sum of all items divided by their number )

sum_ages = sum(ages)
total_persons = len(ages)
average_age = sum_ages // total_persons
print('The avarage age is', average_age)

# Find the range of the ages (max minus min)

range = max - min
print('The Range of ages is', range)

# Compare the value of (min - average) and (max - average), use abs() method

min_age = min
max_age = max
average_age2 = sum(ages) / len(ages)

distance_min = abs(min_age - average_age)
distance_max = abs(max_age - average_age)

# Find the middle country(ies) in the countries list

countries = [
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

middle_index = len(countries) // 2 + 1 # output: 8
print('Middle country:', countries[middle_index]) # Output: Middle country: 'Uzbekistan'


# Divide the countries list into two equal lists if it is even if not one more country for the first half.

list10 = countries[:len(countries) // 2 + 1] # output: ['Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan']
list11 = countries[len(countries) // 2 + 1:] # output: ['Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

if len(list10) % len(list11) != 0:
    print('List 1 has more countries than List 2')
else:
    list11.append(list10[-1])

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
first, second, third, *scandic = countries3
print(first)      # output: China
print(second)     # output: Russia
print(third)      # output: USA
print(scandic)    # output: ['Finland', 'Sweden', 'Norway', 'Denmark']

# Lists in Python

# Creating a list

    # Using list built-in-function

lst = list()  # Using the list constructor

empty_lst = list()  # This is an empty list, it has no elements.
print(empty_lst)  # Output: []

    # Using square brackets []

lst2 = []

empty_lst2 = [] # This is also an empty list.
print(empty_lst2)  # Output: []

# Lists with inital values. We use len() to find the length of a list

fruits = ['banana', 'orange', 'mango', 'lemon']                                 # A list of fruits
vegtables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']                  # A list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yogurt']                          # A list of animal products
web_techs = ['HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'Node', 'MongoDB']  # A list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']               # A list of countries

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegtables)
print('Number of vegetables:', len(vegtables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# List can have different data types

lst3 = ['Kal', 300, True, {'country': 'Finland', 'city': 'Helsinki'}] # A list with different data types
print(lst3)  # Output: ['Kal', 300, True, {'country': 'Finland', 'city': 'Helsinki'}]

# Accessing list items

fruits2 = ['banana', 'orange', 'mango', 'lemon']

first_fruit = fruits2[0] # Accessing the first item
print('First fruit:', first_fruit)  # Output: First fruit: banana
second_fruit = fruits2[1] # Accessing the second item
print('Second fruit:', second_fruit)  # Output: Second fruit: orange
third_fruit = fruits2[2] # Accessing the third item
print('Third fruit:', third_fruit)  # Output: Third fruit: mango

# last item can be accessed using negative indexing

last_index = len(fruits2) - 1 # Finding the last index
last_fruit = fruits2[last_index] # Accessing the last item

# Accessing the last item using negative indexing

fruits3 = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits3[-4]
last_fruit = fruits3[-1]
second_last = fruits3[-2]
print(first_fruit)      # output: banana
print(last_fruit)       # output: lemon
print(second_last)      # output: mango

# Unpacking List Items

lst4 = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst4
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# First Example
fruits4 = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits4
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries2 = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries2
print(gr)           # Germany
print(fr)           # France
print(bg)           # Belgium
print(sw)           # Sweden
print(scandic)      # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)           # Estonia