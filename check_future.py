from database.connection import get_connection


conn=get_connection()


print(
conn.execute(
"SHOW TABLES"
).fetchall()
)


conn.close()