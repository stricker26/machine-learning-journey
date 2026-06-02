import pandas as pd

df = pd.read_csv("data/salaries.csv")

# Data Preparation
print(df.head())
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())