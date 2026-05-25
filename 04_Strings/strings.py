# Exercises: Strings

# 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'

words = ['Thirty', 'Days', 'Of', 'Python']
sentence = ' '.join(words)
print(sentence) # Output: Thirty Days Of Python

# 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

text = 'Coding' + ' For' + ' All'
print(text) # Output: Coding For All

# 3: Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4: Print the variable company using print().

print(company) # Output: Coding For All

# 5: Print the length of the company string using len() method and print().

print(len(company)) # Output: 14

# 6: Change all the characters to uppercase letters using upper() method.

print(company.upper()) # Output: CODING FOR ALL

# 7: Change all the characters to lowercase letters using lower() method.

print(company.lower()) # Output: coding for all

# 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize()) # Output: Coding for all
print(company.title())      # Output: Coding For All
print(company.swapcase())   # Output: cODING fOR aLL

# 9: Cut(slice) out the first word of Coding For All string.

print(company[7:]) # Output: For All

# 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.find('Coding')) # Output: 0
print(company.index('Coding')) # Output: 0
print('Coding' in company) # Output: True

# 11: Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python')) # Output: Python For All

# 12: Change "Python for Everyone" to "Python for All" using the replace method or other methods.

text2 = "Python for Everyone"
print(text2.replace('Everyone', 'All')) # Output: Python for All

# 13: Split the string 'Coding For All' using space as the separator (split()) .

print(company.split()) # Output: ['Coding', 'For', 'All']

# 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', ')) # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 

# 15: What is the character at index 0 in the string Coding For All.

print(company[0]) # Output: C

# 16: What is the last index of the string Coding For All.

print(company[-1]) # Output: l

# 17: What character is at index 10 in "Coding For All" string.

print(company[10]) # Output: A

# 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.

phrase = 'Python For Everyone'
acronym = ''.join(word[0] for word in phrase.split())
print(acronym) # Output: PFE

# 19: Create an acronym or an abbreviation for the name 'Coding For All'.

acronym2 = ''.join(word[0] for word in company.split())
print(acronym2) # Output: CFA

# 20: Use index to determine the position of the first occurrence of C in Coding For All.

print(company.index('C'))  # Output: 0

# 21: Use index to determine the position of the first occurrence of F in Coding For All.

print(company.index('F'))  # Output: 7

# 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.

text3 = 'Coding For All People'
print(text3.rfind('l')) # Output: 18

# 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because')) # Output: 31

# 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence2.rindex('because')) # Output: 47

# 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

start_index = sentence2.find('because because because') # output: 31
end_index = start_index + len('because because because') # output: 31 + 23 = 54
print(sentence2[start_index:end_index]) # Output: because because because

# 26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence2.find('because')) # Output: 31

# 27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence2[start_index:end_index]) # Output: because because because

# 28: Does 'Coding For All' start with a substring Coding?

print(company.startswith('Coding')) # Output: True

# 29: Does 'Coding For All' end with a substring coding?

print(company.endswith('coding')) # Output: False

# 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.

text4 = '   Coding For All      '
print(text4.strip()) # Output: Coding For All

# 31: Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython thirty_days_of_python

var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'

print(var1.isidentifier())  # Output: False
print(var2.isidentifier())  # Output: True

# 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries) # Output: Django # Flask # Bottle # Pyramid # Falcon

# 33: Use the new line escape sequence to separate the following sentences: I am enjoying this challenge, I just wonder what is next.

print('I am enjoying this challenge.\nI just wonder what is next.') # Output: I am enjoying this challenge. in a new line (I just wonder what is next.)

# 34: Use a tab escape sequence to write the following lines: Name      Age     Country, Kal     25     Peruvian

print('Name\tAge\tCountry\nKal\t25\tPeruvian') # Output: Name    Age     Country in a new line (Kal     25     Peruvian)

# 35: Use the string formatting method to display the following: radius = 10, area = 3.14 * radius ** 2.

radius = 10
pi = 3.14
area = pi * radius ** 2
print('The area of a circle with radius %d is %.2f.' % (radius, area))

# 36: Make the following using string formatting methods: 8 + 6 = 14, 8 - 6 = 2, 8 * 6 = 48, 8 / 6 = 1.33, 8 % 6 = 2, 8 // 6 = 1, 8 ** 6 = 262144.

num1 = 8
num2 = 6
print('%d + %d = %d' % (num1, num2, num1 + num2)) # Output: 8 + 6 = 14
print('%d - %d = %d' % (num1, num2, num1 - num2)) # Output: 8 - 6 = 2
print('%d * %d = %d' % (num1, num2, num1 * num2)) # Output: 8 * 6 = 48
print('%d / %d = %.2f' % (num1, num2, num1 / num2)) # Output: 8 / 6 = 1.33
print('%d %% %d = %d' % (num1, num2, num1 % num2)) # Output: 8 % 6 = 2
print('%d // %d = %d' % (num1, num2, num1 // num2)) # Output: 8 // 6 = 1
print('%d ** %d = %d' % (num1, num2, num1 ** num2)) # Output: 8 ** 6 = 262144

# Strings in Python

# Creating a String

letter = 'p'                # A string could be a single character or a bunch of characters
print(letter)               # Output: p
print(len(letter))          # Output: 1
greeting = 'Hello, World!'  # String could be made a single or double quotes
print(greeting)             # Output: Hello, World!
print(len(greeting))        # Output: 13
sentence = "I hope you are enjoying learning Python."
print(sentence)             # Output: I hope you are enjoying learning Python.

# Multiline string is created by using triple single (''') or triple double quotes (""").

multiline_string = '''I am a teacher and enjoy teaching. I didn't find anything as rewarding as empowering people. To learn Python.'''
print(multiline_string)     # Output: I am a teacher and enjoy teaching. I didn't find anything as rewarding as empowering people. To learn Python.

# String Concatenation

first_name = 'Kal'
last_name = 'Castillo'
space = ' '
full_name = first_name + space + last_name
print(full_name)          # Output: Kal Castillo
# Checking the length of a string
print(len(first_name))     # Output: 3
print(len(last_name))     # Output: 8
print(len(first_name) > len(last_name))  # Output: False
print(len(full_name))     # Output: 12

# Escape Sequences in Strings

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

# Example of escape sequences

print('I hope everyone is enjoying the Python Challenge.\nAre you?') # Output: I hope everyone is enjoying the Python Challenge. in a new line (Are you?)
print('Days\tTopics\tExercises')          # Output: Days    Topics   Exercises (Tab space between each word)
print('Day 1\t5\t5')                      # Output: Day 1   5   5 (Tab space between each word)
print('Day 2\t6\t20')                     # Output: Day 2   6   20 (Tab space between each word)
print('Day 3\t5\t23')                     # Output: Day 3   5   23 (Tab space between each word)
print('Day 4\t1\t35')                     # Output: Day 4   1   35 (Tab space between each word)
print('This is a backslash symbol (\\)')  # Output: This is a backslash symbol (\)
print('In every programming language it starts with \"Hello, World!\"') # Output: In every programming language it starts with "Hello, World!"

# String Formatting

# Strings only

first_name1 = 'Kal'
last_name1 = 'Castillo'
language = 'Python'
formatted_string = 'I am %s %s. I teach %s.' % (first_name1, last_name1, language)
print(formatted_string)  # Output: I am Kal Castillo. I teach Python.

# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string2 = 'The area of a circle with radius %d is %.2f.' % (radius, area) # Output: The area of a circle with radius 10 is 314.00.

python_libraries = ['Django', 'Flask', 'NumPy', 'Mathplotlib', 'Pandas']
formatted_string3 = 'The following are some of the popular Python libraries: %s.' % (python_libraries)
print(formatted_string3) # Output: The following are some of the popular Python libraries: ['Django', 'Flask', 'NumPy', 'Mathplotlib', 'Pandas'].

# Accessing characters in a string by index

language2 = 'Python'
first_letter = language2[0]
print(first_letter) # P
second_letter = language2[1]
print(second_letter) # y
last_index = len(language2) - 1
last_letter = language2[last_index]
print(last_letter) # n

# Slicing python strings

language3 = 'Python'
first_three = language3[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language3[3:6]
print(last_three) # hon
# Another way
last_three = language3[-3:]
print(last_three)   # hon
last_three = language3[3:]
print(last_three)   # hon

# Reversing a string

greeting2 = 'Hello, World!'
print(greeting2[::-1]) # !dlroW ,olleH

# Skipping characters While slicing

language4 = 'Python'
print(language4[0:6:2]) # Pto