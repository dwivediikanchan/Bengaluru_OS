import os
import joblib
import pandas as pd



MODEL_PATH = os.path.join(

    "ml_models",

    "salary_prediction",

    "model.pkl"

)



model = joblib.load(

    MODEL_PATH

)




FEATURES = [

    "title",

    "location",

    "experience",

    "skills"

]




def predict_salary(data):


    df = pd.DataFrame(

        [data]

    )


    # create missing columns

    for col in FEATURES:


        if col not in df.columns:

            df[col] = "unknown"



    # keep correct order

    df = df[FEATURES]



    prediction = model.predict(

        df

    )[0]



    return round(

        float(prediction),

        2

    )