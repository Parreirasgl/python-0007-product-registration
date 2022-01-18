# Create a product registration program.
# Criar um programa para registro de produtos.

list_items = []

number_items = int(input("How many items do you want to register?"))

for i in range(number_items):
    list_items.append({})
    inserted_name = input("Whats is the item's name?")
    list_items[i]["name"] = inserted_name

print(list_items)
