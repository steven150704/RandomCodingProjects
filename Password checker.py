#defining the funtion as "password_checker"
def password_checker():
    #has to be indented because it is how heiarchy is identified in python
    #shows that it is within the funtion of passowrd checker
    #prompts the user to input their password
    #input captures and stores the varible 'password'
    password = input('Enter a password: ')
    #conditional statment that checks for two conditions
        #len(password) >= 8 checks if the lenght of the password is at least 8 characcters
            #len funtion returns the lenght of the 'password string'
            #a string is a sequence of characters in quotation marks
        #any(char.isdigit() for char in password) checks to make sure that the password contains at least one digit
            #the any() function returns true if any element in it is true
            #the char.isdigit() checks if char is a digit
            #the for char in password iterates over each character in the password string
    if  len(password) >=8 and any(char.isdigit() for char in password):
       #if both are true, print that the password is valid
        print("Password is valid  💯")
    #if not state that it is invalid 
    else: 
        print('Password invalid. Needs either 8 characters or 1 number')
#define end of function 
password_checker ()
