import streamlit as st



def score_chart(df):


    st.bar_chart(

        df.set_index("area")["score"]

    )



def simple_chart(df, column):


    st.bar_chart(

        df[column].value_counts()

    )