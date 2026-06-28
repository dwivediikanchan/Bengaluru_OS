import streamlit as st
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

    page_title="Bengaluru Decision AI",

    page_icon="🎯",

    layout="wide"

)



st.title(
    "🎯 Bengaluru Decision Intelligence"
)



st.markdown(
"""
AI powered Bengaluru area analysis.

Analyze any location using:

💼 Career  
🏠 Housing  
🚇 Metro  
🚦 Traffic  
🌦 Weather  
🏛 Civic Infrastructure
"""
)



@st.cache_data
def load(table):

    conn = get_connection()

    df = conn.execute(
        f"SELECT * FROM {table}"
    ).fetchdf()

    conn.close()

    return df



housing = load("housing")
metro = load("metro")
traffic = load("traffic")
weather = load("weather")
jobs = load("jobs")
civic = load("civic")



def clean(x):

    return (

        str(x)
        .lower()
        .replace(" ","")
        .replace("-","")

    )



areas = metro["area"].unique()



area = st.selectbox(

    "🏙 Select Bengaluru Area",

    areas

)



key = clean(area)



h = housing[
    housing["area"]
    .apply(clean)
    ==
    key
]


m = metro[
    metro["area"]
    .apply(clean)
    ==
    key
]


t = traffic[
    traffic["area"]
    .apply(clean)
    ==
    key
]


w = weather[
    weather["area"]
    .apply(clean)
    ==
    key
]


c = civic[
    civic["area"]
    .apply(clean)
    ==
    key
]



st.divider()



# =========================
# METRICS
# =========================


traffic_value = str(

    t["traffic_level"]
    .iloc[0]

).capitalize()



a,b,c1,d = st.columns(4)



a.metric(

    "🚇 Metro",

    f"{int(m['connectivity_score'].iloc[0])}/10"

)



b.metric(

    "🏠 Avg Rent",

    f"₹{int(h['rent'].mean())}"

)



c1.metric(

    "🚦 Traffic",

    traffic_value

)



d.metric(

    "🌦 Temperature",

    f"{int(w['temperature'].iloc[0])}°C"

)



st.divider()



# =========================
# HOUSING
# =========================


col1,col2 = st.columns(2)



with col1:


    st.subheader(
        "🏠 Housing Intelligence"
    )


    st.info(

f"""

Average Rent:

₹{int(h['rent'].mean())}



Available BHK:

{[int(x) for x in h['bhk'].unique()]}

"""

    )




with col2:


    st.subheader(
        "🚦 Mobility Intelligence"
    )


    st.warning(

f"""

Average Speed:

{int(t['avg_speed'].mean())} km/h



Traffic Level:

{traffic_value}

"""

    )



st.divider()



# =========================
# AI SCORE
# =========================


score = 50



if int(m["connectivity_score"].iloc[0]) >= 8:

    score += 15



if h["rent"].mean() < 25000:

    score += 15



if t["avg_speed"].mean() > 25:

    score += 10



if c["complaint_count"].sum() < 100:

    score += 10



score = min(score,100)



st.subheader(
    "🤖 Bengaluru OS AI Summary"
)



st.metric(

    "Area Intelligence Score",

    f"{score}/100"

)



if score >=75:


    st.success(

f"""
{area} is a high potential Bengaluru area.

Strengths:

✓ Connectivity

✓ Housing

✓ Mobility

"""

    )


elif score >=55:


    st.info(

f"""
{area} is a balanced Bengaluru location.

Suitable depending on your requirement.

"""

    )


else:


    st.warning(

f"""
{area} has some challenges.

Consider traffic and infrastructure.

"""

    )



st.divider()



# =========================
# CAREER
# =========================


st.subheader(
    "💼 Career Intelligence"
)



area_words = [

    x.lower()

    for x in area.split()

]



job_match = jobs[

    jobs["location"]

    .astype(str)

    .str.lower()

    .apply(

        lambda text:

        any(

            word in text

            for word in area_words

            if len(word)>3

        )

    )

]



if job_match.empty:

    job_match = jobs



st.metric(

    "Relevant Jobs Found",

    len(job_match)

)



st.dataframe(

    job_match[

        [

            "title",

            "company",

            "location",

            "salary"

        ]

    ],

    use_container_width=True

)