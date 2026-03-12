#Required imports
from request_number import request_number 

def select_option(): #<------This function shows the options menu to the user and request the option to execute
    
    #This lines show the options menu to the user 
    print("\n" , "-"*23 , "Please select an option" , "-"*22 , "\n1: Record a new sale\n2: Check active registries\n3: Finish registration and exit\n")

    #This line request the option to execute to the user and return it
    choice = request_number("Please enter your choice: ", "int")
    return choice