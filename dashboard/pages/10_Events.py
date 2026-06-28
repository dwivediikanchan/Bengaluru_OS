import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime
import numpy as np


st.set_page_config(

    page_title="Bengaluru Events Intelligence",

    page_icon="🎉",

    layout="wide"

)


# =====================================================
# HEADER
# =====================================================


st.title("🎉 Bengaluru Events Intelligence")


st.markdown("""

### Discover Bengaluru's Events Ecosystem

Explore upcoming events, trending categories,
and personalized recommendations.

""")



# =====================================================
# EVENT DATA
# =====================================================


events = pd.DataFrame({

    "Event":[

        "Bengaluru Tech Summit",

        "Sunburn Bengaluru",

        "Startup Expo Bengaluru",

        "Bangalore Food Festival",

        "Marathon Bengaluru",

        "AI & Data Conference",

        "Bangalore Music Night"

    ],


    "Category":[

        "Technology",

        "Music",

        "Startup",

        "Food",

        "Sports",

        "Technology",

        "Music"

    ],


    "Area":[

        "Whitefield",

        "Electronic City",

        "Koramangala",

        "Indiranagar",

        "Cubbon Park",

        "HSR Layout",

        "MG Road"

    ],


    "Month":[

        "August",

        "September",

        "October",

        "August",

        "November",

        "December",

        "September"

    ],


    "Crowd":[

        "High",

        "Very High",

        "Medium",

        "High",

        "High",

        "Medium",

        "High"

    ],


    "Price":[

        "Free",

        "Paid",

        "Paid",

        "Free",

        "Free",

        "Paid",

        "Paid"

    ]

})



# =====================================================
# TABS
# =====================================================


tab1,tab2,tab3,tab4 = st.tabs([


"📅 Upcoming Events",

"🔥 Trending Events",

"📍 Event Discovery",

"🤖 AI Recommendation"


])



# =====================================================
# TAB 1
# UPCOMING EVENTS
# =====================================================



with tab1:


    st.subheader("📅 Upcoming Bengaluru Events")


    st.write(

        "Latest events happening across Bengaluru."

    )


    st.divider()



    for _,row in events.iterrows():


        with st.container():


            c1,c2 = st.columns([2,1])



            with c1:


                st.markdown(

f"""

## 🎉 {row['Event']}


📍 Location:

**{row['Area']}**


📅 Month:

**{row['Month']}**


🎯 Category:

**{row['Category']}**

"""

                )



            with c2:


                st.metric(

                    "Crowd",

                    row["Crowd"]

                )


                st.metric(

                    "Entry",

                    row["Price"]

                )



            st.divider()

# =====================================================
# TAB 2
# TRENDING EVENTS
# =====================================================


with tab2:


    st.subheader("🔥 Trending Bengaluru Events")


    st.write(

        "Analyze what type of events are gaining popularity."

    )


    st.divider()



    # ---------------------------------
    # Event Popularity Score
    # ---------------------------------


    trend_df = events.copy()



    trend_df["Popularity"] = [

        95,

        90,

        82,

        78,

        75,

        88,

        80

    ]



    trend_df["Interest"] = [

        "Very High",

        "Very High",

        "High",

        "Medium",

        "Medium",

        "High",

        "High"

    ]



    # ---------------------------------
    # Popularity Chart
    # ---------------------------------


    fig = px.bar(

        trend_df,

        x="Event",

        y="Popularity",

        color="Category",

        title="Event Popularity Ranking"

    )


    fig.update_layout(

        height=500,

        xaxis_tickangle=-45

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ---------------------------------
    # Category Trend
    # ---------------------------------


    st.subheader(

        "📊 Event Category Trends"

    )


    category_count = (

        events

        .groupby("Category")

        .size()

        .reset_index(

            name="Count"

        )

    )



    pie = px.pie(

        category_count,

        names="Category",

        values="Count",

        title="Popular Event Categories"

    )



    st.plotly_chart(

        pie,

        use_container_width=True

    )



    st.divider()



    # ---------------------------------
    # Top Trending Cards
    # ---------------------------------


    st.subheader(

        "🏆 Top Trending Events"

    )



    top_events = trend_df.sort_values(

        "Popularity",

        ascending=False

    ).head(3)



    for _,row in top_events.iterrows():


        st.success(

f"""

### 🔥 {row['Event']}


Category:

{row['Category']}


Location:

📍 {row['Area']}


Popularity:

⭐ {row['Popularity']}/100


Interest:

{row['Interest']}

"""

        )



    st.divider()



    st.info(

"""

🤖 AI Trend Insight


Bengaluru's fastest growing event segments:


🥇 Technology & AI

🥈 Music & Entertainment

🥉 Startup & Business


Future trend:

More technology, networking and innovation events
are expected to grow in Bengaluru.

"""

    )
# =====================================================
# TAB 3
# EVENT DISCOVERY
# =====================================================


with tab3:


    st.subheader("📍 Discover Bengaluru Events")


    st.write(

        "Find events based on your location, interest and budget."

    )


    st.divider()



    # ---------------------------------
    # Filters
    # ---------------------------------


    col1,col2,col3 = st.columns(3)



    with col1:


        selected_area = st.selectbox(

            "📍 Choose Area",

            [

                "All",

                "Whitefield",

                "Koramangala",

                "HSR Layout",

                "Electronic City",

                "Indiranagar",

                "MG Road",

                "Cubbon Park"

            ]

        )



    with col2:


        selected_category = st.selectbox(

            "🎯 Category",

            [

                "All",

                "Technology",

                "Music",

                "Startup",

                "Food",

                "Sports"

            ]

        )



    with col3:


        selected_price = st.selectbox(

            "💰 Entry",

            [

                "All",

                "Free",

                "Paid"

            ]

        )



    st.divider()



    # ---------------------------------
    # Filtering Engine
    # ---------------------------------


    filtered = events.copy()



    if selected_area != "All":

        filtered = filtered[

            filtered["Area"] == selected_area

        ]



    if selected_category != "All":

        filtered = filtered[

            filtered["Category"] == selected_category

        ]



    if selected_price != "All":

        filtered = filtered[

            filtered["Price"] == selected_price

        ]



    # ---------------------------------
    # Result Display
    # ---------------------------------


    st.subheader(

        f"🎉 Available Events ({len(filtered)})"

    )



    if filtered.empty:


        st.warning(

            "No events found for selected filters."

        )


    else:


        for _,row in filtered.iterrows():


            with st.container():


                a,b = st.columns([2,1])



                with a:


                    st.markdown(

f"""

## 🎉 {row['Event']}


📍 {row['Area']}


🎯 {row['Category']}


📅 {row['Month']}

"""

                    )



                with b:


                    st.metric(

                        "Crowd",

                        row["Crowd"]

                    )


                    st.metric(

                        "Entry",

                        row["Price"]

                    )



                st.divider()



    st.success(

"""

🤖 AI Discovery Tip


Based on Bengaluru trends:


Technology + Startup events are best for:

✓ Networking

✓ Career growth

✓ Industry exposure


Entertainment events are best for:

✓ Social experience

✓ Community building

"""

    )
# =====================================================
# TAB 4
# AI EVENT RECOMMENDATION
# =====================================================


with tab4:


    st.subheader("🤖 AI Event Recommendation Engine")


    st.write(

        "Get personalized Bengaluru event suggestions."

    )


    st.divider()



    # ---------------------------------
    # User Preferences
    # ---------------------------------


    c1,c2 = st.columns(2)



    with c1:


        interest = st.selectbox(

            "🎯 Your Interest",

            [

                "Technology",

                "Music",

                "Startup",

                "Food",

                "Sports"

            ],

            key="event_interest"

        )



    with c2:


        purpose = st.selectbox(

            "Why are you attending?",

            [

                "Career Growth",

                "Networking",

                "Entertainment",

                "Learning",

                "Social Experience"

            ],

            key="event_purpose"

        )



    st.divider()



    # ---------------------------------
    # AI Recommendation Logic
    # ---------------------------------


    recommendation = events[

        events["Category"] == interest

    ]



    if recommendation.empty:


        recommendation = events



    recommendation = recommendation.copy()



    recommendation["AI Score"] = np.random.randint(

        75,

        100,

        size=len(recommendation)

    )



    recommendation = recommendation.sort_values(

        "AI Score",

        ascending=False

    )



    st.subheader(

        "✨ Recommended Events"

    )



    # ---------------------------------
    # Recommendation Cards
    # ---------------------------------


    for _,row in recommendation.head(3).iterrows():


        st.success(

f"""

## 🎉 {row['Event']}


📍 Location:

{row['Area']}


🎯 Category:

{row['Category']}


⭐ AI Match Score:

{row['AI Score']}%


🤖 Why Recommended:


Because you selected:

**{interest}**


Best suited for:

**{purpose}**


AI Reason:

This event matches your interest,
location preference and Bengaluru trends.

"""

        )



        st.divider()



    # ---------------------------------
    # Smart Suggestions
    # ---------------------------------


    st.subheader(

        "🧠 Smart Event Advice"

    )



    if purpose == "Career Growth":


        st.info(

"""

Recommended Focus:


✓ Technology conferences

✓ AI events

✓ Startup meetups

✓ Industry networking


Best for building professional connections.

"""

        )


    elif purpose == "Networking":


        st.info(

"""

Recommended Focus:


✓ Startup events

✓ Business expos

✓ Community meetups


Best for meeting new people.

"""

        )


    elif purpose == "Learning":


        st.info(

"""

Recommended Focus:


✓ AI workshops

✓ Developer events

✓ Training sessions


Best for skill improvement.

"""

        )


    else:


        st.info(

"""

Recommended Focus:


✓ Music

✓ Food festivals

✓ Cultural events


Best for experience and enjoyment.

"""

        )



    st.divider()



    st.success(

"""

🌆 Bengaluru Event Intelligence Complete


Features:


✅ Upcoming Events

✅ Trending Analysis

✅ Event Discovery

✅ AI Recommendations


Bengaluru OS helps users discover
the right events at the right time.

"""

    )