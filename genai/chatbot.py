import streamlit as st

from langchain_ollama import OllamaLLM



print("🔥 FAST CHATBOT LOADED")



@st.cache_resource
def get_model():


    return OllamaLLM(

        model="llama3.2:3b",

        temperature=0.2,

        num_predict=120

    )



llm = get_model()



def ask_city_ai(question):


    prompt = f"""

You are Bengaluru OS AI Assistant.

Answer about Bengaluru.

Keep answer short and useful.

User question:

{question}

"""


    answer = llm.invoke(prompt)


    return answer