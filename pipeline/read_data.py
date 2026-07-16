import pandas as pd

# Read the training dataset
df = pd.read_csv("data/final/train.csv")

# Print the first 5 rows
print("First 5 rows of the dataset:\n")
print(df.head())

import pandas as pd

# Read the dataset
df = pd.read_csv("data/final/train.csv")

print("First 5 rows:")
print(df.head())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())