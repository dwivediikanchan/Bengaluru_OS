import streamlit as st
import pandas as pd



def show_rent_chart(data):


    df = pd.DataFrame(data)



    if df.empty:

        st.warning(
            "No rent data available"
        )

        return



    st.subheader(
        "🏠 Rent Trend Analysis"
    )


    st.bar_chart(

        df.set_index(

            "area"

        )[

            "rent"

        ]

    )