import streamlit as st
import pandas as pd


from dashboard.utils.api import get_data





st.title(

    "💼 Bengaluru Jobs Intelligence"

)





try:



    # Load directly from database

    df = get_data(

        "jobs"

    )



    if not df.empty:



        st.subheader(

            "Jobs Data"

        )



        st.dataframe(

            df,

            use_container_width=True

        )





        # Salary Insights


        if "salary" in df.columns:



            st.subheader(

                "Salary Insights"

            )



            st.metric(

                "Average Salary",

                f"₹ {round(df['salary'].mean())}"

            )





        # Companies


        if "company" in df.columns:



            st.subheader(

                "Top Companies"

            )



            st.bar_chart(

                df["company"]

                .value_counts()

                .head(10)

            )





        # Locations


        if "location" in df.columns:



            st.subheader(

                "Job Locations"

            )



            st.bar_chart(

                df["location"]

                .value_counts()

                .head(10)

            )





    else:


        st.warning(

            "No jobs data available"

        )





except Exception as e:


    st.error(

        f"Error loading jobs data: {e}"

    )