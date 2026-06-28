import pandas as pd
import os
import sys


ROOT = os.path.abspath(
    os.path.dirname(__file__)
)

sys.path.append(ROOT)


from database.connection import get_connection



def check_weather():

    conn = get_connection()


    df = conn.execute(
        "SELECT * FROM weather"
    ).fetchdf()


    conn.close()


    return df



weather = check_weather()



print("Weather Data Loaded Successfully")


print("--------------------------------")


print(weather)



print("--------------------------------")


print("Columns:")


print(weather.columns.tolist())