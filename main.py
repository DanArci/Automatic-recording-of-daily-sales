#Required imports
from welcome import welcome
from options_menu import select_option
from new_sale import new_sale
from finish import finish
from check_current_registration import check_current_registration
from new_sale import sales #<------List import

option = 1 #<------Variable declaration

welcome() #<------Welcome function

while option == 1 or option == 2: #<------Main loop

    option = select_option() #<------Option selection
 
    if option == 1: #<------Option execution
        new_sale()
    elif option == 2:
        check_current_registration(sales)     
    elif option == 3:
        finish(sales)
    else:
        print("Invalid option")
        option = 1