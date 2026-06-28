from database.connection import get_connection


conn = get_connection()


result = conn.execute(
    "DESCRIBE area_score"
).fetchall()


print(result)


conn.close()