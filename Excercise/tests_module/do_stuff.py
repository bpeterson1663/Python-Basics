
def add_three(num=0):
    try:
        if num:
            return int(num) + 3
        else:
            return "please enter a number"
        
    except ValueError as err:
        return err