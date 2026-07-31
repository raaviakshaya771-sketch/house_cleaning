import pandas as pd

# Load CSV
df = pd.read_csv("houseprice.csv")

print("Original Dataset")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Area"] = df["Area"].fillna(df["Area"].mean())
df["Bathrooms"] = df["Bathrooms"].fillna(df["Bathrooms"].mode()[0])
df["Price"] = df["Price"].fillna(df["Price"].mean())

print("\nCleaned Dataset")
print(df)

# Save cleaned file
df.to_csv("Cleaned_houseprice.csv", index=False)

print("\nCleaned dataset saved as Cleaned_houseprice.csv")
