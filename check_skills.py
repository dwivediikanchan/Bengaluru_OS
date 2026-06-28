from database.connection import get_connection


conn = get_connection()


print(

    conn.execute(

        "SELECT skills FROM jobs LIMIT 10"

    ).fetchall()

)


conn.close()