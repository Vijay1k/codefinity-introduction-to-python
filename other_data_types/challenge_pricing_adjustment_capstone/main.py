grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}

eggs_details = grocery_inventory.get("Eggs")
#print(eggs_details[1])

if eggs_details[1] > 5:
    new_price = eggs_details[1] - 1
    grocery_inventory["Eggs"] = (eggs_details[0], new_price, eggs_details[2])
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
    
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:")
milk_details = grocery_inventory.get("Milk")
milk_stock = milk_details[2]
if milk_stock < 10:
    milk_stock += 20
    grocery_inventory["Milk"] = (milk_details[0], milk_details[1], milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

apple_details = grocery_inventory.get("Apples")

if apple_details[1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:")
print(grocery_inventory)
    

