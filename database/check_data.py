import duckdb

conn = duckdb.connect("database/bengaluru.duckdb")

result = conn.execute("SELECT * FROM jobs").fetchdf()

print(result)

conn.close()