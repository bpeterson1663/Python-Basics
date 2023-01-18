def my_func(name='Darth Vader', age=123):
    print(f'my_func says hello, {name}')
    print(f'age: ', {age})

def sum_of_age(age1, age2):
    return age1 + age2

def add_two(num1, num2):
    def add_three(num1, num2):
        return num1 + num2 + num2
    return add_three(num1, num2)
    
my_func('Brady', 23)

my_func(age=23, name="Brady")

my_func()

print(add_two(23, 45))