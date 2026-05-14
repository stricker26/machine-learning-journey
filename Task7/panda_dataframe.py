import pandas as pd

# Create a dataframe
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": [50000, 20000, 15000, 12000],
    "Stock": [5, 10, 7, 3]
}

df = pd.DataFrame(data)

# Print dataframe
print(df)

# Print tail
print(df.tail(1))

# Print first 2 rows
print(df.head(2))

# Print info
#print(df.info())

# Print describe
#print(df.describe())

# Print shape
#print(df.shape)

# Print columns
#print(df.columns)

# Print column
#print(df["Product"])

# Print average price
print(df["Price"].mean())

# Print highest price
print(df["Price"].max())

# Print products with price > 15000
print(df[df["Price"] > 15000])