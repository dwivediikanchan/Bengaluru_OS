import streamlit as st
import requests



st.title(
    "🏙 Bengaluru Area Recommendation"
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


    payload = {

        "salary": salary,

        "rent_percentage": rent_percentage

    }



    response = requests.post(

        "http://127.0.0.1:8000/api/recommend",

        json=payload

    )



    if response.status_code == 200:


        data = response.json()



        st.dataframe(

            data,

            use_container_width=True

        )


    else:

        st.error(
            "API Error"
        )