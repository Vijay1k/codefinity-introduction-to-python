produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for outer in groceries:
    print(outer)
    for data in outer:
        print(f"Item name: {data}")