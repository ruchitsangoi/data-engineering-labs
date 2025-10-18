import pandas as pd

# Read CSV
df = pd.read_csv("sample.csv")
print("Original data:")
print(df.head())

# Drop missing values
df_clean = df.dropna()

# Save cleaned data
df_clean.to_csv("cleaned_sample.csv", index=False)
print("\nCleaned data saved as 'cleaned_sample.csv'")
