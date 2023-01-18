'''Cat Module'''

class Cat:
    '''Cat Class'''
    species = 'mamal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

def oldest(*cats_age):
    '''returns oldest'''
    return max(cats_age)


cat_one = Cat('fluffy', 12)
cat_two = Cat('ginger', 33)
cat_three = Cat('bandit', 22)

print(f'The oldest cat is {oldest(cat_one.age, cat_two.age, cat_three.age)} years old')
