
# print(my_file.read())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

try:    
    with open('new_file.txt', mode='r') as my_file:
        test =  my_file.write("adding to the end")
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
