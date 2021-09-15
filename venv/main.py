import utility
from random import random, randint, choice, shuffle
from shopping.shopping_cart import buy

print(buy('item'))

print(utility.multiply(7, 6))

print(random())
print(randint(1, 100))
print(choice([2, 4, 6, 8]))
my_list = [1, 2, 3, 4, 5, 6]
shuffle(my_list)
print(my_list)
