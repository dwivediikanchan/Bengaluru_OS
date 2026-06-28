import streamlit as st

from database.connection import get_connection

from langchain_core.documents import Document




@st.cache_resource
def load_city_documents():


    print("📚 Loading Bengaluru documents...")


    conn = get_connection()



    data = conn.execute(

        """

        SELECT *

        FROM area_score

        """

    ).fetchdf()



    conn.close()



    documents = []



    for _, row in data.iterrows():


        text = f"""

Area: {row['area']}

Rent Score: {row['rent_score']}

Traffic Score: {row['traffic_score']}

Metro Score: {row['metro_score']}

Weather Score: {row['weather_score']}

Civic Score: {row['civic_score']}

Overall Score: {row['area_score']}

"""


        documents.append(

            Document(

                page_content=text.strip()

            )

        )



    print(

        "✅ Documents loaded:",

        len(documents)

    )


    return documents