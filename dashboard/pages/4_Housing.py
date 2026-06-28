import streamlit as st
import pandas as pd


from dashboard.utils.api import get_data





st.title(

    "🏠 Bengaluru Housing Intelligence"

)





try:



    # Load directly from database

    df = get_data(

        "housing"

    )



    if not df.empty:



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


        st.warning(

            "No housing data available"

        )





except Exception as e:


    st.error(

        f"Error loading housing data: {e}"

    )