# %%
"""
Step 02 (v2): Data Extraction

Purpose:
- Extract data from multiple sources
- Keep extraction logic separate from transformation
- Log only meaningful pipeline events
"""

import json
import logging
from pathlib import Path
import pandas as pd

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

DATA_RAW_DIR = Path("data/raw")

# %%
def extract_from_csv(file_path: Path) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Why this function exists:
    - Encapsulates CSV-specific logic
    - Makes future changes isolated
    """
    logging.info(f"Extracting data from CSV: {file_path}")
    return pd.read_csv(file_path)

# %%
def extract_from_api() -> pd.DataFrame:
    """
    Simulate data extraction from an API.

    Why simulated:
    - Keeps project lightweight
    - Avoids network dependency
    """
    logging.info("Extracting data from API (simulated)")

    api_response = [
        {"name": "Bob", "birth_year": 1990, "city": "Mumbai"},
        {"name": "Carol", "birth_year": 1985, "city": "Delhi"}
    ]

    return pd.DataFrame(api_response)

# %%
def extract_from_json(file_path: Path) -> pd.DataFrame:
    """
    Extract and normalize nested JSON data.

    Why json_normalize:
    - Flattens nested structures
    - Converts semi-structured → tabular
    """
    logging.info(f"Extracting data from JSON: {file_path}")

    with open(file_path, "r") as f:
        raw_json = json.load(f)

    return pd.json_normalize(raw_json)

# %%
if __name__ == "__main__":
    logging.info("Step 02 started")

    # CSV extraction
    csv_file = DATA_RAW_DIR / "users.csv"
    df_csv = extract_from_csv(csv_file)

    # API extraction
    df_api = extract_from_api()

    # JSON extraction
    json_file = DATA_RAW_DIR / "users_nested.json"
    df_json = extract_from_json(json_file)

    logging.info(f"CSV records: {len(df_csv)}")
    logging.info(f"API records: {len(df_api)}")
    logging.info(f"JSON records: {len(df_json)}")

    logging.info("Step 02 completed")

