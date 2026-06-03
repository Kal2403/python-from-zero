# Exercises level 1

# Functions in Python

    # def function_name():
        # code
        # code
    # function_name() 

def generate_full_name():
    first_name = 'Kal'
    last_name = 'Castillo'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # Output: Kal Castillo

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers() # Output: 5

# Function returning a value Part 1

def generate_full_name2():
    first_name2 = 'Kal'
    last_name2 = 'Castillo'
    space2 = ' '
    full_name2 = first_name2 + space2 + last_name2
    return full_name2
print(generate_full_name2()) # Output: Kal Castillo

def add_two_numbers2():
    num_one2 = 2
    num_two2 = 3
    total2 = num_one2 + num_two2
    return total2
print(add_two_numbers2()) # Output: 5

# Function with parameters

def greetings(name):
    message = name + ', Welcome to Python for Everyone!'
    return message
print(greetings('Kal')) # Output: Kal, Welcome to Python for Everyone!

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90)) # Output: 100

def square_number(x):
    return x * x
print(square_number(2)) # Output: 4

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(10)) # Output: 314.0

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total +=i
    return total
print(sum_of_numbers(10)) # Output: 55
print(sum_of_numbers(100)) # Output: 5050

# Functions with two parameters

def generate_full_name3(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(f'Full name: {generate_full_name3("Kal", "Castillo")}') # Output: Full name: Kal Castillo

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print(f'Sum of two numbers: {sum_two_numbers(2, 3)}') # Output: Sum of two numbers: 5

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print(f'Your age is: {calculate_age(2026, 1992)}') # Output: Your age is: 34

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'
    return weight
print(f'Weight of an object in Newtons: {weight_of_object(100, 9.81)}') # Output: Weight of an object in Newtons: 981.0 N

# Passing Arguments with key and value

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Kal', lastname = 'Castillo') # Output: Kal Castillo

def add_two_numbers3(num1, num2):
    total3 = num1 + num2
    return total3
print(add_two_numbers3(num2 = 3, num1 = 2)) # Output: 5

# Function returning a Value Part 2

def isEven(n):
    if n * 2 == 0:
        return True
    return False
print(isEven(2)) # Output: True
print(isEven(3)) # Output: False

def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10)) # Output: [0, 2, 4, 6, 8, 10]

# Arbitrary number of arguments

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(1, 2, 3, 4, 5)) # Output: 15

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team A', 'Kal', 'Castillo', 'Python') # Output: Team A # Kal # Castillo # Python

# Keyword arguments and unpacking

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

# Function as parameter of another function

def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # Output: 27