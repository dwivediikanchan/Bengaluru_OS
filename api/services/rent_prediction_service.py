import os
import joblib
import pandas as pd



MODEL_PATH = os.path.join(

    "ml_models",

    "rent_prediction",

    "model.pkl"

)



model = joblib.load(
    MODEL_PATH
)



FEATURES = [

    "rent_score",

    "traffic_score",

    "metro_score",

    "weather_score",

    "civic_score",

    "area_score"

]



def predict_rent(data):


    print("INPUT DATA:", data)



    df = pd.DataFrame(
        [data]
    )


    # convert numeric

    for col in FEATURES:

        if col not in df.columns:

            df[col] = 0


        df[col] = pd.to_numeric(

            df[col],

            errors="coerce"

        )



    df = df[FEATURES]



    prediction = model.predict(

        df

    )[0]



    return round(

        float(prediction),

        2

    )