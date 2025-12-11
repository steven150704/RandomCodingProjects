def account_username_and_password_generator():
    username= input('Enter desired username:')
    print ('Username is' + ' ' + username)
    while True: #loop until valid password is entered
        password= input(' Enter a password:')
        if len(password) >=8 and any(char.isdigit() for char in password):
            print('Password is valid')
            print('Username is' + ' ' + username)
            print ('Password is' + ' ' +password)
            break #exit the loop if the password entered is valid
        else:
            print('Password invalid. Needs either 8 characters or 1 number. Please try again')
account_username_and_password_generator()
