# Step 5: Combine everything (Realistic API Logic)
def get_products(min_price):
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 500}
    ]

    result = []

    for product in products:
        if product["price"] >= min_price:
            if  product["price"] > 1000:
                product["label"] = "Expensive"
            else:
                product["label"] = "Affordable"

            result.append(product)
        
    return {
        "status": "success",
        "data": result
    }

print(get_products(1000))