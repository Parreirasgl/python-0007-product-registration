# Create a product registration program.
# Criar um programa para registro de produtos.

list_items = []

number_items = int(input("How many items do you want to register?"))

for i in range(number_items):
    list_items.append({})
    inserted_name = input("Whats is the product name?")
    list_items[i]["name"] = inserted_name
    inserted_price = input("Whats is the product price?")
    list_items[i]["price"] = inserted_price
    inserted_units = input("How many units of the product?")
    list_items[i]["units"] = inserted_units

print(list_items)
