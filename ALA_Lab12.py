print("Welcome to the Food Ordering System!")
print("Here is the menu:")
menu = {
    "burger": 5.50,
    "pizza": 8.00,
    "pasta": 7.00,
    "salad": 4.50,
    "soda": 1.50
}

for item, price in menu.items():
    print(f"{item}: {price:.2f}")  

order_list = []
total_cost = 0.0

while True:
    order = input("Enter the food item you want to order (or type 'done' to finish): ")  
    
    if order == 'done':
        break
    elif order in menu:
        order_list.append(order)
        total_cost += menu[order]
        print(f"{order} added to your order.")
    else:
        print("Sorry, that item is not on the menu. Please choose again.")

print("Your order:")
for item in order_list:
    print(f"{item}")

print(f"Total cost: {total_cost:.2f}")

while True:
    try:
        cash = float(input(f"\nYour total is {total_cost:.2f}. Please enter your payment: "))
        if cash >= total_cost:
            change = cash - total_cost
            print(f"Payment accepted. Your change is {change:.2f}. Thank you for your purchase!")
            break 
        else:
            print(f"Not enough cash.")
    except ValueError:
        print("ERROR: Invalid input. Please enter a valid amount.")
