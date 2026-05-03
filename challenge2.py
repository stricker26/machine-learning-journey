def get_products():
    products = [
        {"name": "Laptop", "price": 50000, "stock": 5},
        {"name": "Mouse", "price": 500, "stock": 0}
    ]

    result = []

    for product in products:
        # Price label
        if product["price"] > 1000:
            product["label"] = "Expensive"
        else:
            product["label"] = "Affordable"

        # Stock status
        if product["stock"] > 0:
            product["stock_status"] = "In Stock"
        else:
            product["stock_status"] = "Out of stock"

        result.append(product)

    return {
        "status": "success",
        "data": result
    }


print(get_products())