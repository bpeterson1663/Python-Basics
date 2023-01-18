i = 0
while i < 50:
    i += 1
    print(i)
else:
    print('done with loop')
    
while True:
    response = input('say something: ')
    if response == 'bye':
        print('goodbye')
        break
    