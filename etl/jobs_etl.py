import pandas as pd
import duckdb

# Read CSV
df = pd.read_csv("data/raw/jobs/jobs.csv")

# Connect Database
conn = duckdb.connect("database/bengaluru.duckdb")

# Clear Existing Records
conn.execute("DELETE FROM jobs")

# Register DataFrame
conn.register("temp_jobs", df)

# Insert Data
conn.execute("""
INSERT INTO jobs
SELECT * FROM temp_jobs
""")

print(f"{len(df)} records loaded successfully!")

conn.close()