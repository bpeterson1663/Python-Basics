my_list = [char for char in 'hello']

print(my_list)


my_list4 = [num**2 for num in range(0,10) if num % 2 == 0]
print(my_list4)

my_set = {num**2 for num in range(0,10) if num % 2 ==0}
print(my_set)

simple_dict = {
    'a': 1,
    'b': 2,
}
my_dict = {key: value**2 for key,value in simple_dict.items()}

print(my_dict)


some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

duplicates = list(set([val for val in some_list if some_list.count(val) > 1]))
print(duplicates)

