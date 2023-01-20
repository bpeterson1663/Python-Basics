from random import randint

# generate a nmber 1~10
answer = randint(1, 10)

# input from user
# check that input is a number 1~10
while True:
    try:
        guess = int(input("guess a number 1~10: "))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print("1~10 please")
    except ValueError:
        print('please enter a number')
        continue

# check if number is the right guess.  ask again