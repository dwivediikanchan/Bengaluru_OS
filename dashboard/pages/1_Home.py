import streamlit as st
import plotly.graph_objects as go


st.set_page_config(

    page_title="Bengaluru OS",

    page_icon="🏙️",

    layout="wide"

)


# =====================================================
# HERO SECTION
# =====================================================


st.title("🏙 Bengaluru OS")


st.markdown(
"""
## AI Powered Bengaluru City Intelligence Platform


A unified platform that understands Bengaluru's:

🚇 Mobility

🚦 Traffic

🌦 Weather

🏛 Civic Issues

🏠 Housing

💼 Careers

📈 Future Growth


Helping citizens, businesses and planners make smarter decisions.
"""
)


st.divider()



c1,c2,c3,c4 = st.columns(4)



c1.metric(

    "AI Modules",

    "10+"

)


c2.metric(

    "City Insights",

    "Real-time"

)


c3.metric(

    "ML Models",

    "Multiple"

)


c4.metric(

    "Future Simulation",

    "2035"

)



st.divider()



# =====================================================
# ABOUT PLATFORM
# =====================================================


st.header("🌆 What is Bengaluru OS?")


st.info(
"""
Bengaluru OS is an AI-driven urban intelligence platform
designed to analyze and understand Bengaluru as a living system.

It combines:

• Data Science

• Machine Learning

• AI Recommendations

• Urban Analytics

• Predictive Intelligence


to provide insights about today's city and tomorrow's Bengaluru.
"""
)



st.divider()



# =====================================================
# PLATFORM MODULES
# =====================================================


st.header("🚀 Platform Intelligence Modules")



modules = [

("🚇 Metro Intelligence",
"Route analysis, connectivity insights and future expansion"),

("🚦 Traffic Intelligence",
"Congestion analysis, travel impact and optimization"),

("🌦 Weather Intelligence",
"Weather trends, comfort analysis and predictions"),

("🏛 Civic Intelligence",
"Public issues, complaints and infrastructure monitoring"),

("🏠 Housing Intelligence",
"Rent analysis and housing insights"),

("💼 Career Intelligence",
"Skills, jobs, salary and career planning"),

("📈 Future Intelligence",
"Bengaluru growth forecasting and 2035 simulation"),

("🎉 Events Intelligence",
"Discover Bengaluru events and experiences")

]



cols = st.columns(2)



for i,(title,desc) in enumerate(modules):

    with cols[i%2]:

        st.success(

f"""
### {title}


{desc}

"""

        )



st.divider()



# =====================================================
# AI FEATURES
# =====================================================


st.header("🤖 AI Powered Capabilities")


a,b,c = st.columns(3)



with a:

    st.info(
"""
### 🔮 Prediction


Forecast:

• Growth

• Traffic

• Weather

• Future Trends
"""
    )



with b:

    st.info(
"""
### 🎯 Recommendations


AI suggests:

• Areas

• Careers

• Events

• Investments
"""
    )



with c:

    st.info(
"""
### 🌆 Simulation


Explore:

• Bengaluru 2035

• Metro Future

• Urban Growth
"""
    )



st.divider()



# =====================================================
# HOW IT WORKS
# =====================================================


st.header("⚙ How Bengaluru OS Works")


st.write(
"""
### 1️⃣ Data Collection

City datasets from multiple domains


### 2️⃣ AI Processing

Machine Learning models analyze patterns


### 3️⃣ Intelligence Generation

Insights, predictions and recommendations


### 4️⃣ User Decisions

Users explore and make smarter choices

"""
)



st.divider()



# =====================================================
# WHY
# =====================================================


st.header("🌟 Why Bengaluru OS?")


st.success(
"""
Because Bengaluru is not just a city.

It is a continuously changing ecosystem.

Bengaluru OS helps understand:

Where the city is growing.

How people move.

Where opportunities are increasing.

What challenges are coming next.

And how Bengaluru may look in the future.
"""
)



st.divider()



# =====================================================
# FINAL CTA
# =====================================================


st.header("🚀 Explore Bengaluru")


st.write(
"""
Use the sidebar to explore different intelligence modules
and discover Bengaluru from a new perspective.
"""
)



st.caption(
"🏙 Bengaluru OS | AI Powered Urban Intelligence Platform"
)