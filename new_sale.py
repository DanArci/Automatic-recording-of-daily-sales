from request_number import request_number
from request_alpha import request_alpha

sales = []
sale = {
    "name": "",
    "quantity": 0,
    "price": 0.0    
}

def new_sale():
    sale["name"] = request_alpha("Enter the name of the product: ")
    sale["quantity"] = request_number("Enter the quantity of the product: ", "int")
    sale["price"] = request_number("Enter the price of the product: ", "float")
    sales.append(sale)