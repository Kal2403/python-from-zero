# NitroPC@KalTech MINGW64 ~
# $ python
# Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#  File "<python-input-0>", line 1
#    print 'hello world'
#    ^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> print('Hello World!')
# Hello World!
# >>> print(age)
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     print(age)
#           ^^^
# NameError: name 'age' is not defined
# >>> age = 25
# >>> print(age)
# 25
# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
#Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     numbers[5]
#     ~~~~~~~^^^
# IndexError: list index out of range
# >>> numbers[4]
# 5
# >>> import maths
# Traceback (most recent call last):
#   File "<python-input-8>", line 1, in <module>
#     import maths
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<python-input-10>", line 1, in <module>
#     math.PI
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
# >>> math.pi
# 3.141592653589793
# >>> users = {"name": "Kal, "age": 35, "country": "España"}
#   File "<python-input-12>", line 1
#     users = {"name": "Kal, "age": 35, "country": "España"}
#                                                         ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> users = {"name": "Kal", "age": 35, "country": "España"}
# >>> users["county"]
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     users["county"]
#     ~~~~~^^^^^^^^^^
# KeyError: 'county'
# >>> users["country"]
# 'España'
# >>> 4 + "3"
# Traceback (most recent call last):
#   File "<python-input-16>", line 1, in <module>
#     4 + "3"
#     ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 4 + int("3")
# 7
# >>> 4 + float("3")
# 7.0
# >>> from math import power
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>
#     from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>> from math import pow
# >>> pow(2, 3)
# 8.0
# >>> int("12a")
# Traceback (most recent call last):
#   File "<python-input-22>", line 1, in <module>
#     int("12a")
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: '12a'
# >>> 1/0
# Traceback (most recent call last):
#   File "<python-input-23>", line 1, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero
# >>>
