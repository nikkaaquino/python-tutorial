#Intro
'''
print("Nikka Aquino")
print('o----')
print(' ||||')
print('*' * 10)
'''

#Variables
'''
price = 10
rating = 4.9
name = 'Mosh'
is_published = False
print(price)
'''

#Exercise #1
'''
full_name = 'John Smith'
age = 20
is_new = True
'''

#Receiving Input
'''
name = input('What is your name? ')
print('Hi ' + name)
'''

#Exercise #2
'''
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + " likes " + color)
'''

#Type Conversion
'''
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)
'''
#Exercise #3
'''
pounds = input('Your weight in pounds: ')
kilograms = int(pounds) * 0.453592
print(kilograms)
'''

#Strings
'''
course = "Python's Course for Beginners"
python = 'Pythons Course for "Beginners"'
print(course)
print(python)
'''


# course = ''' 
# Hi John,

# This is our first email to you.

# Thank you.

# '''
# print(course)


#String with square brackets
'''
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])

name = 'Jennifer'
print(name[1:-1])
'''

#Formatted Strings
'''
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder'
print(msg)
'''

#String Methods
'''
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)
print(course.lower())
print(course.find('P'))
print(course.find('o'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print('python' in course)
print(course.title())
'''

#Arithmetic Operations
'''
print(10 / 3)
print(10 // 3) #int
print(10 % 3) #modulo
print(10 ** 3) #exponent
x = 10
# x = x + 10
# x += 3 #augmented assignment operator
x -= 3
print(x)
'''

#Operator Precedence
'''
x = (10 + 3) * 2 ** 2
print(x)

#parenthesis
# exponentiation 2 ** 3
# multiplication or division
#addition or subtruction
'''

#Math Functions
'''
x = 2.9
print(round(x))
print(abs(-2.9))

import math
print(math.ceil(2.9))
print(math.floor(2.9))
'''

#If Statements
'''
if it's a hot
    It' a hot day
    Drink plenty of water
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
'''
'''
is_hot = False
is_cold = True

if is_hot:
    print("It' a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
'''
#Exercise #4
'''
house_price = 1_000_000
is_good_credit = True

if is_good_credit:
   down_payment = house_price * 0.10
else:
    down_payment = house_price * 0.20
print(f"Down payment: ${down_payment}")
'''

#Logical Operators
'''
#AND:
#OR
#NOT

has_high_income = True
#has_good_credit = True
has_criminal_record = True

#if has_high_income and has_good_credit:
#if has_high_income or has_good_credit:
if has_high_income and not has_criminal_record:
    print("Eligble for loan")
'''

#Comparison Operators
'''
temperature = 35

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
'''
#Exercise #5
'''
name = "John Smith"

if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")
'''

#Weight Converter Program (Simple Project)
'''
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    weight_converted = weight * 0.45
    print(f'You are {weight_converted} pounds')
else:
     weight_converted = weight/0.45
     print(f'You are {weight_converted} kilograms')
'''

   




