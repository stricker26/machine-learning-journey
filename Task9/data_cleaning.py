import pandas as pd

# Sample dataset
data = {
    "Name": ["John", "Anna", "John", None],
    "Age": [25, None, 25, 30],
    "Salary": [50000, 60000, 50000, None]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull())

# Count missing values
print("\nTOTAL MISSING VALUES")
print(df.isnull().sum())

# Remove rows with missing values
df_clean = df.dropna()

print("\nAFTER REMOVING NULL VALUES")
print(df_clean)

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

print("\nAFTER REMOVING DUPLICATES")
print(df_clean)

# Fill missing values
df_filled = df.fillna(0)

print("\nAFTER FILLING NULL VALUES")
print(df_filled)