dictionary = {
    'a': 1,
    'b': 2,
    'c': {
        'x': 4
    }
}

print(dictionary['b'])
print(dictionary['c']['x'])

dictionary2 = {
    True: 'hi',
    True: 'hi again'
}

print(dictionary2[True])

print(dictionary2.get('hi', 'hello'))

