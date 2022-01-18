# Create a product registration program.
# Criar um programa para registro de produtos.

list_items = []

number_items = int(input("How many items do you want to register?"))
print("")

for i in range(number_items):
    list_items.append({})
    list_items[i]["name"] = input("Whats is the product name?")
    list_items[i]["price"] = input("Whats is the product price?")
    list_items[i]["units"] = input("How many units of the product?")
    print("")

for i2 in range(number_items):
    print("You added the item: " + list_items[i2]["name"])
    print("The price of the item " + list_items[i2]["name"] + " is " + list_items[i2]["price"])
    print("The number of units of the item " + list_items[i2]["name"] + " is " + list_items[i2]["units"])