from database.connection import get_connection


conn=get_connection()


print(
conn.execute(
"DESCRIBE civic"
).fetchall()
)


conn.close()