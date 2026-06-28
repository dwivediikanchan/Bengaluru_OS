from connection import get_connection

conn = get_connection()

conn.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER,
    title VARCHAR,
    company VARCHAR,
    location VARCHAR,
    experience VARCHAR,
    skills VARCHAR,
    salary VARCHAR
)
""")


conn.execute("""
CREATE TABLE IF NOT EXISTS housing (
    area VARCHAR,
    bhk INTEGER,
    rent INTEGER
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS cost_of_living (
    area VARCHAR,
    rent INTEGER,
    food INTEGER,
    transport INTEGER,
    utilities INTEGER,
    internet INTEGER
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS traffic (
    area VARCHAR,
    time_slot VARCHAR,
    avg_speed INTEGER,
    traffic_level VARCHAR
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS metro (
    area VARCHAR,
    nearest_station VARCHAR,
    distance_km FLOAT,
    connectivity_score INTEGER
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS weather (
    area VARCHAR,
    temperature INTEGER,
    rain_probability INTEGER,
    humidity INTEGER,
    weather_condition VARCHAR
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS civic (
    area VARCHAR,
    complaint_type VARCHAR,
    complaint_count INTEGER,
    status VARCHAR
)
""")

conn.close()