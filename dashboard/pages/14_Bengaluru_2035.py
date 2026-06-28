import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
import sys

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

sys.path.append(ROOT)

from database.connection import get_connection

st.set_page_config(
    page_title="Bengaluru 2035 AI",
    page_icon="🌆",
    layout="wide"
)

st.title("🌆 Bengaluru 2035 AI")

st.markdown("""
### Bengaluru Future Simulator

Simulate how Bengaluru transforms from 2025 → 2035

using:

🚇 Metro Expansion  
💼 Jobs Growth  
🏠 Housing  
🌱 Sustainability  
🤖 AI Prediction
""")


# ==========================================================
# DATA LOADING
# ==========================================================


@st.cache_data
def load(table):

    conn = get_connection()

    df = conn.execute(
        f"SELECT * FROM {table}"
    ).fetchdf()

    conn.close()

    return df



area_df = load("area_score")
metro_df = load("metro")
housing_df = load("housing")
jobs_df = load("jobs")
traffic_df = load("traffic")
civic_df = load("civic")





# ==========================================================
# PAGE CONTROLS
# ==========================================================

st.subheader("⚙ Bengaluru 2035 Simulator")


year = st.slider(

    "Simulation Year",

    2025,

    2035,

    2030

)


area = st.selectbox(

    "Select Area",

    sorted(
        area_df.iloc[:,0].astype(str).unique()
    )

)


st.divider()



# ==========================================================
# SIMULATION ENGINE
# ==========================================================


growth = min(

    65 + ((year-2025)*3),

    100

)


metro = min(

    55 + ((year-2025)*4),

    100

)


jobs = min(

    60 + ((year-2025)*3),

    100

)


housing = min(

    58 + ((year-2025)*3),

    100

)


population = (

    14.5 +

    ((year-2025)*0.42)

)



heat_risk = min(

    45 + ((year-2025)*3),

    100

)


water_risk = min(

    40 + ((year-2025)*4),

    100

)


green_score = max(

    75 - ((year-2025)*2),

    30

)



sustainability = int(

    (

        (100-heat_risk)

        +

        (100-water_risk)

        +

        green_score

    )

    /

    3

)



# ==========================================================
# CREATE TABS
# ==========================================================


tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs([

"🌆 Bengaluru 2035 Simulator",

"🚇 Future Metro",

"💰 Investment",

"💼 Jobs 2035",

"🌱 Sustainability",

"🤖 AI Report"

])

# ==========================================================
# TAB 1
# CITY GROWTH SIMULATOR
# ==========================================================

with tab1:

    st.subheader("🏙 Bengaluru 2035 Simulator")

    st.write(
        f"AI projection for **{area}** in **{year}**"
    )

    st.divider()

    # ------------------------------------------
    # Animated Gauges
    # ------------------------------------------

    g1, g2 = st.columns(2)

    with g1:

        gauge = go.Figure(
            go.Indicator(

                mode="gauge+number",

                value=growth,

                title={"text":"Future Readiness"},

                gauge={

                    "axis":{"range":[0,100]},

                    "bar":{"color":"royalblue"},

                    "steps":[

                        {"range":[0,40],"color":"#ffcccc"},

                        {"range":[40,70],"color":"#fff2cc"},

                        {"range":[70,100],"color":"#d9ead3"}

                    ]

                }

            )
        )

        gauge.update_layout(height=350)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with g2:

        gauge2 = go.Figure(
            go.Indicator(

                mode="gauge+number",

                value=metro,

                title={"text":"Metro Coverage"},

                gauge={

                    "axis":{"range":[0,100]},

                    "bar":{"color":"green"}

                }

            )
        )

        gauge2.update_layout(height=350)

        st.plotly_chart(
            gauge2,
            use_container_width=True
        )

    st.divider()

    # ------------------------------------------
    # Growth Timeline
    # ------------------------------------------

    years = list(range(2025, year + 1))

    population_curve = []

    growth_curve = []

    metro_curve = []

    for y in years:

        diff = y - 2025

        population_curve.append(
            14.5 + diff * 0.42
        )

        growth_curve.append(
            65 + diff * 3
        )

        metro_curve.append(
            min(
                55 + diff * 4,
                100
            )
        )

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=years,

            y=population_curve,

            mode="lines+markers",

            name="Population"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=years,

            y=growth_curve,

            mode="lines+markers",

            name="Growth"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=years,

            y=metro_curve,

            mode="lines+markers",

            name="Metro"

        )

    )

    fig.update_layout(

        title="Bengaluru Growth Projection",

        height=500

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ------------------------------------------
    # AI Growth Cards
    # ------------------------------------------

    c1,c2,c3=st.columns(3)

    with c1:

        st.success(f"""

### 👥 Population

**{population:.1f} Million**

Projected urban expansion

↑ Residential demand

↑ Employment

↑ Infrastructure

""")

    with c2:

        st.info(f"""

### 🚇 Metro

Coverage

**{metro}%**

Expected reduction in commute

Improved accessibility

Better public transport

""")

    with c3:

        st.warning(f"""

### 🏗 Infrastructure

Growth Score

**{growth}/100**

Commercial development

Road expansion

Smart city investment

""")

    st.divider()

    # ------------------------------------------
    # Future Readiness Score
    # ------------------------------------------

    readiness = round(

        (growth + metro + jobs + housing) / 4,

        1

    )

    st.metric(

        "🌆 Bengaluru Future Readiness",

        f"{readiness}/100"

    )

    st.progress(

        readiness / 100

    )

    st.success(

f"""
🤖 **AI Insight**

By **{year}**, **{area}** is projected to become a significantly stronger urban center due to:

- 🚇 Metro Expansion
- 💼 Employment Growth
- 🏗 Infrastructure Development
- 🏠 Housing Expansion

Overall Future Readiness:

### ⭐ {readiness}/100
"""
    )
# ==========================================================
# TAB 2
# FUTURE METRO EXPANSION SIMULATOR
# ==========================================================

with tab2:

    st.subheader("🚇 Bengaluru Future Metro Simulator")

    st.write(
        "Simulate how upcoming metro projects transform Bengaluru by 2035."
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        pink = st.toggle(
            "🌸 Pink Line",
            value=True
        )

    with c2:

        airport = st.toggle(
            "✈ Airport Line",
            value=True
        )

    with c3:

        satellite = st.toggle(
            "🛰 Satellite Town Ring",
            value=False
        )

    # ---------------------------------------
    # Metro Simulation
    # ---------------------------------------

    coverage = 55
    travel_save = 12
    property_growth = 15
    connectivity = 68

    if pink:

        coverage += 12
        travel_save += 6
        property_growth += 8
        connectivity += 10

    if airport:

        coverage += 10
        travel_save += 5
        property_growth += 7
        connectivity += 8

    if satellite:

        coverage += 8
        travel_save += 4
        property_growth += 5
        connectivity += 7

    coverage = min(coverage, 100)
    connectivity = min(connectivity, 100)

    st.divider()

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Metro Coverage",
        f"{coverage}%"
    )

    m2.metric(
        "Travel Time Saved",
        f"{travel_save} min/day"
    )

    m3.metric(
        "Property Appreciation",
        f"+{property_growth}%"
    )

    m4.metric(
        "Connectivity",
        f"{connectivity}/100"
    )

    st.divider()

    # ---------------------------------------
    # Before vs After
    # ---------------------------------------

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="2025",
            x=[
                "Coverage",
                "Connectivity",
                "Property"
            ],
            y=[
                55,
                68,
                20
            ]
        )
    )

    fig.add_trace(
        go.Bar(
            name=str(year),
            x=[
                "Coverage",
                "Connectivity",
                "Property"
            ],
            y=[
                coverage,
                connectivity,
                property_growth + 20
            ]
        )
    )

    fig.update_layout(

        barmode="group",

        height=450,

        title="Metro Expansion Impact"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------
    # Metro Network Status
    # ---------------------------------------

    st.subheader("🚉 Future Metro Network")

    network = pd.DataFrame({

        "Metro Line":[

            "Purple",

            "Green",

            "Yellow",

            "Blue",

            "Pink",

            "Airport",

            "Satellite Ring"

        ],

        "Status":[

            "Operational",

            "Operational",

            "Operational",

            "Operational",

            "Operational" if pink else "Planned",

            "Operational" if airport else "Planned",

            "Operational" if satellite else "Future Proposal"

        ]

    })

    st.dataframe(
        network,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------
    # AI Metro Insight
    # ---------------------------------------

    st.success(
f"""
## 🤖 AI Metro Intelligence

Simulation Year : **{year}**

Area : **{area}**

### Expected Benefits

✅ Metro Coverage : {coverage}%

✅ Daily Commute Reduced : {travel_save} Minutes

✅ Property Appreciation : +{property_growth}%

✅ Connectivity Score : {connectivity}/100

### AI Recommendation

With these metro expansions, Bengaluru is expected to become significantly more connected, reducing road congestion while improving employment accessibility and residential demand.

**Overall Metro Outlook : Excellent**
"""
    )
# ==========================================================
# TAB 3
# FUTURE INVESTMENT SIMULATOR
# ==========================================================

with tab3:

    st.subheader("💰 Bengaluru Future Investment Simulator")

    st.write(
        "Estimate future property growth, rental opportunity and investment potential."
    )

    st.divider()


    investment_type = st.selectbox(

        "Investment Purpose",

        [

            "🏠 Buy Property",

            "🏢 Commercial Investment",

            "🏘 Rental Income",

            "💼 Business Setup"

        ],

        key="investment_type"

    )



    budget = st.slider(

        "💰 Investment Budget (Lakhs)",

        20,

        500,

        100,

        key="budget"

    )



    area_growth = growth



    # ---------------------------------------
    # Investment Engine
    # ---------------------------------------


    future_multiplier = (

        1 + ((year - 2025) * 0.045)

    )


    appreciation = round(

        area_growth *

        future_multiplier *

        0.45,

        2

    )


    expected_value = round(

        budget *

        (1 + appreciation/100),

        2

    )


    rental = round(

        budget * 0.06,

        2

    )



    investment_score = min(

        int(

            area_growth +

            (metro/4)

        ),

        100

    )




    st.divider()



    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "Investment Score",

        f"{investment_score}/100"

    )


    c2.metric(

        "Future Appreciation",

        f"+{appreciation}%"

    )


    c3.metric(

        "Future Value",

        f"₹{expected_value} Lakhs"

    )


    c4.metric(

        "Annual Rental",

        f"₹{rental} Lakhs"

    )



    st.progress(

        investment_score/100

    )



    st.divider()



    # ---------------------------------------
    # Growth Visualization
    # ---------------------------------------


    years_list = list(

        range(

            2025,

            year+1

        )

    )


    values=[]



    current = budget



    for y in years_list:


        current = current * 1.045


        values.append(

            round(current,2)

        )



    fig = px.line(

        x=years_list,

        y=values,

        markers=True,

        title="Projected Investment Growth"

    )


    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="Value (Lakhs)"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ---------------------------------------
    # Recommendation
    # ---------------------------------------


    if investment_score >= 85:


        recommendation = "🔥 Highly Recommended"


        color = "success"


    elif investment_score >=70:


        recommendation = "📈 Good Future Potential"


        color = "info"


    else:


        recommendation = "⚠ Monitor Before Investing"


        color = "warning"




    st.subheader("🤖 AI Investment Advisor")



    if color=="success":

        st.success(

f"""
## {recommendation}


Area:

**{area}**


Reason:

✓ Strong growth index

✓ Infrastructure advantage

✓ Better future demand


Best suited for:

{investment_type}


AI Advice:

Long-term investment opportunity looks positive.
"""

        )



    elif color=="info":


        st.info(

f"""
## {recommendation}


Area:

**{area}**


Moderate-to-high future growth expected.

Consider:

✓ Connectivity

✓ Job market

✓ Development timeline

"""

        )



    else:


        st.warning(

f"""
## {recommendation}


Area:

**{area}**


Growth exists but monitor:

✓ Infrastructure

✓ Traffic

✓ Civic development

"""

        )



    st.divider()



    st.success(

f"""
🌆 Bengaluru {year} Investment Outlook


Area:

{area}


Purpose:

{investment_type}


Future Score:

{investment_score}/100


Prediction:

This location may benefit from Bengaluru's long-term urban expansion.
"""

    )
# ==========================================================
# TAB 4
# JOBS 2035 INTELLIGENCE
# ==========================================================

with tab4:

    st.subheader("💼 Bengaluru Jobs 2035 Simulator")


    st.write(
        """
Predict future career opportunities,
industries and skill demand in Bengaluru.
"""
    )


    st.divider()



    # ---------------------------------------
    # Industry Simulation
    # ---------------------------------------


    industries = pd.DataFrame({

        "Industry":[

            "Artificial Intelligence",

            "Software Engineering",

            "Data Science",

            "EV & Mobility",

            "FinTech",

            "Healthcare Tech",

            "Robotics",

            "Cloud Computing"

        ],


        "Current Demand":[

            85,

            90,

            88,

            65,

            75,

            70,

            60,

            82

        ]

    })



    industries["2035 Demand"] = (

        industries["Current Demand"]

        +

        ((year-2025)*2)

    ).clip(

        upper=100

    )




    st.subheader(

        "📈 Future Industry Demand"

    )



    fig = px.bar(

        industries,

        x="Industry",

        y="2035 Demand",

        color="2035 Demand",

        title="Job Demand Forecast 2035"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ---------------------------------------
    # Top Careers
    # ---------------------------------------


    st.subheader(

        "🔥 High Growth Careers"

    )



    top_jobs = industries.sort_values(

        "2035 Demand",

        ascending=False

    ).head(5)



    for _,row in top_jobs.iterrows():


        st.success(

f"""
### 🚀 {row['Industry']}


Future Demand:

{row['2035 Demand']}/100


Career Outlook:

★★★★★


Reason:

Technology adoption + Bengaluru expansion

"""

        )



    st.divider()



    # ---------------------------------------
    # Skill Recommendation
    # ---------------------------------------


    st.subheader(

        "🎯 Skills To Prepare For 2035"

    )


    skill1,skill2 = st.columns(2)



    with skill1:


        st.info(

"""
### 🤖 AI & Data

Recommended Skills:

✓ Machine Learning

✓ Generative AI

✓ Data Analytics

✓ Deep Learning

✓ MLOps

"""
        )


        st.info(

"""
### ☁ Cloud Technology

Skills:

✓ AWS

✓ Azure

✓ DevOps

✓ Kubernetes

"""
        )



    with skill2:


        st.success(

"""
### 💻 Software Development


Skills:

✓ Full Stack

✓ System Design

✓ Backend Engineering

✓ APIs

"""
        )


        st.success(

"""
### 🚗 Future Mobility


Skills:

✓ EV Technology

✓ IoT

✓ Robotics

✓ Automation

"""
        )



    st.divider()



    # ---------------------------------------
    # Salary Simulator
    # ---------------------------------------


    st.subheader(

        "💰 Salary Growth Simulator"

    )


    current_salary = st.slider(

        "Current Salary (LPA)",

        3,

        50,

        10,

        key="salary"

    )



    future_salary = round(

        current_salary *

        (1 + ((year-2025)*0.08)),

        2

    )



    c1,c2,c3 = st.columns(3)



    c1.metric(

        "Current",

        f"{current_salary} LPA"

    )


    c2.metric(

        "2035 Projection",

        f"{future_salary} LPA"

    )


    c3.metric(

        "Growth",

        f"+{round(((future_salary/current_salary)-1)*100)}%"

    )



    st.progress(

        min(future_salary/100,1)

    )



    st.divider()



    st.success(

f"""
## 🤖 AI Career Forecast


For Bengaluru in **{year}**:


Highest opportunity sectors:


🥇 AI & Data

🥈 Software

🥉 Cloud

🏅 EV & Robotics



Recommendation:


Build skills around emerging technologies
because Bengaluru's future economy will be
technology-driven.

"""

    )
# ==========================================================
# TAB 5
# SUSTAINABILITY & CLIMATE INTELLIGENCE
# ==========================================================

with tab5:

    st.subheader("🌱 Bengaluru 2035 Sustainability Intelligence")


    st.write(
        """
Analyze future climate impact,
environment risks and sustainability readiness.
"""
    )


    st.divider()



    # ---------------------------------------
    # Climate Simulation Engine
    # ---------------------------------------


    heat_risk = min(

        45 + ((year-2025)*3),

        100

    )


    water_risk = min(

        40 + ((year-2025)*4),

        100

    )


    green_score = max(

        75 - ((year-2025)*2),

        30

    )


    sustainability = int(

        (

            (100-heat_risk)

            +

            (100-water_risk)

            +

            green_score

        )

        /

        3

    )





    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "🌡 Heat Risk",

        f"{heat_risk}/100"

    )


    c2.metric(

        "💧 Water Stress",

        f"{water_risk}/100"

    )


    c3.metric(

        "🌳 Green Score",

        f"{green_score}/100"

    )


    c4.metric(

        "🌍 Sustainability",

        f"{sustainability}/100"

    )



    st.divider()



    # ---------------------------------------
    # Gauges
    # ---------------------------------------


    col1,col2 = st.columns(2)



    with col1:


        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=sustainability,

                title={

                    "text":

                    "Future Sustainability"

                },

                gauge={

                    "axis":

                    {

                    "range":[0,100]

                    }

                }

            )

        )


        fig.update_layout(

            height=350

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



    with col2:


        climate_df = pd.DataFrame({

            "Risk":[

                "Heat",

                "Water",

                "Green"

            ],


            "Score":[

                heat_risk,

                water_risk,

                green_score

            ]

        })



        fig2 = px.bar(

            climate_df,

            x="Risk",

            y="Score",

            color="Score",

            title="Climate Indicators"

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    st.divider()



    # ---------------------------------------
    # Future Climate Alerts
    # ---------------------------------------


    st.subheader(

        "⚠ Future Environmental Alerts"

    )


    if heat_risk >70:


        st.error(

"""
🌡 Heat Risk Increasing


Expected impact:

• Higher temperatures

• Energy demand increase

• Urban heat islands


Recommendation:

Increase green spaces and tree cover.
"""

        )


    else:


        st.success(

        "🌡 Heat conditions manageable"

        )





    if water_risk >70:


        st.warning(

"""
💧 Water Stress Alert


Possible challenges:

• Groundwater pressure

• Supply demand increase


Recommendation:

Improve water recycling.
"""

        )


    else:


        st.success(

        "💧 Water availability stable"

        )






    if green_score <50:


        st.warning(

"""
🌳 Green Infrastructure Need


Future planning should focus on:

• Parks

• Green buildings

• Sustainable transport

"""

        )


    else:


        st.success(

        "🌳 Good sustainability direction"

        )



    st.divider()



    # ---------------------------------------
    # AI Sustainability Advice
    # ---------------------------------------


    st.success(

f"""
## 🤖 AI Climate Recommendation


Bengaluru {year} Outlook


Sustainability Score:

{ sustainability }/100


Priority Actions:

✓ Expand public transport

✓ Improve water management

✓ Increase green cover

✓ Build climate-resilient infrastructure


Future City Goal:

A connected + sustainable Bengaluru.
"""

    )
# ==========================================================
# TAB 6
# AI BENGALURU 2035 REPORT
# ==========================================================

with tab6:

    st.subheader("🤖 Bengaluru 2035 AI City Report")


    st.write(
        """
A complete AI generated prediction of Bengaluru's future.
"""
    )


    st.divider()



    # ---------------------------------------
    # Overall Future Score
    # ---------------------------------------


    future_score = round(

        (

            growth +

            metro +

            jobs +

            housing +

            sustainability

        )

        /

        5,

        1

    )



    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "🌆 Future Score",

        f"{future_score}/100"

    )


    c2.metric(

        "📅 Simulation Year",

        year

    )


    c3.metric(

        "🏙 Selected Area",

        area

    )


    c4.metric(

        "🚀 Growth Status",

        "Excellent"

        if future_score>80

        else "Developing"

    )



    st.progress(

        future_score/100

    )



    st.divider()



    # ---------------------------------------
    # AI Narrative
    # ---------------------------------------


    st.subheader(

        "🌆 Future Bengaluru Story"

    )



    st.success(

f"""

## Bengaluru {year}


According to AI simulation:


**{area}** is expected to experience:


🚇 Improved Connectivity

Metro expansion will reduce travel dependency
and improve accessibility.


💼 Economic Growth

Technology, AI and new industries will increase
career opportunities.


🏠 Urban Expansion

Housing demand and infrastructure development
will continue increasing.


🌱 Sustainability Challenge

Future planning must focus on water,
green spaces and climate resilience.


Overall Future Outlook:


## ⭐ {future_score}/100


Bengaluru is expected to remain one of India's
strongest technology and innovation hubs.

"""

    )



    st.divider()



    # ---------------------------------------
    # Opportunity / Risk Split
    # ---------------------------------------


    left,right = st.columns(2)



    with left:


        st.subheader(

            "🚀 Future Opportunities"

        )


        opportunities=[

            "💼 Technology Jobs",

            "🚇 Better Mobility",

            "🏠 Real Estate Growth",

            "🤖 AI Economy",

            "🌱 Smart City Development"

        ]


        for item in opportunities:


            st.success(item)



    with right:


        st.subheader(

            "⚠ Future Challenges"

        )


        risks=[

            "🚦 Traffic Growth",

            "💧 Water Stress",

            "🏙 Urban Density",

            "🏠 Housing Affordability",

            "🌡 Climate Pressure"

        ]


        for item in risks:


            st.warning(item)



    st.divider()



    # ---------------------------------------
    # Final AI Recommendation
    # ---------------------------------------


    st.subheader(

        "🎯 AI City Recommendation"

    )


    if future_score >=85:


        message = """

🔥 HIGH POTENTIAL AREA


Recommended for:

✓ Long-term investment

✓ Career opportunities

✓ Business expansion

✓ Future living


"""

    elif future_score >=70:


        message = """

📈 DEVELOPING AREA


Recommended:

Monitor infrastructure growth
and upcoming projects.

"""

    else:


        message = """

⚠ WATCH AREA


Requires infrastructure improvement
before major expansion.

"""



    st.info(message)



    st.divider()



    st.caption(

        "🌆 Bengaluru 2035 AI | Bengaluru OS Future Intelligence"

    )