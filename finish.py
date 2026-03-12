def finish(sales_list): #<------This function shows a summary of the registration of sales and the total collected to the user
    #variable declaration
    total = 0 
    print("\n" , "=" * 24 ,"REGISTRATION SUMMARY", "=" * 24 )
    
    #This loop shows a summary of the registration of sales and the total collected to the user
    for i in range(len(sales_list)):
        x = 1 + i
        print("\n" , "-"*26 , f"REGISTRATION NUMBER {x}" , "-"*21)
        print(f"Product: {sales_list[i]['name'].upper()}\nTotal quantity sold: {sales_list[i]['quantity']}")
        total = total + (sales_list[i]['price']*sales_list[i]['quantity'])

    #This line shows the total collected and the end message to the user
    print("\n" , "-" * 20 , f"✅Total collected✅: {total}", "-" * 20 , "\n\nThanks for using our service.")

