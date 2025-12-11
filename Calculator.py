def calculator():
    last_result= None #sets that there is no initial last result for the first, 'none' makes it clear that last result currently has no value
    while True:
        if last_result is None: #there is no previos result, then
             first_number = float(input('Enter first number:'))
        else: #if there is a previous result, ask if they would like to use, because last result is not 'none'
            #.lower() converts all characters in a string to lowercase
            use_last = input(f"Do you want to use the last result ({last_result}) as the first number? (yes/no): ").lower()
            if use_last == 'yes':
                 first_number=last_result # if they want to use again, then first number is the last result
            else:
                first_number = float(input('Enter first number:'))
        operation = input('Enter operation:')
        second_number = float(input('Enter second number: '))
        if operation == "+":
                    last_result= first_number+second_number
                    #for all operation statements, the result is stored as the variable 'last result' for use in the next calculation
        elif operation == '-' :
                    last_result= first_number-second_number
        elif operation == '*' :
                    last_result= first_number*second_number
        elif operation == '/' :
                if second_number !=0: #prevents division by 0, ! means anything besides, so anything besides 0
                    last_result= first_number/second_number
                else:
                    print('Error. Cannot divide by zero.')
        else:
            print ('Syntax Error Has Occured')
            continue #tells it to skip over the rest
        #f string used to create formatted string where 'last_result' is replaced by its actual value
        print(f'Result: {last_result}')
        #asking if they would like to perform another
        another = input('Is there another mathematical operation you would like performed? (Yes/No): ').lower()
        if another != 'yes':
            break
calculator()
