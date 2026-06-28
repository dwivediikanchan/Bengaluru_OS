import streamlit as st
import requests



st.title(
    "🏠 AI Rent Prediction"
)



API_URL = (

"http://127.0.0.1:8000/api/predict-rent"

)



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


    payload = {


        "rent_score": rent_score,


        "traffic_score": traffic_score,


        "metro_score": metro_score,


        "weather_score": weather_score,


        "civic_score": civic_score,


        "area_score": area_score


    }



    try:


        response = requests.post(

            API_URL,

            json=payload

        )



        result = response.json()



        st.success(

            f"Predicted Rent: ₹ {result['predicted_rent']}"

        )



    except Exception as e:


        st.error(e)