def finish(sales_list):
    total = 0
    print("")
    print("=" * 24 ,"REGISTRATION SUMMARY", "=" * 24 )
    for i in range(len(sales_list)):
        print("")
        print("-" * 26 , f"REGISTRATION NUMBER {i+1}", "-" * 21)
        print(f"Product: {sales_list[i]['name'].upper()}")
        print(f"Total quantity sold: {sales_list[i]['quantity']}")
        total = total + (sales_list[i]['price']*sales_list[i]['quantity'])
    print("")
    print("-" * 24 , f"Total collected: {total}", "-" * 24 )
    print("")
    print("Thanks for using our service.")  

