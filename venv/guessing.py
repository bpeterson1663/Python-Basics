from random import randint


def run_guess(user_guess, generator_answer):
    if 0 < user_guess < 11:
        if user_guess == generator_answer:
            print('you are a genius')
            return True
    else:
        print('please 1~10')
        return False


# generate a number 1- 10
if __name__ == '__main__':
    answer = randint(1, 10)
    # get input from user?
    # check that input is a number !~10
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
    # check if number is the right guess. Otherwise ask again.
