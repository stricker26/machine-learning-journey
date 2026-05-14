import pandas as pd

# Sample dataset
data = {
    "Name": ["John", "Anna", "John", None],
    "Age": [25, None, 25, 30],
    "Salary": [50000, 60000, 50000, None]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("AFTER FILLING AGE WITH MEAN")
print(df)

df.columns = ["name", "age", "salary"]
print("\nAFTER RENAMING COLUMNS")
print(df)

df.columns = df.columns.str.strip()
print("\nAFTER STRIPPING COLUMN NAMES")
print(df)