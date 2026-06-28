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



from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder

from sklearn.ensemble import RandomForestClassifier



from database.connection import get_connection





conn = get_connection()



df = conn.execute(

"""
SELECT

    area,

    time_slot,

    avg_speed,

    traffic_level


FROM traffic

"""

).fetchdf()



conn.close()



print(df.head())



df = df.fillna("unknown")



# Features

X = df[

    [

        "area",

        "time_slot",

        "avg_speed"

    ]

]



# Target

y = df["traffic_level"]



# preprocessing

preprocessor = ColumnTransformer(

    transformers=[

        (

            "cat",

            OneHotEncoder(

                handle_unknown="ignore"

            ),

            [

                "area",

                "time_slot"

            ]

        )

    ],

    remainder="passthrough"

)



model = Pipeline(

    steps=[

        (

            "preprocessor",

            preprocessor

        ),

        (

            "classifier",

            RandomForestClassifier(

                n_estimators=100,

                random_state=42

            )

        )

    ]

)



model.fit(

    X,

    y

)



joblib.dump(

    model,

    "ml_models/traffic_forecasting/model.pkl"

)



print(

    "Traffic forecasting model trained successfully"

)