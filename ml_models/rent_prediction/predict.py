import joblib
import pandas as pd



# Load trained model

model = joblib.load(

    "ml_models/rent_prediction/model.pkl"

)



def predict_rent(

    area,

    bhk,

    metro_distance

):


    input_data = pd.DataFrame(

        {

            "area":[area],

            "bhk":[bhk],

            "metro_distance":[metro_distance]

        }

    )


    prediction = model.predict(

        input_data

    )


    return round(

        prediction[0]

    )