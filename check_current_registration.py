def check_current_registration(sales_list): #<------This function checks the current registration of sales and shows it to the user
    print("\n" , "=" * 26 ,"ACTIVE REGISTRIES", "=" * 25 )
    for i in range(len(sales_list)): #<------This loop shows the current registration of sales to the user 
        x = 1 + i

        #This line shows the current product names, quantitys, prices and subtotals.
        print(f"\n","-" * 26 , f"REGISTRATION NUMBER {x}", "-" * 21)
        print(f"Product: {sales_list[i]['name'].upper()}\nTotal quantity sold: {sales_list[i]['quantity']}")
        print(f"Price of the product: {sales_list[i]['price']}\nSubtotal: {sales_list[i]['quantity']*sales_list[i]['price']}")