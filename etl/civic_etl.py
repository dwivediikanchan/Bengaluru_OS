import pandas as pd
import duckdb


df = pd.read_csv(
    "data/raw/civic/civic.csv"
)


conn = duckdb.connect(
    "database/bengaluru.duckdb"
)


conn.execute(
    "DELETE FROM civic"
)


conn.register(
    "temp_civic",
    df
)


conn.execute("""
INSERT INTO civic
SELECT *
FROM temp_civic
""")


print(
    f"{len(df)} civic records loaded!"
)


conn.close()