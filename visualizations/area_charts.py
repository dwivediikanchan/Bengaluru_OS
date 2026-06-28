import streamlit as st
import pandas as pd




def show_area_chart(data):


    df = pd.DataFrame(

        data

    )


    if df.empty:


        st.warning(

            "No area data available"

        )


        return



    st.subheader(

        "🏙️ Area Intelligence Score"

    )



    st.dataframe(

        df,

        use_container_width=True

    )



    st.bar_chart(

        df.set_index(

            "area"

        )[

            "area_score"

        ]

    )




def show_score_breakdown(row):


    scores = {


        "Rent":

        row["rent_score"],


        "Traffic":

        row["traffic_score"],


        "Metro":

        row["metro_score"],


        "Weather":

        row["weather_score"],


        "Civic":

        row["civic_score"]

    }



    st.subheader(

        "📊 Score Breakdown"

    )



    st.bar_chart(

        scores

    )