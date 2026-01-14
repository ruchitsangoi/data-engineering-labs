# %%
"""
Step 04 (v2): Mini ETL Pipeline

Purpose:
- Orchestrate extraction and transformation steps
- Produce a clean processed dataset
- Act as a single pipeline entry point
"""

import logging
from pathlib import Path
import pandas as pd
from config import (RAW_DATA, PROCESSED_DATA)

from step_02_extraction import (
    extract_from_csv,
    extract_from_api,
    extract_from_json,
)
from step_03_cleaning import (
    standardize_columns,
    clean_and_transform,
)

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

OUTPUT_FILE = PROCESSED_DATA / "processed_data.csv"

# %%
def run_extraction() -> list[pd.DataFrame]:
    """
    Run all extraction steps.

    Why return a list:
    - Keeps sources independent
    - Easy to add/remove sources later
    """
    logging.info("Starting extraction phase")

    dfs = [
        extract_from_csv(RAW_DATA / "users.csv"),
        extract_from_api(),
        extract_from_json(RAW_DATA / "users_nested.json"),
    ]

    logging.info("Extraction phase completed")
    return dfs

# %%
def run_transformation(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Standardize, combine, and clean extracted data.
    """
    logging.info("Starting transformation phase")

    standardized = [standardize_columns(df) for df in dfs]
    combined = pd.concat(standardized, ignore_index=True)
    cleaned = clean_and_transform(combined)

    logging.info("Transformation phase completed")
    return cleaned

# %%
def run_load(df: pd.DataFrame) -> None:
    """
    Load processed data to disk.
    """
    logging.info("Starting load phase")

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    logging.info(f"Data written to {OUTPUT_FILE}")
    logging.info("Load phase completed")

# %%
def run_pipeline() -> None:
    """
    Execute the full ETL pipeline.
    """
    logging.info("ETL pipeline started")

    extracted_dfs = run_extraction()
    processed_df = run_transformation(extracted_dfs)
    run_load(processed_df)

    logging.info("ETL pipeline completed successfully")

# %%
if __name__ == "__main__":
    run_pipeline()

# %%
