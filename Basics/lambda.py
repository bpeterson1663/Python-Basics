my_list = [1,2,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list)

a = [(0,2), (4,3), (10, -1), (9,9)]

a.sort(key=lambda x: x[1]) # sort by the second value in the tuple
print(a)