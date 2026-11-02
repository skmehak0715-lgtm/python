#create the stores item names and stock counts
item = ['pencil','eraser','notebook','sharpener','glue']
stock_count = [5, 0, 4, 7, 9]

inventory = {item: count for item, count in zip(item, stock_count)}
print("full inventory:", inventory)

in_stock_item = [item for item in item if inventory[item] > 0]
print("full in stock:", in_stock_item)

chosen_item = input("which item do you want to buy? ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! stopping the checker.")
    exit()

prices = [9, 14, 19, 4, 17]
markup = int(input("enter the markup amount to add to every price: "))

markup_up_prices = list(map(lambda p: p + markup, prices))
print("marked up prices:", markup_up_prices)

item_index = item.index(chosen_item)
chosen_price = markup_up_prices[item_index]
print("price of", chosen_item, "after markup:", chosen_price)