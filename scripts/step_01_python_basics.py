# %%
"""
Step 01 (v2): Python Basics for Data Engineering

Purpose:
- Establish coding style
- Demonstrate data-friendly Python patterns
- Set logging standards for the project
"""

import logging
from datetime import datetime

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# %%
def calculate_age(birth_year: int, current_year: int) -> int:
    """
    Calculate age from birth year.

    Why this exists:
    - Demonstrates pure function design
    - Easy to test
    - No side effects
    """
    return current_year - birth_year

# %%
def enrich_user_record(record: dict) -> dict:
    """
    Add derived fields to a user record.

    Why return a new dict:
    - Avoids mutating input
    - Safer in pipelines
    """
    enriched = record.copy()
    enriched["age"] = calculate_age(
        birth_year=record["birth_year"],
        current_year=datetime.now().year
    )
    enriched["processed_at"] = datetime.now().isoformat()
    return enriched

# %%
if __name__ == "__main__":
    logging.info("Step 01 started")

    raw_record = {
        "name": "Alice",
        "birth_year": 1995,
        "city": "Pune"
    }

    processed_record = enrich_user_record(raw_record)

    logging.info(f"Raw record: {raw_record}")
    logging.info(f"Processed record: {processed_record}")

    logging.info("Step 01 completed")
