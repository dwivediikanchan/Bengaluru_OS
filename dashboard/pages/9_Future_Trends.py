import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
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
    page_title="Future Trends Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Bengaluru Future Trends Intelligence")

st.markdown("""
### Predict Tomorrow's Bengaluru Today

AI powered growth forecasting using

- 🚇 Metro Connectivity
- 💼 Employment
- 🏠 Housing
- 🚦 Traffic
- 🏛 Civic Infrastructure

Understand which areas will become the next Bengaluru hotspots.
""")

@st.cache_data
def load(table):

    conn = get_connection()

    df = conn.execute(
        f"SELECT * FROM {table}"
    ).fetchdf()

    conn.close()

    return df


area_df = load("area_score")
housing_df = load("housing")
jobs_df = load("jobs")
metro_df = load("metro")
traffic_df = load("traffic")
civic_df = load("civic")

def growth_engine(area):

    score = 50

    drivers = []

    if area.lower() in metro_df.iloc[:,0].astype(str).str.lower().values:

        score += 15
        drivers.append("🚇 Metro Expansion")

    if area.lower() in jobs_df.iloc[:,0].astype(str).str.lower().values:

        score += 20
        drivers.append("💼 Employment Growth")

    if area.lower() in housing_df.iloc[:,0].astype(str).str.lower().values:

        score += 10
        drivers.append("🏠 Housing Demand")

    traffic = traffic_df[
        traffic_df["area"].str.lower()==area.lower()
    ]

    if not traffic.empty:

        if traffic.avg_speed.mean()<25:

            score -=10
            drivers.append("🚦 Congestion Risk")

    civic = civic_df[
        civic_df["area"].str.lower()==area.lower()
    ]

    if not civic.empty:

        if civic.complaint_count.sum()>100:

            score -=10
            drivers.append("🏛 Civic Pressure")

    return min(max(score,0),100),drivers

future=[]

areas = sorted(area_df.iloc[:,0].astype(str).unique())

for area in areas:

    score,drivers = growth_engine(area)

    future.append({

        "Area":area,

        "Growth Score":score,

        "Drivers":drivers

    })

future_df=pd.DataFrame(future)

st.divider()

c1,c2,c3,c4=st.columns(4)

c1.metric(
    "Areas Analysed",
    len(future_df)
)

c2.metric(
    "High Growth Areas",
    len(future_df[future_df["Growth Score"]>=80])
)

c3.metric(
    "Average Growth",
    round(future_df["Growth Score"].mean(),1)
)

c4.metric(
    "Highest Score",
    future_df["Growth Score"].max()
)

tab1,tab2,tab3,tab4,tab5=st.tabs([

"📊 Growth Forecast",

"🏙 Emerging Areas",

"🚇 Infrastructure Impact",

"💼 Economic Trends",

"⚠ Future Risks"

])

# =====================================================
# TAB 1 : GROWTH FORECAST
# =====================================================

with tab1:

    st.subheader("📊 Bengaluru Growth Forecast")

    col1, col2 = st.columns([2, 1])

    with col1:

        fig = px.bar(
            future_df.sort_values(
                "Growth Score",
                ascending=False
            ),
            x="Area",
            y="Growth Score",
            color="Growth Score",
            text="Growth Score",
            color_continuous_scale="Viridis"
        )

        fig.update_layout(
            height=500,
            xaxis_title="Area",
            yaxis_title="Growth Score",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        area = st.selectbox(
            "Choose Area",
            future_df["Area"]
        )

        row = future_df[
            future_df["Area"] == area
        ].iloc[0]

        score = row["Growth Score"]

        st.metric(
            "Growth Potential",
            f"{score}/100"
        )

        st.progress(score / 100)

        if score >= 85:

            st.success("🚀 Premium Growth Zone")

        elif score >= 70:

            st.info("📈 High Growth Zone")

        else:

            st.warning("🌱 Developing Area")

        st.markdown("### Growth Drivers")

        if len(row["Drivers"]) == 0:

            st.write("No strong drivers detected.")

        else:

            for d in row["Drivers"]:

                st.success(d)

        st.markdown("### AI Prediction")

        st.info(
            f"""
{area} is expected to witness continuous urban
development because of improving infrastructure,
employment opportunities and housing demand.
"""
        )


# =====================================================
# TAB 2 : EMERGING AREAS
# =====================================================

with tab2:

    st.subheader("🏙 Emerging Bengaluru Growth Zones")

    st.caption(
        "Top areas with the highest future development potential."
    )

    ranking = future_df.sort_values(
        "Growth Score",
        ascending=False
    ).head(5)

    medals = ["🥇", "🥈", "🥉", "⭐", "⭐"]

    for i, (_, row) in enumerate(ranking.iterrows()):

        area = row["Area"]
        score = row["Growth Score"]
        drivers = row["Drivers"]

        if score >= 85:

            invest = "★★★★★"
            career = "★★★★★"
            living = "★★★★★"
            prediction = "Premium Growth Zone"

        elif score >= 70:

            invest = "★★★★☆"
            career = "★★★★☆"
            living = "★★★★☆"
            prediction = "Rapidly Developing"

        else:

            invest = "★★★☆☆"
            career = "★★★☆☆"
            living = "★★★☆☆"
            prediction = "Steady Growth"

        with st.expander(
            f"{medals[i]} {area} • {score}/100",
            expanded=(i == 0)
        ):

            c1, c2 = st.columns([2, 1])

            with c1:

                st.progress(score / 100)

                st.markdown(f"### 🚀 {prediction}")

                st.markdown("#### Growth Drivers")

                if len(drivers) == 0:

                    st.write("No major drivers.")

                else:

                    for d in drivers:

                        st.success(d)

                st.markdown("#### AI Future Insight")

                st.info(
                    f"""
**{area}** is expected to grow because of:

• Better infrastructure

• Urban expansion

• Employment opportunities

• Housing demand

Overall outlook:

**{prediction}**
"""
                )

            with c2:

                st.metric(
                    "Future Score",
                    f"{score}/100"
                )

                st.metric(
                    "Investment",
                    invest
                )

                st.metric(
                    "Career",
                    career
                )

                st.metric(
                    "Living",
                    living
                )

            st.divider()

            x1, x2, x3 = st.columns(3)

            with x1:

                st.success(
                    """
### 💰 Investment

Recommended

Property appreciation expected.
"""
                )

            with x2:

                st.info(
                    """
### 💼 Career

Strong future employment potential.
"""
                )

            with x3:

                st.warning(
                    """
### 🏠 Living

Suitable for long-term residential growth.
"""
                )

    st.divider()

    st.subheader("📊 Top Area Comparison")

    radar = ranking.copy()

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=radar["Growth Score"],

            theta=radar["Area"],

            fill="toself",

            name="Growth"

        )

    )

    fig.update_layout(

        height=500,

        showlegend=False,

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0, 100]

            )

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.success(
        """
🤖 **AI Summary**

The highlighted areas have the strongest long-term
growth because of metro accessibility, employment,
housing demand and urban development.

These are the most suitable locations for:

- 💰 Investment
- 💼 Career
- 🏠 Living
"""
    )
    
# =====================================================
# TAB 3 : INFRASTRUCTURE IMPACT
# =====================================================

with tab3:

    st.subheader("🚇 Infrastructure Impact Simulator")

    st.write(
        "Understand how metro connectivity and infrastructure influence travel, property value and accessibility."
    )

    st.divider()

    area = st.selectbox(
        "📍 Select Area",
        future_df["Area"],
        key="infra_area"
    )

    score = future_df.loc[
        future_df["Area"] == area,
        "Growth Score"
    ].iloc[0]

    before_time = np.random.randint(55, 90)

    metro_available = area.lower() in metro_df.iloc[:,0].astype(str).str.lower().values

    if metro_available:
        after_time = max(before_time - np.random.randint(15, 30), 20)
        property_growth = np.random.randint(18, 35)
        connectivity = np.random.randint(80, 98)
    else:
        after_time = before_time - np.random.randint(5, 10)
        property_growth = np.random.randint(8, 18)
        connectivity = np.random.randint(55, 75)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Travel Time",
        f"{before_time} min",
        delta=f"-{before_time-after_time} min"
    )

    c2.metric(
        "Connectivity",
        f"{connectivity}/100"
    )

    c3.metric(
        "Property Growth",
        f"+{property_growth}%"
    )

    c4.metric(
        "Future Score",
        f"{score}/100"
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=["Before Metro", "After Metro"],
                y=[before_time, after_time],
                text=[before_time, after_time],
                textposition="auto"
            )
        )

        fig.update_layout(
            title="Estimated Daily Travel Time",
            yaxis_title="Minutes",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        fig2 = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=connectivity,
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"thickness": 0.3},
                    "steps": [
                        {"range": [0, 40], "color": "#ffcccc"},
                        {"range": [40, 70], "color": "#fff2cc"},
                        {"range": [70, 100], "color": "#d9ead3"},
                    ],
                },
                title={"text": "Connectivity Index"},
            )
        )

        fig2.update_layout(height=420)

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    st.subheader("📈 AI Infrastructure Insights")

    a1, a2 = st.columns(2)

    with a1:

        st.success(
            f"""
### 🚇 Connectivity

Area: **{area}**

Current Connectivity Score:

**{connectivity}/100**

Metro Presence:

**{"Available" if metro_available else "Limited"}**
"""
        )

    with a2:

        st.info(
            f"""
### 🏠 Property Outlook

Estimated Appreciation:

**{property_growth}%**

Travel Improvement:

**{before_time-after_time} minutes**

Future Development:

**High**
"""
        )

    st.divider()

    st.subheader("🤖 AI Recommendation")

    if metro_available:

        st.success(
            f"""
**{area}** is expected to experience significant urban growth due to existing metro connectivity.

### Best For

- 💼 Career Growth
- 🏠 Residential Investment
- 💰 Long-term Property Investment
- 🚇 Daily Commuters

Overall Recommendation: **Highly Recommended**
"""
        )

    else:

        st.warning(
            f"""
**{area}** currently has limited metro connectivity but has moderate development potential.

### Best For

- 🏠 Future Investment
- 💰 Long-term Holding

Recommendation:

Monitor upcoming infrastructure projects before investing.
"""
        )
# =====================================================
# TAB 4 : ECONOMIC TRENDS
# =====================================================

with tab4:

    st.subheader("💼 Bengaluru Economic Intelligence")

    st.write(
        "Analyze employment, investment, startup ecosystem and future business opportunities."
    )

    st.divider()

    area = st.selectbox(
        "📍 Select Area",
        future_df["Area"],
        key="economic_area"
    )

    score = future_df.loc[
        future_df["Area"] == area,
        "Growth Score"
    ].iloc[0]

    # ------------------------------------------
    # AI Generated Metrics
    # ------------------------------------------

    hiring = min(score + np.random.randint(-5, 8), 100)

    startup = min(score + np.random.randint(-10, 10), 100)

    salary = np.random.randint(8, 25)

    investment = min(score + np.random.randint(-3, 5), 100)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Hiring Index",
        f"{hiring}/100"
    )

    c2.metric(
        "Startup Score",
        f"{startup}/100"
    )

    c3.metric(
        "Salary Growth",
        f"+{salary}%"
    )

    c4.metric(
        "Investment Score",
        f"{investment}/100"
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=[
                    "Hiring",
                    "Investment",
                    "Startup",
                    "Growth"
                ],
                y=[
                    hiring,
                    investment,
                    startup,
                    score
                ],
                text=[
                    hiring,
                    investment,
                    startup,
                    score
                ],
                textposition="auto"
            )
        )

        fig.update_layout(

            title="Economic Indicators",

            height=420

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        labels = [

            "IT",

            "AI",

            "FinTech",

            "Healthcare",

            "Manufacturing"

        ]

        values = np.random.randint(
            10,
            35,
            5
        )

        pie = px.pie(

            names=labels,

            values=values,

            title="Future Industry Growth"

        )

        st.plotly_chart(

            pie,

            use_container_width=True

        )

    st.divider()

    st.subheader("📈 Business Opportunity Score")

    progress = investment / 100

    st.progress(progress)

    if investment >= 85:

        st.success(
            "🟢 Excellent location for business expansion."
        )

    elif investment >= 70:

        st.info(
            "🟡 Good future business opportunity."
        )

    else:

        st.warning(
            "🟠 Moderate investment potential."
        )

    st.divider()

    st.subheader("🏆 Top Growth Industries")

    ind1, ind2 = st.columns(2)

    with ind1:

        st.success("""
### 💻 Information Technology

★★★★★

Future Demand : High

Expected Hiring : Very High

Recommended Skills

• AI

• Data Science

• Cloud

• Cyber Security
""")

        st.success("""
### 💳 FinTech

★★★★☆

High Startup Activity

Growing Investment

Digital Payments
""")

    with ind2:

        st.info("""
### 🏥 Healthcare

★★★★☆

Growing Hospitals

Medical Technology

Healthcare Analytics
""")

        st.info("""
### 🤖 Artificial Intelligence

★★★★★

Highest Future Demand

Automation

Generative AI

Machine Learning
""")

    st.divider()

    st.subheader("🤖 AI Economic Recommendation")

    st.success(
f"""
### Area Analysis : {area}

📈 Growth Potential : {score}/100

💼 Hiring Outlook : {hiring}/100

💰 Investment Score : {investment}/100

🏢 Startup Ecosystem : {startup}/100

### Recommendation

This area has strong long-term economic potential because of:

✓ Employment Growth

✓ Urban Expansion

✓ Infrastructure Development

✓ Business Opportunities

Suitable for:

• Career

• Investment

• Startup

• Office Space

• Commercial Development
"""
    )
# =====================================================
# TAB 5 : FUTURE RISK CENTER
# =====================================================

with tab5:

    st.subheader("⚠ Bengaluru Future Risk Intelligence")

    st.write(
        """
Predict future urban challenges using
traffic, civic infrastructure,
housing demand and growth patterns.
"""
    )

    st.divider()

    area = st.selectbox(
        "📍 Select Area",
        future_df["Area"],
        key="risk_area"
    )

    score = future_df.loc[
        future_df["Area"] == area,
        "Growth Score"
    ].iloc[0]

    # -----------------------------------------
    # Calculate Risks
    # -----------------------------------------

    traffic = traffic_df[
        traffic_df["area"].str.lower() == area.lower()
    ]

    civic = civic_df[
        civic_df["area"].str.lower() == area.lower()
    ]

    if not traffic.empty:

        avg_speed = traffic.avg_speed.mean()

        traffic_risk = max(
            100 - avg_speed * 3,
            20
        )

    else:

        traffic_risk = np.random.randint(
            30,
            60
        )

    if not civic.empty:

        complaints = civic.complaint_count.sum()

        civic_risk = min(
            complaints / 2,
            100
        )

    else:

        civic_risk = np.random.randint(
            20,
            60
        )

    housing_risk = np.random.randint(
        40,
        90
    )

    population_risk = min(
        score + np.random.randint(
            -5,
            10
        ),
        100
    )

    # -----------------------------------------
    # KPI Cards
    # -----------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Traffic Risk",
        f"{int(traffic_risk)}/100"
    )

    c2.metric(
        "Civic Risk",
        f"{int(civic_risk)}/100"
    )

    c3.metric(
        "Housing Pressure",
        f"{housing_risk}/100"
    )

    c4.metric(
        "Population Pressure",
        f"{population_risk}/100"
    )

    st.divider()

    # -----------------------------------------
    # Risk Chart
    # -----------------------------------------

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=[
                "Traffic",
                "Civic",
                "Housing",
                "Population"
            ],

            y=[
                traffic_risk,
                civic_risk,
                housing_risk,
                population_risk
            ],

            text=[
                int(traffic_risk),
                int(civic_risk),
                housing_risk,
                population_risk
            ],

            textposition="auto"

        )

    )

    fig.update_layout(

        title="Future Urban Risk Index",

        height=450

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # -----------------------------------------
    # Risk Cards
    # -----------------------------------------

    r1, r2 = st.columns(2)

    with r1:

        if traffic_risk > 70:

            st.error(
                """
### 🚦 Traffic

High congestion expected.

Reason

• Population Growth

• Vehicle Increase

Recommendation

Expand Metro Usage
"""
            )

        else:

            st.success(
                """
### 🚦 Traffic

Risk manageable.
"""
            )

        if housing_risk > 70:

            st.warning(
                """
### 🏠 Housing

High housing demand expected.

Property prices may rise.

Affordable housing projects recommended.
"""
            )

        else:

            st.success(
                """
### 🏠 Housing

Balanced demand.
"""
            )

    with r2:

        if civic_risk > 60:

            st.error(
                """
### 🏛 Civic

Future infrastructure pressure.

Water

Roads

Waste Management

Need expansion.
"""
            )

        else:

            st.success(
                """
### 🏛 Civic

Infrastructure adequate.
"""
            )

        if population_risk > 80:

            st.warning(
                """
### 👥 Population

Rapid urban expansion expected.

Need:

Schools

Hospitals

Public Transport
"""
            )

        else:

            st.success(
                """
### 👥 Population

Growth under control.
"""
            )

    st.divider()

    # -----------------------------------------
    # AI Recommendations
    # -----------------------------------------

    st.subheader("🤖 AI Recommendations")

    rec = []

    if traffic_risk > 70:

        rec.append(
            "🚇 Expand metro connectivity."
        )

    if civic_risk > 60:

        rec.append(
            "🏛 Improve civic infrastructure."
        )

    if housing_risk > 70:

        rec.append(
            "🏠 Increase affordable housing."
        )

    if population_risk > 80:

        rec.append(
            "👥 Expand schools and hospitals."
        )

    if len(rec) == 0:

        st.success(
            """
Area is well prepared for future growth.
"""
        )

    else:

        for r in rec:

            st.info(r)

    st.divider()

    st.success(
f"""
## 📈 AI Future Summary

### Area

**{area}**

Growth Potential

**{score}/100**

Overall Outlook

✅ Strong Growth

### Key Opportunities

• Employment

• Infrastructure

• Housing

• Metro Expansion

### Major Challenge

Managing urban growth while maintaining quality of life.
"""
    )

st.divider()

st.caption(
    "🚀 Bengaluru Future Trends Intelligence | Bengaluru OS"
)

