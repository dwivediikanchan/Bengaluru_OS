import pandas as pd
import sys
from pathlib import Path



# -------------------------
# Add Project Root
# -------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]


sys.path.append(
    str(PROJECT_ROOT)
)



# -------------------------
# Database Connection
# -------------------------

from database.connection import get_connection




# -------------------------
# Connect Database
# -------------------------

conn = get_connection()




# -------------------------
# Clean Data Files
# -------------------------

files = {


    "jobs":
    "data/cleaned/jobs_clean.csv",



    "housing":
    "data/cleaned/housing_clean.csv",



    "traffic":
    "data/cleaned/traffic_clean.csv",



    "weather":
    "data/cleaned/weather_clean.csv",



    "civic":
    "data/cleaned/civic_clean.csv",



    # NEW FEATURE ENGINEERING OUTPUT

    "area_score":
    "data/processed/area_intelligence_score.csv"

}




# -------------------------
# Load CSV into DuckDB
# -------------------------

for table, file in files.items():


    print(
        f"Loading {table}..."
    )



    df = pd.read_csv(
        file
    )



    conn.register(

        "temp_table",

        df

    )



    conn.execute(

        f"""

        CREATE OR REPLACE TABLE {table}

        AS

        SELECT *

        FROM temp_table

        """

    )



    print(

        f"{table} table created successfully"

    )




# -------------------------
# Close Connection
# -------------------------

conn.close()



print(
    "\nAll data loaded into DuckDB successfully"
)