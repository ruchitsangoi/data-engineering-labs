# %%
"""
Step 03 (v2): Data Cleaning & Transformation

Purpose:
- Standardize schemas across sources
- Clean and type data safely
- Create derived columns for downstream use
"""

import logging
import pandas as pd

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# %%
def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names across datasets.

    Why this exists:
    - Different sources name things differently
    - Downstream steps expect consistency
    """
    return (
        df.rename(columns={"details.birth_year": "birth_year", "details.city": "city"})
          .assign(
              name=lambda x: x["name"].str.strip(),
              city=lambda x: x["city"].str.strip()
          )
    )

# %%
def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean data and create derived columns.

    Design decisions:
    - Use chaining instead of inplace
    - Fail safely on bad numeric data
    """
    cleaned = (
        df.assign(
            birth_year=lambda x: pd.to_numeric(x["birth_year"], errors="coerce")
        )
        .dropna(subset=["birth_year"])
        .assign(
            age=lambda x: 2025 - x["birth_year"]
        )
        .astype({"age": "int"})
    )

    return cleaned

# %%
if __name__ == "__main__":
    logging.info("Step 03 started")

    # Input data (simulating outputs of Step 02)
    df_csv = pd.DataFrame([
        {"name": " Alice ", "birth_year": 1995, "city": " Pune "}
    ])

    df_api = pd.DataFrame([
        {"name": "Bob", "birth_year": "1990", "city": "Mumbai"}
    ])

    df_json = pd.DataFrame([
        {"name": "Neha", "details.birth_year": 1992, "details.city": "Chennai"}
    ])

    # Standardize
    df_csv_std = standardize_columns(df_csv)
    df_api_std = standardize_columns(df_api)
    df_json_std = standardize_columns(df_json)

    # Combine
    combined_df = pd.concat([df_csv_std, df_api_std, df_json_std], ignore_index=True)

    # Clean & transform
    final_df = clean_and_transform(combined_df)

    logging.info(f"Final record count: {len(final_df)}")
    logging.info(f"\n{final_df}")

    logging.info("Step 03 completed")

# %%
