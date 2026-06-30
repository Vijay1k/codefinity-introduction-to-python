prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        prices[i] = prices[i] * 0.9  # 10% discount
    elif i == 1:
        prices[i] = prices[i] * 0.8  # 20% discount
    elif i == 2:
        prices[i] = prices[i] * 0.85  # 15% discount
    elif i == 3:
        prices[i] = prices[i] * 0.95  # 5% discount
    
    print(f"Updated price for item {i}: ${prices[i]:.2f}")