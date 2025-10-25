import pandas as pd
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract():
    """Extract data from multiple sources."""
    logging.info("Starting extraction phase...")

    df_csv = pd.read_csv('data/combined_data.csv')
    logging.info(f"Extracted {len(df_csv)} records from CSV")

    return df_csv

def transform(df):
    """Clean and enrich data."""
    logging.info("Starting transformation phase...")

    # Drop duplicates
    df = df.drop_duplicates().copy() # Copy method used to fix warning: SettingWithCopyWarning

    # Standardize city names (capitalize)
    df['city'] = df['city'].str.title()

    # Add a new column with current timestamp
    df['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    logging.info("Transformation complete")
    return df

def load(df):
    """Save transformed data to new file."""
    output_path = 'data/processed_data.csv'
    df.to_csv(output_path, index=False)
    logging.info(f"Data successfully loaded to {output_path}")

def etl():
    """Complete ETL pipeline."""
    logging.info("=== ETL Pipeline Started ===")
    df_raw = extract()
    df_transformed = transform(df_raw)
    load(df_transformed)
    logging.info("=== ETL Pipeline Completed ===")

if __name__ == "__main__":
    etl()
