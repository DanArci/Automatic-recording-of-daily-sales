#Imports for modules
from welcome import welcome
from options_menu import select_option
from new_sale import new_sale
from finish import finish
from check_current_registration import check_current_registration

#List declaration
from new_sale import sales
from new_sale import sale


#Variable declaration
option = 1

#Main code
welcome()
while option == 1 or option == 2:
    option = select_option()
    if option == 1:
        new_sale()
    elif option == 2:
        check_current_registration(sales)       
    elif option == 3:
        finish(sales)
    else:
        print("Invalid option")
        option = 1
