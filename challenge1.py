products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 500}
]

for product in products:
    print(product["name"] + " - " + str(product["price"]))

    if product["price"] > 1000 :
        print("Expensive")


# Recommendation more cleaner code
for product in products:
    name = product["name"]
    price = product["price"]

    print(f"{name} - {price}")

    if price > 1000:
        print("Expensive")

    print("---")