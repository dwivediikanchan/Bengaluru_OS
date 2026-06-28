import streamlit as st


from ai_engine.decision_engine import BengaluruDecisionEngine

from database.connection import get_connection

import pandas as pd





st.title(

    "🏙 Bengaluru Area Recommendation"

)





@st.cache_data
def load_data():

    conn = get_connection()


    housing = conn.execute(
        "SELECT * FROM housing"
    ).fetchdf()


    metro = conn.execute(
        "SELECT * FROM metro"
    ).fetchdf()


    traffic = conn.execute(
        "SELECT * FROM traffic"
    ).fetchdf()


    weather = conn.execute(
        "SELECT * FROM weather"
    ).fetchdf()


    jobs = conn.execute(
        "SELECT * FROM jobs"
    ).fetchdf()


    civic = conn.execute(
        "SELECT * FROM civic"
    ).fetchdf()


    conn.close()


    return housing, metro, traffic, weather, jobs, civic





housing, metro, traffic, weather, jobs, civic = load_data()





engine = BengaluruDecisionEngine(

    housing,

    metro,

    traffic,

    weather,

    jobs,

    civic

)





salary = st.number_input(

    "Monthly Salary",

    min_value=10000,

    value=60000

)




rent_percentage = st.slider(

    "Rent Budget %",

    20,

    60,

    40

)





if st.button("Recommend"):



    result = engine.recommend_area(

        "Best area to live",

        [

            "Low Rent",

            "Metro"

        ]

    )



    df = pd.DataFrame(result)



    st.dataframe(

        df,

        use_container_width=True

    )