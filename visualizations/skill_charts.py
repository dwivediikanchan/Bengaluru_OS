import streamlit as st
import pandas as pd



def show_skill_chart(data):


    df = pd.DataFrame(

        data

    )



    if df.empty:


        st.warning(

            "No skill data available"

        )


        return



    st.subheader(

        "🔥 Bengaluru Skill Demand Trends"

    )



    st.dataframe(

        df,

        use_container_width=True

    )



    st.bar_chart(

        df.set_index(

            "skill"

        )[

            "demand"

        ]

    )