import pandas as pd
import logging
from io import StringIO

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Try reading from an existing CSV
    df = pd.read_csv('data/sample_data.csv')
    logging.info("Loaded data from 'data/sample_data.csv'")
except FileNotFoundError:
    # Fallback: create a small sample dataset
    logging.warning("'data/sample_data.csv' not found. Using sample data instead.")
    sample_csv = StringIO("""name,age,city
Alice,24,New York
Bob,30,London
Charlie,29,Sydney
David,35,Berlin
Eve,22,Paris
Ruchit,18,""")
    df = pd.read_csv(sample_csv)

# Display first few rows
print(df.head())

# Get basic info about the DataFrame
print(df.info())
print('Describe')
# Get summary statistics
print(df.describe())

# Select specific columns
print(df[['name', 'age']].head())

# Filter rows based on a condition
filtered_df = df[df['age'] > 25]
logging.info(f"Filtered {len(filtered_df)} rows where age > 25")
print(filtered_df)

# Sort the DataFrame by a column
sorted_df = df.sort_values('age', ascending=False)
logging.info("Sorted DataFrame by 'age' in descending order")
print(sorted_df)
