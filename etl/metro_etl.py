import pandas as pd
import duckdb


df = pd.read_csv(
    "data/raw/metro/metro.csv"
)


conn = duckdb.connect(
    "database/bengaluru.duckdb"
)


conn.execute(
    "DELETE FROM metro"
)


conn.register(
    "temp_metro",
    df
)


conn.execute("""
INSERT INTO metro
SELECT *
FROM temp_metro
""")


print(
    f"{len(df)} metro records loaded!"
)


conn.close()