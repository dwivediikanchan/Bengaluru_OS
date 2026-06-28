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

from sklearn.linear_model import LinearRegression


from database.connection import get_connection




conn = get_connection()



df = conn.execute(

"""
SELECT

    title,

    location,

    experience,

    skills,

    salary


FROM jobs

"""

).fetchdf()



conn.close()



print(df.head())



# clean data

df = df.fillna("unknown")



# Features

X = df[

    [

        "title",

        "location",

        "experience",

        "skills"

    ]

]



y = pd.to_numeric(

    df["salary"],

    errors="coerce"

)



# remove bad rows

mask = y.notna()


X = X[mask]

y = y[mask]




# Text encoding

preprocessor = ColumnTransformer(

    transformers=[

        (

            "cat",

            OneHotEncoder(

                handle_unknown="ignore"

            ),

            [

                "title",

                "location",

                "experience",

                "skills"

            ]

        )

    ]

)



model = Pipeline(

    steps=[

        (

            "preprocessor",

            preprocessor

        ),

        (

            "regressor",

            LinearRegression()

        )

    ]

)



model.fit(

    X,

    y

)



joblib.dump(

    model,

    "ml_models/salary_prediction/model.pkl"

)



print(

    "Salary prediction model trained successfully"

)