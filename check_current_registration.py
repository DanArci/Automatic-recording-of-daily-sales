def check_current_registration(sales_list): #<------This function checks the current registration of sales and shows it to the user
    print("")
    print("=" * 26 ,"ACTIVE REGISTRIES", "=" * 25 )
    for i in range(len(sales_list)): #<------This loop shows the current registration of sales to the user
        print("")
        print("-" * 26 , f"REGISTRATION NUMBER {i+1}", "-" * 21)
        print(f"Product: {sales_list[i]['name'].upper()}")
        print(f"Total quantity sold: {sales_list[i]['quantity']}")
        print(f"Price of the product: {sales_list[i]['price']}")