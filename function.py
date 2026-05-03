# Step 1: Basic Function
def greet(name):
    return f"Hello, {name}"

print(greet("jonas"))

# Step 2: API like function
def get_products():
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 500}
    ]

    return products

response = get_products()
print(response)