import streamlit as st
import pandas as pd
import folium


from streamlit_folium import st_folium


from dashboard.utils.api import get_data





st.title(

    "🗺 Bengaluru Intelligence Map"

)




try:


    # Load directly from database

    df = get_data(

        "area_score"

    )



    if df.empty:


        st.warning(

            "No area data available"

        )



    else:



        # Bengaluru center

        m = folium.Map(

            location=[12.9716,77.5946],

            zoom_start=11

        )



        for _, row in df.iterrows():



            if (

                "latitude" in df.columns

                and

                "longitude" in df.columns

            ):



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


    st.error(

        f"Error loading map: {e}"

    )