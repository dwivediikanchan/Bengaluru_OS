import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)


import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression

from database.connection import get_connection



conn = get_connection()



df = conn.execute(

"""
SELECT

    rent,

    rent_score,

    traffic_score,

    metro_score,

    weather_score,

    civic_score,

    area_score


FROM area_score

"""

).fetchdf()



conn.close()



print(df.head())



# Handle missing data

df = df.fillna(0)



# Features

X = df[

    [

        "rent_score",

        "traffic_score",

        "metro_score",

        "weather_score",

        "civic_score",

        "area_score"

    ]

]



# Target

y = df["rent"]



# Model

model = LinearRegression()



model.fit(

    X,

    y

)



# Save model

joblib.dump(

    model,

    "ml_models/rent_prediction/model.pkl"

)



print(
    "Rent prediction model trained successfully"
)