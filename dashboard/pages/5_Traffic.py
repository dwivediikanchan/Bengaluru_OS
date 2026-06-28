import streamlit as st
import pandas as pd
import plotly.express as px

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

    page_title="Traffic Intelligence",

    page_icon="🚦",

    layout="wide"

)



st.title("🚦 Bengaluru Traffic Intelligence")


st.write(
"""
Smart traffic analytics system.

Understand congestion,
travel impact and better routes.
"""
)





# ======================================
# LOAD TRAFFIC DATA
# ======================================


def load_traffic():


    conn = get_connection()


    df = conn.execute(

    """

    SELECT

    area,

    time_slot,

    avg_speed,

    traffic_level


    FROM traffic

    """

    ).fetchdf()


    conn.close()


    return df





traffic_df = load_traffic()





if traffic_df.empty:

    st.error(
    "Traffic data unavailable"
    )

    st.stop()





# ======================================
# CONGESTION SCORE
# ======================================


def congestion(speed):


    if speed >=40:

        return 20


    elif speed >=25:

        return 50


    else:

        return 90





traffic_df["congestion_score"] = traffic_df["avg_speed"].apply(

congestion

)









# ======================================
# TABS
# ======================================


live_tab,analysis_tab,time_tab,route_tab = st.tabs(

[

"🚦 Live Traffic",

"📊 Traffic Analysis",

"⏱ Travel Impact",

"🛣 Route Optimization"

]

)







# ======================================
# LIVE TRAFFIC
# ======================================


with live_tab:


    st.subheader(

    "🚦 Live Traffic Status"

    )


    area = st.selectbox(

    "Select Area",

    traffic_df.area.unique()

    )


    row = traffic_df[

    traffic_df.area==area

    ].iloc[0]



    a,b,c = st.columns(3)



    a.metric(

    "Average Speed",

    f"{row.avg_speed} km/h"

    )



    b.metric(

    "Traffic Level",

    row.traffic_level

    )



    c.metric(

    "Congestion",

    f"{row.congestion_score}/100"

    )



    if row.traffic_level.lower()=="high":


        st.error(
        "🔴 Heavy traffic detected"
        )


    elif row.traffic_level.lower()=="medium":


        st.warning(
        "🟡 Moderate traffic"
        )


    else:


        st.success(
        "🟢 Smooth traffic"
        )










# ======================================
# ANALYSIS
# ======================================



with analysis_tab:


    st.subheader(

    "📊 Traffic Congestion Analysis"

    )


    chart = px.bar(

    traffic_df,

    x="area",

    y="congestion_score",

    color="traffic_level"

    )


    st.plotly_chart(

    chart,

    use_container_width=True

    )



    st.divider()



    st.subheader(

    "⏰ Peak Hour Detection"

    )


    peak = traffic_df.groupby(

    "time_slot"

    )["avg_speed"].mean().reset_index()



    fig = px.line(

    peak,

    x="time_slot",

    y="avg_speed"

    )


    st.plotly_chart(

    fig,

    use_container_width=True

    )





    st.divider()



    st.subheader(

    "📈 Traffic Forecasting"

    )



    increase = st.slider(

    "Expected traffic increase %",

    0,

    100,

    20

    )



    st.info(

f"""

Future prediction:

Traffic pressure may increase by

{increase}% during high demand.


"""

    )









# ======================================
# TRAVEL IMPACT
# ======================================



with time_tab:


    st.subheader(

    "⏱ Travel Impact Analysis"

    )



    area = st.selectbox(

    "Select Area",

    traffic_df.area.unique(),

    key="travel"

    )



    distance = st.slider(

    "Distance KM",

    1,

    60,

    20

    )



    row = traffic_df[

    traffic_df.area==area

    ].iloc[0]



    normal = distance*2



    traffic_time = (

    distance / row.avg_speed

    )*60



    delay = traffic_time-normal




    a,b,c = st.columns(3)



    a.metric(

    "Normal",

    f"{normal:.0f} min"

    )


    b.metric(

    "Traffic",

    f"{traffic_time:.0f} min"

    )


    c.metric(

    "Delay",

    f"{delay:.0f} min"

    )








# ======================================
# ROUTE OPTIMIZATION
# ======================================



with route_tab:


    st.subheader(

    "🛣 Smart Route Optimization"

    )


    st.write(

    """

    Find better travel decisions based on
    current Bengaluru traffic.

    """

    )



    start = st.selectbox(

    "Current Area",

    traffic_df.area.unique(),

    key="route"

    )



    current = traffic_df[

    traffic_df.area==start

    ].iloc[0]



    current_speed = current.avg_speed





    st.subheader(

    "Current Situation"

    )


    a,b = st.columns(2)



    a.metric(

    "Speed",

    f"{current_speed} km/h"

    )


    b.metric(

    "Traffic",

    current.traffic_level

    )






    better = traffic_df[

    traffic_df.avg_speed >

    current_speed

    ]





    if not better.empty:



        solution = better.sort_values(

        "avg_speed",

        ascending=False

        ).iloc[0]



        improvement = (

        solution.avg_speed-current_speed

        )



        st.success(

f"""

## ✅ Recommended Solution



Avoid:

📍 {start}



Try:

📍 {solution.area}



Reason:


✓ Faster traffic flow

✓ Higher average speed

✓ Lower congestion pressure



Expected improvement:

+{improvement} km/h



Best for:

✓ Daily commute

✓ Peak hours

✓ Time saving



"""

        )




    else:


        st.info(

        """

        Current route is already good.

        No better traffic option found.

        """

        )






    if current.traffic_level.lower()=="high":


        st.warning(

        """

        Advice:

        • Avoid rush hours

        • Prefer metro connectivity

        • Keep extra travel buffer


        """

        )