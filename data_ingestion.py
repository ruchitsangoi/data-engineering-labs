import pandas as pd
import logging
from io import StringIO

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CSV Ingestion ---
csv_data = StringIO("""name,age,city
Alice,24,New York
Bob,30,London
Charlie,29,Sydney
David,35,Berlin
Eve,22,Paris""")
df_csv = pd.read_csv(csv_data)
logging.info(f"Loaded {len(df_csv)} records from CSV data")

# --- JSON Ingestion ---
json_data = [
    {"name": "Frank", "age": 33, "city": "Tokyo"},
    {"name": "Grace", "age": 27, "city": "Toronto"}
]
df_json = pd.json_normalize(json_data)
logging.info(f"Loaded {len(df_json)} records from JSON data")

# --- Excel Ingestion ---
excel_data = {
    'name': ['Helen', 'Ian', 'Jack'],
    'age': [26, 31, 28],
    'city': ['Rome', 'Madrid', 'Oslo']
}
df_excel = pd.DataFrame(excel_data)
logging.info(f"Loaded {len(df_excel)} records from simulated Excel data")

# Combine all into one DataFrame
df_combined = pd.concat([df_csv, df_excel, df_json], ignore_index=True)

logging.info(f"Combined dataset has {len(df_combined)} total records")
print(df_combined)
