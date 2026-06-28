import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

sys.path.append(ROOT)

from database.connection import get_connection

st.set_page_config(
    page_title="Weather Intelligence",
    page_icon="🌦",
    layout="wide"
)

st.title("🌦 Bengaluru Weather Intelligence")
st.caption("Real-time weather insights for smarter living and commuting.")

# ====================================================
# LOAD WEATHER DATA
# ====================================================

@st.cache_data
def load_weather():

    conn = get_connection()

    df = conn.execute("""

    SELECT
        area,
        temperature,
        rain_probability,
        humidity,
        weather_condition

    FROM weather

    """).fetchdf()

    conn.close()

    return df


weather_df = load_weather()

# ====================================================
# HELPER FUNCTIONS
# ====================================================

def comfort_score(temp, humidity, rain):

    score = 100

    if temp > 34:
        score -= 25
    elif temp > 30:
        score -= 10

    if humidity > 80:
        score -= 20
    elif humidity > 70:
        score -= 10

    if rain > 80:
        score -= 25
    elif rain > 60:
        score -= 10

    return max(score, 0)


weather_df["comfort_score"] = weather_df.apply(
    lambda x: comfort_score(
        x.temperature,
        x.humidity,
        x.rain_probability
    ),
    axis=1,
)


def weather_summary(row):

    if row.temperature >= 34:
        return "🔥 Very Hot"

    if row.rain_probability >= 70:
        return "🌧 Heavy Rain Expected"

    if row.humidity >= 80:
        return "💧 Very Humid"

    return "🌤 Pleasant"


def travel_advice(row):

    if row.rain_probability > 70:
        return "Carry umbrella • Expect traffic delays"

    if row.temperature > 34:
        return "Stay hydrated • Avoid afternoon travel"

    return "Good weather for travel"


# ====================================================
# TABS
# ====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🌦 Current Weather",
        "📊 Weather Analysis",
        "🌡 Living Comfort",
        "🚗 Weather Impact",
        "⚠ Alerts",
    ]
)

# ====================================================
# CURRENT WEATHER
# ====================================================

with tab1:

    st.subheader("Current Weather")

    area = st.selectbox(
        "Select Area",
        weather_df.area.unique()
    )

    row = weather_df[
        weather_df.area == area
    ].iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🌡 Temperature",
        f"{row.temperature} °C"
    )

    c2.metric(
        "🌧 Rain",
        f"{row.rain_probability}%"
    )

    c3.metric(
        "💧 Humidity",
        f"{row.humidity}%"
    )

    c4.metric(
        "🌤 Condition",
        row.weather_condition
    )

    st.info(weather_summary(row))

    st.success(
        travel_advice(row)
    )

# ====================================================
# WEATHER ANALYSIS
# ====================================================

with tab2:

    st.subheader("Area Weather Comparison")

    fig = px.bar(
        weather_df,
        x="area",
        y="temperature",
        color="temperature",
        title="Temperature Across Bengaluru"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    fig2 = px.bar(
        weather_df,
        x="area",
        y="rain_probability",
        color="rain_probability",
        title="Rain Probability"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3 = px.line(
        weather_df,
        x="area",
        y="humidity",
        markers=True,
        title="Humidity Comparison"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
# ====================================================
# LIVING COMFORT
# ====================================================

with tab3:

    st.subheader(
        "🌡 Weather Living Comfort Intelligence"
    )


    area = st.selectbox(

        "Compare Area",

        weather_df.area.unique(),

        key="comfort_area"

    )


    row = weather_df[

        weather_df.area == area

    ].iloc[0]



    score = row.comfort_score



    c1, c2, c3 = st.columns(3)



    c1.metric(

        "Comfort Score",

        f"{score}/100"

    )


    c2.metric(

        "Weather",

        row.weather_condition

    )


    c3.metric(

        "Humidity",

        f"{row.humidity}%"

    )





    if score >= 80:


        st.success(

        """

        🟢 Excellent living condition

        Weather is suitable for:

        • Outdoor activity

        • Daily commute

        • Residential living

        """

        )


    elif score >= 60:


        st.warning(

        """

        🟡 Moderate comfort

        Some weather impact expected.

        """

        )


    else:


        st.error(

        """

        🔴 Weather discomfort detected

        """

        )






    st.divider()



    st.subheader(

        "🏆 Best Weather Areas"

    )



    best = weather_df.sort_values(

        "comfort_score",

        ascending=False

    ).head(5)



    for _, area_row in best.iterrows():


        st.success(

f"""

📍 {area_row.area}


Comfort:

{area_row.comfort_score}/100


Condition:

{area_row.weather_condition}

"""

        )








# ====================================================
# WEATHER IMPACT
# ====================================================


with tab4:


    st.subheader(

        "🚗 Weather Impact Intelligence"

    )



    area = st.selectbox(

        "Select Travel Area",

        weather_df.area.unique(),

        key="impact"

    )



    row = weather_df[

        weather_df.area == area

    ].iloc[0]





    st.write(

    """

    Weather affects:

    ✓ Traffic

    ✓ Metro usage

    ✓ Travel planning

    ✓ Outdoor activities


    """

    )




    # Travel impact


    if row.rain_probability > 70:


        traffic_effect = "High"

        metro_effect = "Increase"

        advice = "Avoid two-wheeler travel"



    elif row.temperature > 33:


        traffic_effect = "Medium"

        metro_effect = "Normal"

        advice = "Avoid afternoon travel"



    else:


        traffic_effect = "Low"

        metro_effect = "Normal"

        advice = "Good travel conditions"






    c1,c2,c3 = st.columns(3)



    c1.metric(

        "Traffic Impact",

        traffic_effect

    )



    c2.metric(

        "Metro Demand",

        metro_effect

    )



    c3.metric(

        "Travel Advice",

        advice

    )






    st.info(

f"""

Weather decision:


Area:

{area}



Condition:

{row.weather_condition}



Recommended:

{advice}

"""

    )









# ====================================================
# WEATHER ALERT ENGINE
# ====================================================


with tab5:


    st.subheader(

        "⚠ Weather Alert System"

    )



    alerts_found = False




    for _, row in weather_df.iterrows():



        if row.temperature >= 35:


            alerts_found = True


            st.error(

f"""

🔥 Heat Alert


Area:

{row.area}


Temperature:

{row.temperature} °C


Action:

Avoid direct sunlight

"""

            )




        elif row.rain_probability >= 80:


            alerts_found = True


            st.warning(

f"""

🌧 Heavy Rain Alert


Area:

{row.area}


Rain Probability:

{row.rain_probability}%


Action:

Expect travel delays

"""

            )





        elif row.humidity >= 85:


            alerts_found = True


            st.warning(

f"""

💧 High Humidity Alert


Area:

{row.area}


Humidity:

{row.humidity}%


Action:

Outdoor discomfort possible

"""

            )






    if not alerts_found:


        st.success(

        """

        🟢 No major weather alerts.


        Bengaluru weather conditions are stable.

        """

        )





# ====================================================
# FOOTER
# ====================================================


st.divider()


st.caption(

"🌦 Weather Intelligence Module | Bengaluru OS"

)