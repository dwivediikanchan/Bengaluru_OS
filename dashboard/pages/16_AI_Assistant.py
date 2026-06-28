import sys
import os


sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../.."

        )

    )

)



import streamlit as st


from genai.chatbot import ask_city_ai





st.set_page_config(

    page_title="Bengaluru OS AI",

    page_icon="🤖",

    layout="wide"

)




st.title(

    "🤖 Bengaluru OS AI Assistant"

)



st.markdown(

"""
Ask Bengaluru OS about:

🏙 Areas  
🚦 Traffic  
🌦 Weather  
🚇 Metro  
🏠 Housing  
💼 Career  
📈 Future Trends

"""

)





# Faster cache

@st.cache_data(

    ttl=600,

    show_spinner=False

)

def get_ai_response(question):


    return ask_city_ai(question)






question = st.text_input(

    "Ask anything about Bengaluru",

    placeholder="Example: Which area is best for IT jobs?"

)




if st.button(

    "🚀 Ask AI",

    use_container_width=True

):


    if question.strip():



        with st.spinner(

            "🤖 Generating answer..."

        ):



            answer = get_ai_response(

                question.strip()

            )



        st.markdown(

            "### 🤖 Bengaluru OS Response"

        )



        st.write(

            answer

        )



    else:


        st.warning(

            "Enter a question first"

        )