# Exercises level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def two_numbers_add(a, b):
    return a + b
print(two_numbers_add(2, 3)) # Output: 5

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def space_of_circle(pi, r):
    area = pi * r * r
    return area
print(space_of_circle(pi = 3.14, r = 10)) # Output: 314.0

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    total = 0;
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            print(f"'{arg}' is not a number. Please provide only numbers.")
    return total
print(add_all_nums(1, 2, 3, 4, 5)) # Output: 15
print(add_all_nums(1, 2, 'three', 4, 5)) # Output: 'three' is not a number. Please provide only numbers. 12

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f'{celsius}°C is equal to {fahrenheit}°F'
print(convert_celsius_to_fahrenheit(0)) # Output: 0°C is equal to 32.0°F
print(convert_celsius_to_fahrenheit(100)) # Output: 100°C is equal to 212.0°F

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']

    if month in Autumn:
        return 'Autumn'
    elif month in Winter:
        return 'Winter'
    elif month in Spring:
        return 'Spring'
    elif month in Summer:
        return 'Summer'
    else:
        return 'Invalid month'
print(check_season('October')) # Output: Autumn
print(check_season('January')) # Output: Winter
print(check_season('April')) # Output: Spring
print(check_season('July')) # Output: Summer

# 6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4)) # Output: 1.0
print(calculate_slope(2, 3, 2, 5)) # Output: Slope is undefined (vertical line)

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f'Two real roots: {root1} and {root2}'
    elif discriminant == 0:
        root = -b / (2*a)
        return f'One real root: {root}'
    else:
        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        return f'Two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i'
print(solve_quadratic_eqn(1, -3, 2)) # Output: Two real roots: 2.0 and 1.0
print(solve_quadratic_eqn(1, -2, 1)) # Output: One real root: 1.0
print(solve_quadratic_eqn(1, 2, 5)) # Output: Two complex roots: -1.0 + 2.0i and -1.0 - 2.0i

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5]) # Output: 1 # 2 # 3 # 4 # 5
print_list(["A", "B", "C"]) # Output: A # B # C

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops). print(reverse_list([1, 2, 3, 4, 5])), print(reverse_list(["A", "B", "C"])) 

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lista):
    capitalize_list = []
    for item in lista:
        capitalize_list.append(item.capitalize())
    return capitalize_list
print(capitalize_list_items(['manzana', 'pera', 'uva']))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst, new_item):
    lst.append(new_item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(['potato', 'manzana', 'leche', 'pera'], 'manzana'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(number):
    total = 0
    for num in range(number + 1):
        total += num
    return total
print(sum_of_numbers(10))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(number):
    total_odds = 0
    for num in range(number + 1):
        if num % 2 == 1:
            total_odds += num
    return total_odds

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(number):
    total_evens = 0
    for num in range(number + 1):
        if num % 2 == 0:
            total_evens += num
    return total_evens


# Exercises level 2

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    total_factorial = 1
    for num in range(1, number + 1):
        total_factorial *= num
    return total_factorial
print(f'El factorial del un numero es: {factorial(5)}')

# 2. Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(epty):
    if not epty:
        return True
    else:
        return False

# 3. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

from collections import Counter
import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def calculate_mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())

    modes = [num for num, count in counts.items() if count == max_count]

    if len(modes) == len(counts):
        return None  # No mode
    return modes


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

data = [1, 2, 2, 3, 4, 5]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

# 4. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

def greet(name= 'Kal'):
    if name:
        return f'Hello, {name}'
    else:
        return 'Hello, Guest!'
    
print(greet('Kal'))
print(greet('Jonathan'))

# 5. Create a function called show_args to take an arbitrary number of named arguments and print their names and values. show_args(name="Alice", age=30, city="New York"), show_args(name="Bob", pet="Fluffy, the bunny")

def show_args(**kwarg):
    for key, value in kwarg.items():
        print(f'{key}: {value}')

show_args(name='Alice', age=30, city='New York')
show_args(name='Bob', pet='Fluffy, the bunny')

# Exercises level 3

# 1. Write a function called is_prime, which checks if a number is prime.
# 2. Write a functions which checks if all items are unique in the list.
# 3. Write a function which checks if all the items of the list are of the same data type.
# 4. Write a function which check if provided variable is a valid python variable
# 5. Go to the data folder and access the countries-data.py file.
# 6. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# 7. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order

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