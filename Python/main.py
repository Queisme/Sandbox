# This my first python program

# print('OoO Yummy, yummy pizza!')
# print('It is so delicious')

#variables - Strings, integers, floats, booleans
# full_name = 'Que Code'
# age = 45
# gpa = 3.8
# is_student = False

# print(f'Hello {full_name}') #Hello Que Code
# print(f'{full_name}') #Que Code

# print(f'You are {age} years old')
# print(f"Your gpa is {gpa}")
# print(f'Are you a student? {is_student}')

# if statement
# if is_student:
#   print('You are  student')
# else:
#   print('You are not a student')

# arithmetic

# + addition 
# - subtraction
# * multiplication
# / division (returns a float)
# // integer division (returns an integer)
# % remainder

# friends = 5

# friends += 1 #6
# friends -= 1 #5
# friends *= 2 #10
# friends /= 2 #5.0
# friends //= 3 #3

# friendsNow = 10

# remainingFriends = friendsNow % 3

# print(remainingFriends) #1

# Typecasting = the process of converting a variable from one data type to another. str(), int(), float(), bool()

name = 'Que Code'
age = 103
gpa = 4.0
is_student = False

# type(name) #returns nothing. Needs to be printed.
# print(type(name)) # <class 'str'>
# print(type(age)) # <class 'int'>
# print(type(gpa)) # <class 'float'>
# print(type(is_student)) # <class 'bool'>

# gpa = int(gpa)

# print(gpa) #4
# print(type(gpa)) # <class 'int'>

# age = float(age)

# print(age) #103.0
# print(type(age)) # <class 'float'>

# age = str(age)

# print(age) #103
# print(type(age)) # <class 'str'>

# User input

# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) #int() changes age from string to integer

# # User input is always a string

# print(f'Hello {name}!')
# print(f'You are {age} years old.')
# print(type(age))

# if statements = execute some code only if a condition is True (if, elif, else)

# age = int(input('Enter your age: '))

# if age >= 18:
#   print('You are an adult.')
# elif age < 0:
#   print('Is your name Benjamin Button?')
# elif age == 0:
#   print('Is today your birthday?')
# else:
#   print('You are a baby.')

# Logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

# temp = 36
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#   print('The outdoor event is cancelled')
# else:
#   print('The outdoor event is still scheduled')

# temp = 27
# is_sunny = True

# if temp >= 28 and is_sunny:
#   print('It is hot outside')
#   print('It is sunny')
# elif temp <=0 and is_sunny:
#   print('It is cold outside')
#   print('It is sunny')
# elif 28 > temp > 0 and is_sunny:
#   print('It is warm outside')
#   print('It is sunny')

# while loop = used to repeat a block of code as long as a condition remains 'True' we re-check the condition at the end of the loop

# name = input('Enter your name: ')

# while name == '':
#   name = input('Enter your name: ')

# age = int(input('Enter your age: '))

# while age < 0:
#   print("Age can't be less than 0")
#   age = int(input('Enter your age: '))

# print(f'Hello {name}!')
# print(f'You are {age} years old')

# for loops = used to iterate over a sequence (string, list, tuple, set)
#             repeat a block of code an exact amount of times

# for i in range(1, 11): #first number is inclusive, second exclusive
#   print(i)

# name = "Que Code"

# for letter in name:
#   print(letter, end=" ")

# import time

# for i in range (10, 0, -1):
#   print(i)
#   time.sleep(1)

# print('Happy New Year!')

# Lists, Tuples, and Sets

# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remove), unordered, NO duplicates, best for membership testing

# Lists

# fruits = ['apple', 'orange', 'banana', 'coconut']

# print(fruits[0]) #apple
# print(fruits[1]) #orange

# fruits[0] = 'pineapple'
# fruits[3] = 'mango'

# fruits.append('mango') #adds mango to the end
# fruits.remove('banana') #removes banana
# fruits.pop(0) #removes item at index indicated
# fruits.clear() #removes every item from your list

# for fruit in fruits:
#   print(fruit, end=' ')

# Tuples

# fruits = ('apple', 'orange', 'banana', 'coconut') #Tuples can't be changed. Periodt.

# Sets

# fruits = {'apple', 'orange', 'banana', 'coconut'} #can add and remove elements, but can't replace any elements in it because they are unordered

# # fruits.add('mango') #adds mango to the set even if the index of it isn't static
# fruits.remove('coconut') #removes coconut
# fruits.clear() #works too
# will not read or print duplicates

# for fruit in fruits:
#   print(fruit, end=' ') #list order changes each time it's printed

# fruit = input('Enter a fruit to search for: ')

# if fruit in fruits:
#   print(f'{fruit} was found')
# else:
#   print(f'no {fruit} here')
