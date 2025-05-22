######list to store products
products = []
########A function to add a product to the stocktaking

def add_product(name, price, quantity):
    for product in products: ###browse the list
        if product["name"] == name: #to see if the product name matches an item in the list"
            product["quantity"] += quantity ##if it is equal we add the quantity entered
            print("\nThe product already exists. The amount you putted has been added.")
            return
    product = {"name": name,
                "price": price,
                "quantity": quantity}
    products.append(product)
    print("\nProduct uploaded correctly..")

# Function to search a product in the inventary

def search_product(name):
    for product in products: ## search for a specific product in the stocktaking's list
        if product["name"] == name:
            print(f"\nname: {product['name']}")
            print(f"price: {product['price']}")
            print(f"quantity: {product['quantity']}")
            return
    print(f"\nUpps. The product '{name}'is Not in the stocktaking's list stored")

# Function to change the product's price 

def new_price(name, price):
    for product in products:
        if product["name"] == name:
            product["price"] = price
            print("\nPrice changed correctly")
            return
    print(f"\nUpss. The product '{name}' is NOT in the stocktaking's list stored")


# Function to delete a product from the stocktaking's list stored 
def delete_product(name):
    for product in products:
        if product["name"] == name:
            products.remove(product)
            print(f"\nProducto '{name}' deleted correctly.")
            return
    print(f"\nUpps. The product'{name}' is NOT in the stocktaking's list stored.")


# A function to show the current stocktaking
def show_stocktaking():
    if not products:
        print("\nThe stocktaking is empty.")
        return
    print(f"\n{'name':<20} {'price':<20} {'quantity':<20}")
    print("-" * 60)
    for product in products:
        print(f"{product['name']:<20} {product['price']:<20.2f} {product['quantity']:<20}")

# Función lambda para calcular el valor total del inventario
total_stocktaking= lambda: sum(product["price"] * product["quantity"] for product in products)
### main program loop (menu)
while True:
    print("WELCOME TO OUR STOCKTAKING'S SISTEM")
    print("="*60)
    print("Select the option you prefer: ")
    print("-" * 60)
    print("\n1. add a product")
    print("2. search a product")
    print("3. change a product's price")
    print("4. delete a product")
    print("5. get the total stocktaking's value")
    print("6. show the stocktaking")
    print("7. leave the program")
    while True:
        try:#####depending on the option, an action is executed
            choice = input("\nEnter the option you want to execute:")
            choice = int(choice)
            break
        except ValueError:
            print("\nUpps. Enter a valid number according to the choice you want.")

    match choice:
        case 1:
            while True:
                name = input("\nEnter the product's name: ").strip().lower()####It is validated if enter a blank space in the name
                if name == "":
                    print("\nUpss. The product's name can not be empty.")
                else:
                    break

            while True:
                try:
                    price = input("\nEnter the product's price: ")
                    price = float(price)#####It is validated that positive numbers other than 0 are entered.
                    if price <= 0:
                        print("\nUpps. The product's pice has to be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("\nUpps. The product's price has to be a valid number.") ###Validates that valid characters are entered

            while True:
                try:
                    quantity = input("\nEnter the product's quantity: ")
                    quantity = int(quantity)
                    if quantity <= 0: #######It is validated that positive numbers other than 0 are entered.
                        print("\nUpps. The product's quantity has to be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("\nUpps. The product's quantity has to be a integer number.") ###Validates that valid characters are entered

            add_product(name, price, quantity)

        case 2:
            while True:
                name = input("\nEnter the product's name you want to search in the stocktaking: ").strip().lower()
                if name == "":
                    print("\nUpps. The product's name can not be empty.") ####It is validated if enter a blank space in the name
                else:
                    break

            search_product(name)
        case 3:

            while True:
                name = input("\nEnter the product's name: ").strip().lower()
                if name == "": ####It is validated if enter a blank space in the name
                    print("\nUpps. The product's name can not be empty.")
                else:
                    break

            while True:
                try:
                    price = input("\nEnter the new product's price: ")
                    price = float(price)
                    if price <= 0: #######It is validated that positive numbers other than 0 are entered.
                        print("\nUpps. The product's price has to be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("\nUpps. The product's price has to be a valid number.") ###Validates that valid characters are entered

            new_price(name, price)

        case 4:
            while True:
                name = input("\nEnter the product's name you want delete: ").strip().lower()
                if name == "": ####It is validated if enter a blank space in the name
                    print("\nUpps. The product's name can not be empty.")
                else:
                    break

            delete_product(name)

        case 5: ##The total value of the inventory is calculated using lambda for simplicity.
            print(f"\n{'Name':<20} {'Price':<20} {'quantity':<20}")
            print("-" * 60)
            for product in products:
                print(f"{product['name']:<20} {product['price']:<20.2f} {product['quantity']:<20}")
            print(f"\nThe stocktaking's total cost is: ${total_stocktaking():.2f}")

        case 6:####show the stocktaking with the added products to improve the user experience
            show_stocktaking()

        case 7: ###exit the program

            print("\Leaving the program. See you later!")
            break

        case _: ###check that the option is in the range


            print("\nInvalid option. Select an option from 1 to 7.")
