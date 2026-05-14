import pandas as pd

# Load CSV file
df = pd.read_csv("products.csv")

# Show first 5 rows
print(df.head())

# Show last 5 rows
print(df.tail())

# Show dataset info
print(df.info())

# Show statistics
print(df.describe())

# Show column names
print(df.columns)

# Show dataset shape (rows, columns)
print(df.shape)