from database.connection import get_connection

from ai_engine.decision_engine import BengaluruDecisionEngine



def load(table):

    conn=get_connection()

    df=conn.execute(
        f"SELECT * FROM {table}"
    ).fetchdf()

    conn.close()

    print(table, df.shape)

    return df



housing=load("housing")

metro=load("metro")

traffic=load("traffic")

weather=load("weather")

jobs=load("jobs")

civic=load("civic")



engine=BengaluruDecisionEngine(

    housing,

    metro,

    traffic,

    weather,

    jobs,

    civic

)



result = engine.recommend_area()


print("RESULT")

print(result)