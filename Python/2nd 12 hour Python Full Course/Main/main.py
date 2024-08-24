# This is a comment
# That down there v is actually a python program

# print('I like yummy yummy pizza!')
# print('It is delicious')

# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings

# firstName = 'Que'
# food = 'pizza'
# email = 'que@gmail.com'

# print(firstName)
# print(f'My name is {firstName}') #f-string
# print(f'{food} is the best food.')
# print(f'My email is: {email}')

# Integers

# myNumber = 1110
# quantity = 3
# numOfStudents = 30

# print(f'This number: {myNumber} is my number.')
# print(f'You are buying {quantity} items.')
# print(f'Your class has {numOfStudents} students.')

# Floats

# price = 10.99
# gpa = 4.0
# distance = 5.5

# print(f'The price is ${price}.')
# print(f'My grade point average is: {gpa}')
# print(f'You ran: {distance}km')

# Boolean

# isStudent = False
# isHungry = False
# isDem = True

# if isStudent:
#   print('You are a student')
# else:
#   print('You are not a student')

# if isHungry:
#   print('You are hungry')
# else:
#   print('You are not hungry')

# if isDem:
#   print('The DNC was amazing, right?')
# else:
#   print('Boo. Hiss. Boo.')

# Think of 4 variables

# String - name = 'Que'
# Integer - age = 45
# Float - pi = 3.14
# Boolean isTired = True

# Typecasting = converting a variable from one data type to another
#               str(), int(), float(), bool()

# name = 'Que Code'
# age = 45
# gpa = 4.0
# isStudent = True

# gpa = int(gpa)
# age = float(age)
# age = str(age)
# name = bool(name)

# print(gpa)
# print(type(age))
# print(name) # will be True until string is empty

# input - a function that prompts user to enter data
#         always returns data as a string

# name = input('What is your name? ')
# age = int(input('How old are you? '))

# age += 1

# print(f'Hello {name}!')
# print('Happy Birthday!')
# print(f'You are {age} years old.')

# Exercise 1 - Rectangle Area Calculation
# area = width * length

# length = float(input('Enter the length of your rectangle: '))
# width = float(input('Enter the width of your rectangle: '))
# area = width * length

# print(f'The area of your rectangle is {width} * {length}: {area}cm²')

#Exercise 2 - Shopping Cart Program

# item = input('What item would you like to buy? ')
# price = float(input('What is the price? '))
# quantity = int(input('How many would you like? '))
# total = price * quantity

# print(f'You have bought {quantity} * {item}(s)')
# print(f'Your total is: ${total}')

# Madlibs game
# word game where you create a story by filling in blanks with random words

# adjective1 = input('Enter an adjective: ')
# noun1 = input('Enter a noun: ')
# adjective2= input('Enter another adjective: ')
# verb1 = input('Enter a verb ending with `ing`: ')
# adjective3 = input('Enter another adjective: ')

# print(f'Today I went to a {adjective1} zoo.')
# print(f'In an exhibit, I saw a {noun1}.')
# print(f'{noun1} was {adjective2} and {verb1}.')
# print(f'I was {adjective3}!')

# Maths

# friends = 5

# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends //= 2
# friends **= 2
# remainder = friends % 10

# print(friends)
# print(remainder)

# x = 3.14
# y = 4
# z = 5

# # a = round(x) #3
# # a = abs(y) # abs = absolute value  #4
# # a = pow(y, z) # pow = power (to the power of) #1024
# # a = max(z, x, y)
# # a = min(z, x, y)


# result = a
# print(result)

# import math 

# print(math.pi)
# print(math.e)
# result = math.sqrt(169)
# result = math.ceil(9.1) #10
# result = math.floor(9.9) #9

# print(result)

# 1st Exercise - Calculate the circumference of a circle
# C = 2πr (2 * pi * radius)

# import math

# radius = float(input('Enter the circle`s radius: '))
# circ = 2 * math.pi * radius

# print(f'Your circle`s circumference is {round(circ, 2)}cm!')

# 2nd Exercise - calculate the area of a circle
# A = πr² (pi * radius squared)

# import math

# radius = float(input('Enter the circle`s radius: '))
# area = math.pi * pow(radius, 2)

# print(f'The circle`s area is: {round(area, 2)}cm²')

# 3rd Exercise - find the hypotenuse of a right triangle
# H = sqrt(a² + b²) (The square root of a squared plus b squared)

# import math

# a = float(input('Enter side a: '))
# b = float(input('Enter side b: '))
# h = math.sqrt(pow(a, 2)+ pow(b, 2))

# print(f'The hypotenuse of your right triangle is {round(h, 2)}')

# if - do code only if condition is True; else, do something else

# age = int(input('Enter your age: '))

# if age >= 100:
#   print('You are too old to sign-up')
# elif age < 0:
#   print('Okay Benjamin Buttons')
# elif age >= 18:
#   print('You are now signed up')
# else: 
#   print('You must be 18+ to sign-up')

# response = input('Would you like food? (Y/N): ')

# if response == 'Y':
#   print('Eat then')
# else:
#   print('No soup for you!')

# name = input('Enter your name: ')

# if name == '':
#   print('You did not type in your name!')
# else:
#   print(f'Hello {name}!')

# forSale = False

# if forSale:
#   print('You are in luck')
# else:
#   print('Tough luck. You`ll get `em next time!')

# Python Calculator

# operator = input('Enter an operator (+ - * /): ')
# num1 = float(input('Enter the first number: '))
# num2 = float(input('Enter the second number: '))

# if operator == '+':
#   print(num1 + num2)
# elif operator == '-':
#   print(num1 - num2)
# elif operator == '*':
#   print(num1 * num2)
# elif operator == '/':
#   print(num1 / num2)
# else:
#   print(f'{operator} is not a valid operator')

# Python weight converter

# weight = float(input('Enter your weight: '))
# unit = input('Kilograms or Pounds? (K or L): ')

# if unit == 'K':
#   weight = weight * 2.205
#   unit = 'Lbs.'
#   print(f'Your weight is: {round(weight, 2)} {unit}')
# elif unit == 'L':
#   weight = weight / 2.205
#   unit = 'Kgs.'
#   print(f'Your weight is: {round(weight, 2)} {unit}')
# else:
#   print(f'{unit} was not valid')

# Tempurate Conversation Program

# temp = float(input("Enter the temp: "))
# unit = input('Is this temp in Celsius or Fahrenheit? (C or F): ')

# if unit == 'C':
#   convertedC = (temp * 9/5) + 32
#   print(f"{temp}°C is {round(convertedC, 2)}°F")
# elif unit == 'F':
#   convertedF = (temp - 32) * 5/9
#   print(f'{temp}°F is {round(convertedF, 2)}°C')
# else:
#   print(f'{unit} was not valid')

# logical operators = evaluate multiple conditions (or, not, and)
#                     or = at least 1 condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# or

# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#   print('Outdoor event is cancelled.')
# else:
#   print('The outdoor event is still scheduled.')

# and

# temp = 20
# is_sunny = True

# if temp >= 28 and is_sunny:
#   print('It is HOT outside.')
#   print('It is Sunny.')
# elif temp <= 0 and is_sunny:
#   print('It is COLD outside.')
#   print('It is Sunny.')
# elif 28 > temp > 0 and is_sunny:
#   print('It is WARM outside.')
#   print('It is Sunny.')

# not

# temp = 12
# is_sunny = True

# if temp >= 28 and is_sunny:
#   print('It is HOT outside.')
#   print('It is Sunny.')
# elif temp <= 0 and is_sunny:
#   print('It is COLD outside.')
#   print('It is Sunny.')
# elif 28 > temp > 0 and is_sunny:
#   print('It is WARM outside.')
#   print('It is Sunny.')
# elif temp >= 28 and not is_sunny:
#   print('It is HOT outside.')
#   print('It is NOT Sunny. It is cloudy.')
# elif temp <= 0 and not is_sunny:
#   print('It is COLD outside.')
#   print('It is NOT Sunny. It is cloudy.')
# elif 28 > temp > 0 and not is_sunny:
#   print('It is WARM outside.')
#   print('It is NOT Sunny. It is cloudy.')

# conditional expression = a one-line shortcut for the if-else statement
#                          (ternary operator)
#                          Print or assign one of 2 values based on a condition
#                          X if condition, else Y

# num = 5
# a = 6
# b = 7
# age = 12
# temp = 20
# user_role = 'user'

# print('Positive' if num > 0 else 'Negative')
# result = 'Even' if num % 2 == 0 else 'Odd'
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = 'Adult' if age >= 18 else 'Child'
# weather = 'HOT' if temp > 20 else 'COLD'

# access_level = 'Full Access' if user_role == 'admin' else 'Denied'

# print(access_level)

# String Methods

#name = input('Enter your full name: ')

#phone_number = input('Enter your phone number: ')

#result = len(name) #length of a string
#result = name.find('o') #returns the 1st occurance of a given character
#result = name.rfind('s') #find last occurance of given character
#result = name.capitalize() #capitalizes 1st letter
#result = name.upper() #capitalizes whole word
#result = name.lower() #lowercases whole word
#result = name.isdigit() #bool for if it's all numbers
#result = name.isalpha() #bool for if it's all letters
#result = phone_number.count('-')
#result = phone_number.replace('-', '')
#result = name.count('e') #counts the amount of letter you determine
#result = name.replace('e', 'i') #replaces a letter with what you determine
#print(name*3) #repeats name however many times you determine

#print(help(str)) #list of all avaliable string methods for str

# print(result)

# Exercise - validate user input 
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input('Enter your user name: ')

# if len(username) > 12:
#   print('Username too long.')
# elif not username.count(' ') == 0:
#   print('Username must not contain spaces.')
# elif not username.isalpha():
#   print('Username must not contain digits.')
# else:
#   print(f'Welcome {username}')

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = '123456789101112131415'

# print(credit_number[:4]) #1234
# print(credit_number[4:]) #56789101112131415
# print(credit_number[-1]) #5 - from the back
# print(credit_number[-2]) #1
# print(credit_number[::2]) #13579012345

# A program to get the last four digits of a credit card number

# credit_number = '123456789101112'

# last_digits = credit_number[-4:]
# print(f'XXXX-XXXX-XXXX-{last_digits}')

# # reverse characters in the string
# reversed_number = credit_number[::-1]
# print(f'Reversed credit number: {reversed_number}')

# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1110.34

# print(f'Price 1 is ${price1:+,.2f}')
# print(f'Price 2 is ${price2:+,.2f}')
# print(f'Price 3 is ${price3:+,.2f}')

# while loop = execute some code WHILE some condition remains true

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# while name == '':
#   print('You don`t have a name?')
#   name = input('Enter your name: ')

# print(f'Hellooooo, {name}!')

# while age < 0:
#   print("You didn't enter your age!")
#   age = int(input('Enter your age: '))

# print(f'You are {age} yours old!')

# food = input('Enter a food you life (q to quit): ')

# while not food == 'q':
#   print(f'You like {food}')
#   food = input('Enter another food you like (q to quit): ')
# print("Ohhhh, I'm stuffed.")

# num = int(input('Enter a number between 1 - 10: '))

# while num < 1 or num > 10:
#   print(f'{num} is not valid')
#   num = int(input('Enter a number between 1 - 10: '))

# print(f'Your number is: {num}')

# Creating a compound interest calculator in Python

# principle = 0
# rate = 0
# time = 0

# while True:
#   principle = float(input("Enter the principle amount: "))
#   if principle < 0:
#     print("Principle can't be less than zero.")
#   else:
#     break

# while True:
#   rate = float(input("Enter the interest rate: "))
#   if rate < 0:
#     print("Interest rate can't be less than zero.")
#   else:
#     break

# while True:
#   time = int(input("Enter the time in years: "))
#   if time < 0:
#     print("Time can't be less than zero.")
#   else:
#     break

# total = principle * pow((1 + rate / 100), time)
# print(f'Balance after {time} year(s): ${total:.2f}')

# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# creditCard = '1234-5678-9012-3456'

# for x in range(2, 11, 2):
#   print(x)

# for x in creditCard:
#   print(x)

# for x in range(1, 21):
#   if x == 13:
#     break
#   else: 
#     print(x)

# creating a countdown timer program

# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#   seconds = x % 60
#   minutes = int(x / 60) % 60
#   hours = int(x / 3600)
#   print(f"{hours:02}:{minutes:02}:{seconds:02}")
#   time.sleep(1)

# print("Time's up!")

# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                 inner loop:

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input('Enter a symbol to use: ')


# for x in range(rows):
#   for y in range(columns):
#     print(symbol, end='')
#   print()

# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates are OK.
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchaneable. Duplicates OK. Faster.

### List - Ordered & Changeable. Duplicates are OK.

# fruits = ['apple', 'orange', 'banana', 'coconut']

# print(fruits[::-1]) backwards

#print(dir(fruits)) #to list the different attributes and methods avaliable to a collection
#print(help(fruits)) #description of each attribute and method

# print(len(fruits)) #length of collection - 4
# print('apple' in fruits) #returns bool if values in collection - True
# print('pineapple' in fruits) # False

#fruits[0] = "grapes" #replaces 'apple'
# fruits.append('pineapple') #adds item to end of list
# fruits.remove('apple') #removes item
# fruits.insert(0, 'mango') #at what index, then value
# fruits.sort() #abc order
# fruits.reverse() #reverses list
# fruits.clear() #clears list
# print(fruits.index('apple')) #0
# print(fruits.count('banana')) #1

# for fruit in fruits:
#   print(fruit, end=" ")

### Set - unordered & immutable, but Add/Remove elements Ok. No duplicates

#fruits = {'apple', 'orange', 'banana', 'coconut'}

#print(dir(fruits)) #to list the different attributes and methods avaliable to a collection
#print(help(fruits)) #description of each attribute and method
# print(len(fruits)) #4
# print('pineapple' in fruits) #returns bool if values in collection - False

# fruits.add('pineapple') #adds element
# fruits.remove('apple') #removes element
# fruits.pop() #removes whatever is first - will be random
# fruits.clear() #clears the set

# print(fruits) #unordered - will be in any order each time printed
#for fruit in fruits:
#  print(fruit)

### Tuple - ordered and unchaneable. Duplicates OK. Faster.

#fruits = ('apple', 'orange', 'banana', 'coconut', 'coconut')
#print(dir(fruits)) - attributes & methods
#print(help(fruits))
#print(len(fruits)) #4
#print('mango' in fruits) #returns bool if values in collection = False

# print(fruits.index('banana')) #2
# print(fruits.count('coconut')) #2

#print(fruits)
# for fruit in fruits:
#   print(fruit)