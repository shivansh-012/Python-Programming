def top_three_items(item_prices):
    # Sort the dictionary by value in descending order and get the top three items
    sorted_items = sorted(item_prices.items(), key=lambda x: x[1], reverse=True)[:3]
    return sorted_items

# Sample data
item_prices = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Get the top three items
top_items = top_three_items(item_prices)

print("Top three items:")
for item, price in top_items:
    print(f"{item}: ${price}")
