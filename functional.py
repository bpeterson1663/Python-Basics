from functools import reduce


# Pure Function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

# map

my_list = [1, 2, 3]


def multiply_by2_modified(item):
    return item * 2


print(list(map(multiply_by2_modified, my_list)))
print(my_list)  # my_list is unaffected


# filter

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# zip

your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]

# reduce
acc_list = [3, 4, 5]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, acc_list, 4))  # 16

# lambda expressions
lambda_list = [6, 7, 8]
print(list(map(lambda item: item * 2, lambda_list)))  # [12, 14, 16]
