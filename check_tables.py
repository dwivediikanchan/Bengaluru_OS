from database.connection import get_connection


tables=[

"jobs",

"housing",

"metro",

"traffic",

"weather",

"civic"

]


conn=get_connection()


for t in tables:


    print("\nTABLE:",t)


    df=conn.execute(
        f"select * from {t} limit 1"
    ).fetchdf()


    print(df.columns.tolist())


conn.close()