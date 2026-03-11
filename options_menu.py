from request_number import request_number 
def select_option():
    print("")
    print("-" *23 ,"Please select an option", "-" *22)
    print("                        1: Record a new sale")
    print("                        2: Check active registries")
    print("                        3: Finish registration and exit")
    print("")
    choice = request_number("Please enter your choice: ", "int")
    return choice