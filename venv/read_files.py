try:
    with open('text.txt', mode='r+') as my_file:
        text = my_file.write('hey this is a test')
        print(my_file.readlines())
except IOError as err:
    print('IOError')
    raise err
