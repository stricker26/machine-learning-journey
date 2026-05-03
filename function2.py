# Step 3: Add business logic
def get_products():
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 500}
    ]

    for product in products:
        if product["price"] > 1000:
            product["label"] = "Expensive"
        else:
            product["label"] = "Affordable"

    return products

print(get_products())