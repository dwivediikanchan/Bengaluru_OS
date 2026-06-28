import streamlit as st
import joblib
import os
import numpy as np




st.title(

    "🏠 AI Rent Prediction"

)





# Load model

MODEL_PATH = os.path.join(

    "ml_models",

    "rent_prediction",

    "model.pkl"

)




@st.cache_resource
def load_model():


    return joblib.load(

        MODEL_PATH

    )




model = load_model()





rent_score = st.slider(

    "Rent Score",

    0,

    100,

    80

)



traffic_score = st.slider(

    "Traffic Score",

    0,

    100,

    70

)



metro_score = st.slider(

    "Metro Score",

    0,

    100,

    90

)



weather_score = st.slider(

    "Weather Score",

    0,

    100,

    85

)



civic_score = st.slider(

    "Civic Score",

    0,

    100,

    75

)



area_score = st.slider(

    "Area Score",

    0,

    100,

    88

)





if st.button(

    "Predict Rent"

):


    input_data = np.array(

        [[

        rent_score,

        traffic_score,

        metro_score,

        weather_score,

        civic_score,

        area_score

        ]]

    )



    prediction = model.predict(

        input_data

    )[0]



    st.success(

        f"Predicted Rent: ₹ {round(prediction)}"

    )