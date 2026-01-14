# %%
"""
Step 05 (v2): Exploratory Data Analysis (EDA)

Purpose:
- Understand processed data
- Perform safe exploratory analysis
- Avoid modifying pipeline outputs
"""

import logging
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from config import PROCESSED_DATA

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

DATA_PROCESSED_FILE = PROCESSED_DATA / "processed_data.csv"

# %%
def load_processed_data(file_path: Path) -> pd.DataFrame:
    """
    Load processed data for analysis.

    Why separate function:
    - Keeps I/O isolated
    - Easier to test or replace later
    """
    logging.info(f"Loading processed data from {file_path}")
    return pd.read_csv(file_path)

# %%
def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    """
    Identify numeric columns safely.

    Why this matters:
    - Prevents invalid plots
    - Makes analysis robust
    """
    return df.select_dtypes(include="number").columns.tolist()

# %%
def plot_histograms(df: pd.DataFrame, numeric_cols: list[str]) -> None:
    """
    Plot histograms for numeric columns.
    """
    if not numeric_cols:
        logging.warning("No numeric columns available for histogram plotting")
        return

    df[numeric_cols].hist(figsize=(8, 6))
    plt.tight_layout()
    plt.show()

# %%
def plot_correlation_heatmap(df: pd.DataFrame, numeric_cols: list[str]) -> None:
    """
    Plot correlation heatmap if valid.
    """
    if len(numeric_cols) < 2:
        logging.warning("Not enough numeric columns for correlation analysis")
        return

    corr = df[numeric_cols].corr()
    plt.imshow(corr)
    plt.colorbar()
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45)
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# %%
if __name__ == "__main__":
    logging.info("Step 05 started")

    df = load_processed_data(DATA_PROCESSED_FILE)
    logging.info(f"Dataset shape: {df.shape}")

    numeric_columns = get_numeric_columns(df)
    logging.info(f"Numeric columns detected: {numeric_columns}")

    plot_histograms(df, numeric_columns)
    plot_correlation_heatmap(df, numeric_columns)

    logging.info("Step 05 completed")

# %%
