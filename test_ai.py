from database.connection import get_connection

from ai_engine.decision_engine import BengaluruDecisionEngine



def load(table):

    conn=get_connection()

    df=conn.execute(
        f"select * from {table}"
    ).fetchdf()

    conn.close()

    return df



engine=BengaluruDecisionEngine(

    load("housing"),

    load("metro"),

    load("traffic"),

    load("weather"),

    load("jobs"),

    load("civic")

)



print(

engine.recommend_area()

)