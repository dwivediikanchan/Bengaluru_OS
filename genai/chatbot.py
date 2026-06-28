import streamlit as st

from groq import Groq



@st.cache_resource
def get_client():

    return Groq(

        api_key=st.secrets["GROQ_API_KEY"]

    )



client = get_client()



def ask_city_ai(question):


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {

                "role":"system",

                "content":
                "You are Bengaluru OS AI Assistant. Give short practical answers about Bengaluru."

            },

            {

                "role":"user",

                "content":question

            }

        ],

        temperature=0.3

    )


    return response.choices[0].message.content