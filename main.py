# Create a product registration program.
# Criar um programa para registro de produtos.

list_items = []

number_items = int(input("How many items do you want to register?"))
print("")

# Loop with the number of iterations equal to the number of items.
# For each loop, add a dictionary to the list_items list,...
# ...and add the following keys to the dictionary: name, price and units.
# Fazer um loop com número de voltas igual ao número de itens.
# Para cada volta, adicionar um dicionário à lista list_items,...
# ...e adicionar ao dicionário as seguintes keys: name, price and units.
for i in range(number_items):
    list_items.append({})
    list_items[i]["name"] = input("Whats is the product name?")
    list_items[i]["price"] = input("Whats is the product price?")
    list_items[i]["units"] = input("How many units of the product?")
    print("")

# Print name, price and units of each item.
# Imprimir nome, preço e unidades de cada item.
for i2 in range(number_items):
    print("You added the item: " + list_items[i2]["name"])
    print("The price of the item " + list_items[i2]["name"] + " is: " + list_items[i2]["price"])
    print("The number of units of the item " + list_items[i2]["name"] + " is: " + list_items[i2]["units"])