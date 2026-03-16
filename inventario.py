#name some variables tha im gonna use later
sales={}
another_product= "yes"
total_cost =0
#This is a loop for when the customer wants to enter more than one product
while another_product == "yes":
    try:
        #ask for the product name,price and quantity
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        #If a product is already registered, the new quantity is added; otherwise, the new product is added.
        if product in sales:
            sales[product]["quantity"] += quantity
        else:
            sales[product] ={"price": price,
                            "quantity": quantity}
        #Here, each product is processed and its price is multiplied by the quantity. The result is added to the total cost.
        for product in sales:
            subtotal= sales[product]["price"] * sales[product]["quantity"]
            total_cost = subtotal+total_cost
        another_product=input("do you wanna add another product (yes/no): ").lower()
        print("")
#This is a try-except block to handle the error when the user enters a non-numeric value for price or quantity.
    except ValueError:
        print("please, try again")
        continue
#Finally, the summary of the products and the total cost is printed.
print("SHOW SUMMARY")
for product in sales:
    print("product:", product)
    print("price:",sales[product]["price"])
    print("quantity:",sales[product]["quantity"])
    print("----------------------------------------")
print("total:", total_cost)