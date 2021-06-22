# name = input("What is your name?")
# print("hello: " + name)

#Fundamental Data Types
#int
print(type(6))
#float
print(type(2 / 5))
print(type(2 * .333))
print(2 * .5)

print(2 ** 3) #2 to the power of 3
print(6 // 4) # 1 removes remainder
print( 6 % 4) # 2

#Math functions
print(round(3.567, 2)) # 3.57
print(abs(-20))

#variables, do not need to declare
#best practices for variables
#snake_case
#Start with lowercase or underscore
#Letters, numbers, underscores
#case sensitive
#don't overwrite keywords


user_iq = 90
a,b,c = 1,2,3 # assign values to multiple variables
print(user_iq) #90

#augmented asignment operator
some_value = 5
some_value -= 2
print(some_value) #3

long_string = '''
Multiple 
line
String

'''
print(long_string)

#string concantination only works with strings so need to convert type
print("number is " + str(5))

#Escape Sequence
weather = "It's \"kind of\" sunny with a backslash \\"
print(weather)

#Formatting strings 
age = 32
name = "Brady"
print(f'hi {name} you are {age} years old' )
bool

list
tuple
set
dict

#Classes -> custom types

#Specialized Data Types

None
print('*' * 10)
#password checker assignment
username = input('enter your username')
password = input('enter your password')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password {hidden_password} is {password_length} letters long')

#Lists
cart = ['notebooks', 'pencils', 'pens', 'staples']
print(cart[1]) # pencils

print(cart[0:2]) #notebooks, pencils
#lists are mutable
cart[0] = 'laptop'
#assigning one list to another is similar to object referencing in javascript
#create a new copy
cart2 = cart[:]

#.append, .extend, adds new items to the list do no return anything 

#pop(position) removes the item in the list, pop will return the item that was just removed

#.index returns the position

#cart.sort() or sorted(cart), sorted produces a new list
#reverse or reversed, doesnt sort but reverses the order of the items 

#list unpacking
a,b, *other = [1,2,3,4,5,6,7,8]

print(a) #1
print(b) #2
print(other) #[3,4,5,5,6,7,8]

#Dictionary
dictionary = {
  'a': 1,
  'b': 2
}
#Dictionary keys can be a number or boolean but has to be unique
print

dictionary.get('a', 'DEFAULT_VALUE')

print('a' in dictionary.keys())

dictionary.update({'a': 3}) #will create if a doesnt exist
