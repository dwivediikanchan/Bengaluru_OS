import streamlit as st
import requests
import pandas as pd
import folium

from streamlit_folium import st_folium



st.title(
    "🗺 Bengaluru Intelligence Map"
)



API_URL = (

"http://127.0.0.1:8000/api/area-intelligence"

)



try:


    response = requests.get(API_URL)


    data = response.json()


    df = pd.DataFrame(data)



    # Bengaluru center

    m = folium.Map(

        location=[12.9716,77.5946],

        zoom_start=11

    )



    for _, row in df.iterrows():


        if "latitude" in df.columns and "longitude" in df.columns:


            folium.Marker(

                [

                row["latitude"],

                row["longitude"]

                ],

                popup=f"""

                Area: {row['area']}<br>

                Score: {round(row['area_score'],2)}

                """

            ).add_to(m)



    st_folium(

        m,

        width=900,

        height=600

    )



except Exception as e:


    st.error(e)