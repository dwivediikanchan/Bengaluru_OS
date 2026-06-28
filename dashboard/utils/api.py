from database.connection import get_connection


def get_data(table):

    conn = get_connection()

    df = conn.execute(

        f"SELECT * FROM {table}"

    ).fetchdf()


    conn.close()


    return df