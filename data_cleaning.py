import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', None],
    'age': [24, 30, None, 35, 22, 28],
    'city': ['New York', 'London', 'Sydney', None, 'Paris', 'New York'],
    'income': [50000, 60000, 55000, None, 52000, 62000]
}
df = pd.DataFrame(data)

logging.info("Sample data loaded successfully")
print("Original Data:")
print(df)

# --- Handling Missing Values ---
# df['age'].fillna(df['age'].mean(), inplace=True)       # Replace missing age with average
df['age'] = df['age'].fillna(round(df['age'].mean()))
# df['city'].fillna('Unknown', inplace=True)             # Replace missing city with 'Unknown'
df['city'] = df['city'].fillna('Unknown')
# df['income'].fillna(df['income'].median(), inplace=True)  # Replace missing income with median
df['income'] = df['income'].fillna(df['income'].median())
logging.info("Handled missing values")

# --- Renaming Columns ---
df.rename(columns={'income': 'annual_income'}, inplace=True)
logging.info("Renamed 'income' to 'annual_income'")

# --- Changing Data Types ---
df['annual_income'] = df['annual_income'].astype(int)

# --- Creating New Columns ---
df['monthly_income'] = (df['annual_income'] / 12).round(2)
df['is_high_earner'] = df['annual_income'] > 55000
logging.info("Created derived columns")

# --- Removing Duplicates ---
df.drop_duplicates(inplace=True)

# --- Final Output ---
print("\nCleaned & Transformed Data:")
print(df)

logging.info("Data cleaning and transformation complete")
