from random import randint
import sys
# generate a number 1- 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# get input from user?
# check that input is a number !~10
while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius')
                break
        else:
            print('please 1~10')
    except ValueError:
        print('please enter a number')
        continue
#check if number is the right guess. Otherwise ask again.