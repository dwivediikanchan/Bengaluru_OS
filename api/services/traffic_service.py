import os
import joblib
import pandas as pd



MODEL_PATH = os.path.join(

    "ml_models",

    "traffic_forecasting",

    "model.pkl"

)



model = joblib.load(

    MODEL_PATH

)



FEATURES = [

    "area",

    "time_slot",

    "avg_speed"

]




def predict_traffic(data):


    df = pd.DataFrame(

        [data]

    )



    # Text columns

    for col in [

        "area",

        "time_slot"

    ]:


        if col not in df.columns:

            df[col] = "unknown"



    # Numeric column

    if "avg_speed" not in df.columns:

        df["avg_speed"] = 0



    df["avg_speed"] = pd.to_numeric(

        df["avg_speed"],

        errors="coerce"

    )



    df["avg_speed"] = df["avg_speed"].fillna(0)



    df = df[FEATURES]



    prediction = model.predict(

        df

    )[0]



    return prediction