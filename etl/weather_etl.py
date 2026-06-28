import pandas as pd
import duckdb


df = pd.read_csv(
    "data/raw/weather/weather.csv"
)


conn = duckdb.connect(
    "database/bengaluru.duckdb"
)


conn.execute(
    "DELETE FROM weather"
)


conn.register(
    "temp_weather",
    df
)


conn.execute("""
INSERT INTO weather
SELECT *
FROM temp_weather
""")


print(
    f"{len(df)} weather records loaded!"
)


conn.close()