user_name = input('Enter username: ')
password = input('Enter password: ')
password_length = len(password)
password_display = '*' * password_length
print(f'{user_name}, your password {password_display} is {password_length} letters long')