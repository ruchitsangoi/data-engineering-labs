# %%
"""
Step 06 (v2): Database Load (PostgreSQL)

Purpose:
- Load processed data into PostgreSQL
- Use environment variables for credentials
- Support idempotent upserts
"""

import logging
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from config import PROCESSED_DATA

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# %%
load_dotenv()

# %%
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# %%
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# %%
DATA_FILE = PROCESSED_DATA / "processed_data.csv"

# %%
def load_processed_data(file_path: Path) -> pd.DataFrame:
    """
    Load processed CSV data.
    """
    logging.info(f"Loading processed data from {file_path}")
    return pd.read_csv(file_path)

# %%
def ensure_table_exists(conn) -> None:
    """
    Create target table if it does not exist.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        name TEXT PRIMARY KEY,
        birth_year INTEGER,
        city TEXT,
        age INTEGER
    );
    """
    conn.execute(text(create_table_sql))
    logging.info("Ensured users table exists")

# %%
def upsert_users(conn, df: pd.DataFrame) -> None:
    """
    Upsert records into PostgreSQL.
    """
    upsert_sql = """
    INSERT INTO users (name, birth_year, city, age)
    VALUES (:name, :birth_year, :city, :age)
    ON CONFLICT (name)
    DO UPDATE SET
        birth_year = EXCLUDED.birth_year,
        city = EXCLUDED.city,
        age = EXCLUDED.age;
    """

    records = df.to_dict(orient="records")

    for record in records:
        conn.execute(text(upsert_sql), record)

    logging.info(f"Upserted {len(records)} records")

# %%
def run_db_load() -> None:
    """
    Execute database load step.
    """
    logging.info("Database load started")

    df = load_processed_data(DATA_FILE)

    with engine.begin() as conn:
        ensure_table_exists(conn)
        upsert_users(conn, df)

    logging.info("Database load completed successfully")

# %%
if __name__ == "__main__":
    run_db_load()

# %%
