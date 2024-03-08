shopping_list = []
while True:
    item = input("Enter item for shopping list: ")
    if not item:
        break
    shopping_list.append(item)
print("shpping list :\n",shopping_list)