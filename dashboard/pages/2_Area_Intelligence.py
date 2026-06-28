import sys
import os



sys.path.insert(

    0,

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../"

        )

    )

)



import streamlit as st
import requests
import pandas as pd



from visualizations.area_charts import show_area_chart




st.title(

    "🏙️ Bengaluru Area Intelligence"

)



API_URL = (

    "http://127.0.0.1:8000/api/area-intelligence"

)



try:


    response = requests.get(

        API_URL

    )



    data = response.json()



    if data:



        df = pd.DataFrame(

            data

        )



        st.subheader(

            "📍 Area Performance"

        )



        st.dataframe(

            df,

            use_container_width=True

        )



        show_area_chart(

            data

        )



    else:


        st.warning(

            "No area data available"

        )



except Exception as e:


    st.error(e)