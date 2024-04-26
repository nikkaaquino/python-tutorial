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