import streamlit as st


st.set_page_config(
    page_title="Bengaluru OS",
    page_icon="🏙️",
    layout="wide"
)



pages = {


    "": [

        st.Page(
            "pages/1_Home.py",
            title="🏠 Home"
        )

    ],



    "🏙️ Area Intelligence": [

        st.Page(
            "pages/2_Area_Intelligence.py",
            title="Area Intelligence"
        ),

        st.Page(
            "pages/3_Bangalore_Map.py",
            title="Bangalore Map"
        )

    ],



    "🏠 Housing": [

        st.Page(
            "pages/4_Housing.py",
            title="Housing"
        ),

        st.Page(
            "pages/5_Rent_Prediction.py",
            title="Rent Prediction"
        ),

        st.Page(
            "pages/6_Recommendation.py",
            title="Recommendation"
        )

    ],




    "🚦 City Intelligence": [

        st.Page(
            "pages/7_Traffic.py",
            title="Traffic"
        ),

        st.Page(
            "pages/8_Weather.py",
            title="Weather"
        ),

        st.Page(
            "pages/9_Civic.py",
            title="Civic"
        ),

        st.Page(
            "pages/10_Metro.py",
            title="Metro"
        ),

        st.Page(
            "pages/11_City_Chat.py",
            title="City Chat"
        )

    ],




    "💼 Career": [

        st.Page(
            "pages/12_Career.py",
            title="Career"
        )

    ],




    "📈 Future Intelligence": [

    st.Page(
        "pages/13_Future_Trends.py",
        title="📊 Future Trends"
    ),

    st.Page(
        "pages/14_Bengaluru_2035.py",
        title="🌆 Bengaluru 2035 AI"
    )

],




    "🎉 Events": [

        st.Page(
            "pages/15_Events.py",
            title="Events"
        )

    ],




    "🤖 AI": [

        st.Page(
            "pages/16_AI_Assistant.py",
            title="AI Assistant"
        ),

        st.Page(
            "pages/17_Smart_Recommendation.py",
            title="Smart Recommendation"
        )

    ]

}



pg = st.navigation(pages)



pg.run()