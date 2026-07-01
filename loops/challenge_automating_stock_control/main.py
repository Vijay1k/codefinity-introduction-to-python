# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for items in inventory.items():
    #for item_details in items:
      for i in range(1, len(items)):
          print(f"Processing {items[0]}")
          while(items[i][0] < items[i][1]):
              items[i][0] += items[i][2]

for items in inventory.values():
    if items[0]  > discount_threshold:
        items[3] = True

print(inventory)
print("Processing completed")