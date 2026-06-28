import pandas as pd
import duckdb

df = pd.read_csv(
    "data/raw/cost_of_living/cost_of_living.csv"
)

conn = duckdb.connect(
    "database/bengaluru.duckdb"
)

conn.execute(
    "DELETE FROM cost_of_living"
)

conn.register(
    "temp_col",
    df
)

conn.execute("""
INSERT INTO cost_of_living
SELECT *
FROM temp_col
""")

print(
    f"{len(df)} records loaded!"
)

conn.close()