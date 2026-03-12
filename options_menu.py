#Required imports
from request_number import request_number 

def select_option(): #<------This function shows the options menu to the user and request the option to execute
    
    #This lines show the options menu to the user 
    print("")
    print("-" *23 ,"Please select an option", "-" *22)
    print("                        1: Record a new sale")
    print("                        2: Check active registries")
    print("                        3: Finish registration and exit")
    print("")

    #This line request the option to execute to the user and return it
    choice = request_number("Please enter your choice: ", "int")
    return choice