import os
import joblib



MODEL_PATH = os.path.join(

    "ml_models",

    "skill_forecasting",

    "model.pkl"

)



skills_df = joblib.load(

    MODEL_PATH

)



def get_skill_trends():


    data = skills_df.head(10)



    result = []



    for _, row in data.iterrows():


        result.append(

            {

                "skill": row["skill"],

                "demand": int(row["count"])

            }

        )



    return result