#Required imports
from request_number import request_number
from request_alpha import request_alpha

#List and dictionary declaration
sales = []
sale = {
    "name": "",
    "quantity": 0,
    "price": 0.0    
}

def new_sale(): #<------This function registers a new sale and shows the subtotal to the user

    #This lines request the name, quantity and price of the product to the user and save it in a dictionary
    sale["name"] = request_alpha("Enter the name of the product: ")
    sale["quantity"] = request_number("Enter the quantity of the product: ", "int")
    sale["price"] = request_number("Enter the price of the product: ", "float")

    #This line shows the subtotal to the user
    print("\nSubtotal: ", sale["quantity"]*sale["price"], "\n\nSale registered successfully✅.")
    sales.append(sale.copy()) #<------This line adds the sale to the list of sales