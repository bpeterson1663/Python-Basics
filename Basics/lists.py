amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'

new_cart = amazon_cart[0:3]
# to create a copy of a list - new_cart = amazone_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# list unpacking
a, b, c, *other = [1, 2, 3, 4, 5, 6]

print(a)
print(b)
print(c)
print(other)