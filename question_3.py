
Available_Menu = {'cold_drink': 80, 'chicken_65': 200, 'kukkad_chicken': 300, 'tower': 1200}


calculate_price = lambda price, quantity: price * quantity

print("Welcome to our Restro-Bar!")
print("What would you like to have? Type 'done' to finish ordering.")

Ordered_menu = {}


while True:
    try:
        item = input("Please order: ").strip()
        if item.lower() == "done":
            break

        if item not in Available_Menu:
            raise ValueError(f"'{item}' is not available in the menu.")
        
        Quantity = int(input(f"Please tell the quantity for {item}: "))
        if Quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        Ordered_menu[item] = Quantity
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")


Total_price = 0

print("\nOrder Summary:")
for item, quantity in Ordered_menu.items():
    price = calculate_price(Available_Menu.get(item, 0), quantity)
    Total_price += price
    print(f"{item}: {quantity} x {Available_Menu[item]} = {price}")

print(f"\nThe total bill amount is: ${Total_price}\n")

# Front-end Receipt Generation
print(f"|{'_'*90}|")
print("|{:*^90}|".format(" HOTEL RECEIPT "))
print(f"|{'_'*90}|")
print(f"|{'SR No.':^10} {'ORDER name':^30} {'QUANTITY':^20} {'PRICE':>20}       |")

c = 0
for item, quantity in Ordered_menu.items():
    price = calculate_price(Available_Menu.get(item, 0), quantity)
    c += 1
    print(f"|{c:^10} {item:^30} {quantity:^20} {price:>20}       |")

print(f"|{'_'*90}|")
print(f"|{'Total':>70}{Total_price:^20}|")
print(f"|{'_'*90}|")
