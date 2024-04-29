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
#While Loops
'''
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")
'''

#Guessing Game
'''
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed.")
'''

#Building the Car Game
'''
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
'''

#For Loops
'''
for item in 'Python':
    print(item)
'''
'''
for item in ['Mosh', 'John', 'Sarah']:
    print(item)
'''
'''
for item in [1, 2, 3, 4, 5]:
    print(item)
'''
'''
#for item in range(10):
#for item in range(5, 10): #start and end
for item in range(5, 10, 2): #two steps forward
    print(item)
'''
'''
prices = [10, 20, 30]
total = 0

for price in prices:
   total += price
print(f"Total: {total}")
'''

#Nested Loops
'''
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')
'''

#Challenge
'''
numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    #print('x' * x)
   
'''

#List
'''
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:4])
'''

#Find the largest number
'''
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
'''

#2D Lists
'''
[
    1 2 3
    4 5 6
    7 8 9
]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(matrix[0][1])
#matrix[0][1] = 20
#print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
'''

#List Methods
'''
numbers = [5, 2, 1, 7, 4]
#numbers.insert(0, 10)
#numbers.remove(5)
#numbers.clear()
#numbers.pop() //remove the last value from the list
#print(numbers)
#print(numbers.index(5))
#print(50 in numbers) #false - occurunces in list
#print(numbers.count(5))
#numbers.sort()
#numbers.reverse()

numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)
'''

#Exercise
'''
numbers = [1,2,1,2,3,4,5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
'''

#Tupples
'''
numbers = (1,2,3)
print(numbers[0])
'''

#Unpacking
'''
coordinates = (1, 2, 3)
#x = coordinates[1]
#y = coordinates[1]
#z = coordinates[2]

x, y, z = coordinates
print(x)
'''

#Dictionaries
'''
customer = {
    "name": "John Smith",
    "age" : 30,
    "is_verified": True
}

#print(customer["name"])
customer["name"] = "Jack Smith"
print(customer.get("birthdate", "Jan 1 1980"))
print(customer["name"])

'''

#Exercise
phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""

for ch in phone:
    output+= digits_mapping.get(ch, "!") + " "
print(output)