from database.connection import get_connection


conn = get_connection()


print(
    conn.execute(
        "DESCRIBE traffic"
    ).fetchall()
)


conn.close()