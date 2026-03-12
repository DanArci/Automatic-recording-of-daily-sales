def request_number(msg,type): #<------This function request a number to the user and validate that the input is a number
    
    #Variable declaration
    terminate = 0

    #This loop request a number to the user and validate that the input is a number
    while terminate == 0:
        try:

            #This if statement validate the type of number to request to the user and save it in a variable
            if type == "int":
                number = int(input(msg))
            elif type == "float":
                number = float(input(msg))

            #This if statement validate that the number is non-negative
            #If it is negative, it shows a message to the user and continue with the loop
            if number < 0:
                print("Please enter a non-negative number.")
                continue 
            terminate = 1
            return number
        
        #This except statement catch the error if the user enter a non-numeric value and shows a message to the user
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            terminate = 0