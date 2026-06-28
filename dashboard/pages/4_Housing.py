import streamlit as st
import requests
import pandas as pd



st.title(
    "🏠 Bengaluru Housing Intelligence"
)



API_URL = (

    "http://127.0.0.1:8000/api/housing"

)



try:


    response = requests.get(

        API_URL

    )


    if response.status_code == 200:


        data = response.json()


        df = pd.DataFrame(

            data

        )



        st.subheader(
            "Housing Data"
        )


        st.dataframe(

            df,

            use_container_width=True

        )



        if "rent" in df.columns:


            st.subheader(

                "Average Rent"

            )


            avg_rent = df["rent"].mean()


            st.metric(

                "Average Rent",

                f"₹ {round(avg_rent)}"

            )



    else:


        st.error(

            "Housing API Error"

        )



except Exception as e:


    st.error(

        f"API not reachable: {e}"

    )