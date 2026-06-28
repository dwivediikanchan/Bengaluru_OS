import streamlit as st
import requests
import pandas as pd



st.title(
    "💼 Bengaluru Jobs Intelligence"
)



API_URL = (

    "http://127.0.0.1:8000/api/jobs"

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

            "Jobs Data"
        )



        st.dataframe(

            df,

            use_container_width=True

        )



        # Insights



        if "salary" in df.columns:



            st.subheader(

                "Salary Insights"
            )



            st.metric(

                "Average Salary",

                f"₹ {round(df['salary'].mean())}"
            )



        if "company" in df.columns:



            st.subheader(

                "Top Companies"
            )



            st.bar_chart(

                df["company"].value_counts().head(10)

            )



        if "location" in df.columns:



            st.subheader(

                "Job Locations"
            )



            st.bar_chart(

                df["location"].value_counts().head(10)

            )



    else:


        st.error(

            "Jobs API Error"
        )



except Exception as e:


    st.error(

        f"API not reachable: {e}"
    )