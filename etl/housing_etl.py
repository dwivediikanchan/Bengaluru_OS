import pandas as pd
import duckdb

df = pd.read_csv(
    "data/raw/housing/housing.csv"
)

conn = duckdb.connect(
    "database/bengaluru.duckdb"
)

conn.execute(
    "DELETE FROM housing"
)

conn.register(
    "temp_housing",
    df
)

conn.execute("""
INSERT INTO housing
SELECT *
FROM temp_housing
""")

print(
    f"{len(df)} housing records loaded!"
)

conn.close()