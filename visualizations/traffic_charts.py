import streamlit as st
import pandas as pd



def show_traffic_chart(data):


    df = pd.DataFrame(data)



    if df.empty:

        st.warning(
            "No traffic data available"
        )

        return



    st.subheader(
        "🚦 Traffic Speed Analysis"
    )


    st.line_chart(

        df.set_index(

            "time_slot"

        )[

            "avg_speed"

        ]

    )