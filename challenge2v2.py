def transform_product(product):
    return {
        **product,
        "label": "Expensive" if product["price"] > 1000 else "Affordable",
        "stock_status": "In Stock" if product["stock"] > 0 else "Out of stock"
    }


def get_products():
    products = [
        {"name": "Laptop", "price": 50000, "stock": 5},
        {"name": "Mouse", "price": 500, "stock": 0}
    ]

    return {
        "status": "success",
        "data": [transform_product(p) for p in products]
    }

print(get_products())