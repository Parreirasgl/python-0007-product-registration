# Create a product registration program.
# Criar um programa para registro de produtos.

list_items = []

number_items = int(input("How many items do you want to register?"))
print("")

for i in range(number_items):
    list_items.append({})
    inserted_name = input("Whats is the product name?")
    list_items[i][1] = inserted_name
    inserted_price = float(input("Whats is the product price?"))
    list_items[i][2] = inserted_price
    inserted_units = int(input("How many units of the product?"))
    list_items[i][3] = inserted_units
    print("")

for i2 in range(number_items):
    print(f"You added the item: {list_items[i2][1]}")
    print(f"The price of the item {list_items[i2][1]} is: {list_items[i2][2]}")
    print(f"The number of units of the item {list_items[i2][1]} is: {list_items[i2][3]}")