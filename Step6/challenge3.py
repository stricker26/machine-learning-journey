import numpy as np

products = np.array([500, 1200, 3000, 499])

# Multiply all prices by 1.12 (tax)
print(products * 1.12)

# Print average price
print(np.mean(products))

# Print highest price
print(np.max(products))

# Print only prices > 1000
print(products[products > 1000])

# Cleaner version of above
taxed_products = products * 1.12
average_price = np.mean(products)
highest_price = np.max(products)
expensive_products = products[products > 1000]

print("With Tax:", taxed_products)
print("Average:", average_price)
print("Highest:", highest_price)
print("Expensive Products:", expensive_products)