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



from genai.chatbot import ask_city_ai




st.title(

    "💬 Bengaluru City Chat"

)



st.write(

"""

Ask anything about Bengaluru:

• Best areas

• Traffic

• Metro

• Housing

• Civic issues

• Future trends

"""

)



question = st.text_input(

    "Ask Bengaluru AI"

)



if st.button(

    "Ask"

):


    if question:


        with st.spinner(

            "Analyzing Bengaluru data..."

        ):


            answer = ask_city_ai(

                question

            )



        st.success(

            answer

        )