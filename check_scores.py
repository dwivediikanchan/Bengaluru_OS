from database.connection import get_connection


def load(table):

    conn=get_connection()

    df=conn.execute(
        f"select * from {table}"
    ).fetchdf()

    conn.close()

    return df



for table in [
    "housing",
    "metro",
    "traffic",
    "weather",
    "jobs",
    "civic"
]:

    print("\n\nTABLE:",table)

    print(load(table))