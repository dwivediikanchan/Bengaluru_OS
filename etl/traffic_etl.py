import pandas as pd
import duckdb


df = pd.read_csv(
    "data/raw/traffic/traffic.csv"
)


conn = duckdb.connect(
    "database/bengaluru.duckdb"
)


conn.execute(
    "DELETE FROM traffic"
)


conn.register(
    "temp_traffic",
    df
)


conn.execute("""
INSERT INTO traffic
SELECT *
FROM temp_traffic
""")


print(
    f"{len(df)} traffic records loaded!"
)


conn.close()