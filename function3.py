# Step 4: Add  filtering (like request params)
def get_products(min_price):
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 500}
    ]

    filtered = []

    for product in products:
        if product["price"] >= min_price:
            filtered.append(product)

    return filtered

print(get_products(1000))