import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium


# ==============================
# PROJECT IMPORT FIX
# ==============================

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

    page_title="Metro Intelligence",

    page_icon="🚇",

    layout="wide"

)




st.title(
"🚇 Bengaluru Metro Intelligence"
)



st.write(
"""
Smart Bengaluru Metro Analytics System

Routes | Interactive Map | Connectivity | Travel Analysis | Alerts
"""
)





# =====================================================
# METRO ROUTE DATA
# =====================================================


routes = pd.DataFrame(

[


["Purple Line",
"Whitefield",
"Majestic",
15,
24,
55],


["Purple Line",
"Whitefield",
"Kengeri",
25,
35,
85],


["Green Line",
"Nagasandra",
"Majestic",
14,
18,
40],


["Green Line",
"Majestic",
"Yelachenahalli",
20,
24,
50],


["Yellow Line",
"Electronic City",
"RV Road",
16,
22,
50],


["Pink Line (Upcoming)",
"Kalena Agrahara",
"Nagawara",
18,
21,
45]


],


columns=[

"Line",

"From",

"To",

"Stations",

"Distance",

"Time"

]

)







# =====================================================
# DISRUPTION DATA
# =====================================================


alerts = pd.DataFrame(

[

["Purple Line","Normal",0],

["Green Line","Minor Delay",10],

["Yellow Line","Maintenance",30],

["Pink Line","Upcoming",0]

],


columns=[

"Line",

"Status",

"Delay"

]

)







# =====================================================
# LOAD AREA SCORE
# =====================================================


def load_area_score():

    try:


        conn = get_connection()


        df = conn.execute(

        """

        SELECT

        area,

        metro_score,

        traffic_score,

        area_score


        FROM area_score


        """

        ).fetchdf()


        conn.close()


        return df



    except:


        return pd.DataFrame()





area_df = load_area_score()







# =====================================================
# TABS
# =====================================================


route_tab,map_tab,connect_tab,time_tab,alert_tab = st.tabs(

[

"🚇 Metro Routes",

"🗺️ Metro Map",

"📍 Connectivity",

"⏱ Travel Time",

"⚠️ Alerts"

]

)









# =====================================================
# ROUTE MODULE
# =====================================================


with route_tab:


    st.subheader(
    "🚇 Metro Route Planner"
    )



    c1,c2 = st.columns(2)



    source = c1.selectbox(

    "From Station",

    sorted(routes["From"].unique())

    )



    destination = c2.selectbox(

    "Destination",

    sorted(routes["To"].unique())

    )




    if st.button(
    "Find Metro Route"
    ):


        result = routes[

        (routes["From"]==source)

        &

        (routes["To"]==destination)

        ]



        if len(result):


            r=result.iloc[0]



            a,b,c,d=st.columns(4)



            a.metric(

            "Line",

            r.Line

            )


            b.metric(

            "Stations",

            r.Stations

            )


            c.metric(

            "Distance",

            f"{r.Distance} KM"

            )


            d.metric(

            "Time",

            f"{r.Time} min"

            )



            st.success(

f"""

{source}

↓

{r.Line}

↓

{destination}


Estimated travel:

{r.Time} minutes

"""

            )



        else:


            st.warning(
            "Route unavailable"
            )










# =====================================================
# INTERACTIVE MAP
# =====================================================


with map_tab:



    st.subheader(

    "🗺️ Bengaluru Metro Interactive Map"

    )



    station_data = {


    "Majestic":{

    "location":[12.9716,77.5946],

    "lines":[

    "Purple Line",

    "Green Line"

    ],

    "type":"Major Interchange"

    },


    "Whitefield":{

    "location":[13.0320,77.6600],

    "lines":[

    "Purple Line"

    ],

    "type":"Terminal Station"

    },


    "Electronic City":{

    "location":[12.8399,77.6770],

    "lines":[

    "Yellow Line"

    ],

    "type":"Upcoming Metro Zone"

    },


    "HSR Layout":{

    "location":[12.9165,77.6101],

    "lines":[

    "Yellow Line",

    "Pink Line"

    ],

    "type":"High Growth Area"

    },


    "Nagawara":{

    "location":[13.0430,77.6200],

    "lines":[

    "Pink Line"

    ],

    "type":"Future Station"

    }


    }





    selected = st.selectbox(

    "Select Station",

    station_data.keys()

    )



    details = station_data[selected]





    c1,c2=st.columns(2)



    c1.info(

f"""

### 🚉 {selected}


Type:

{details['type']}



Connected Lines:

{", ".join(details['lines'])}

"""

    )



    c2.success(

f"""

Connectivity:

{len(details['lines'])} Lines


Status:

Active

"""

    )






    metro_map = folium.Map(

    location=details["location"],

    zoom_start=13

    )






    lines = {


    "Purple Line":

    (

    [

    [12.9716,77.5946],

    [13.0320,77.6600]

    ],

    "purple"

    ),



    "Green Line":

    (

    [

    [13.0450,77.5000],

    [12.9716,77.5946]

    ],

    "green"

    ),



    "Yellow Line":

    (

    [

    [12.8399,77.6770],

    [12.9165,77.6101]

    ],

    "orange"

    ),



    "Pink Line":

    (

    [

    [12.9165,77.6101],

    [13.0430,77.6200]

    ],

    "pink"

    )

    }





    for name,(points,color) in lines.items():


        folium.PolyLine(

        points,

        color=color,

        weight=7,

        tooltip=name

        ).add_to(metro_map)







    for name,data in station_data.items():


        if name==selected:


            folium.Marker(

            data["location"],

            popup=name,

            icon=folium.Icon(

            color="red",

            icon="train"

            )

            ).add_to(metro_map)


        else:


            folium.CircleMarker(

            data["location"],

            radius=6,

            popup=name,

            fill=True

            ).add_to(metro_map)





    st_folium(

    metro_map,

    width=1100,

    height=650

    )









# =====================================================
# CONNECTIVITY MODULE
# =====================================================


with connect_tab:


    st.subheader(

    "📍 Metro Connectivity Intelligence"

    )



    if area_df.empty:


        st.warning(
        "Area score data unavailable"
        )



    else:


        area = st.selectbox(

        "Choose Area",

        area_df.area

        )



        row = area_df[

        area_df.area==area

        ].iloc[0]



        a,b,c=st.columns(3)



        a.metric(

        "Metro Score",

        row.metro_score

        )


        b.metric(

        "Traffic Score",

        row.traffic_score

        )


        c.metric(

        "Area Score",

        row.area_score

        )









# =====================================================
# TRAVEL ANALYSIS
# =====================================================


with time_tab:


    st.subheader(

    "⏱ Travel Time Analysis"

    )



    distance = st.slider(

    "Distance KM",

    1,

    60,

    20

    )



    peak = st.checkbox(

    "Peak Traffic"

    )



    car = distance*3



    if peak:

        car+=25



    metro = distance*2



    saved = car-metro




    a,b,c=st.columns(3)



    a.metric(

    "Car",

    f"{car} min"

    )


    b.metric(

    "Metro",

    f"{metro} min"

    )


    c.metric(

    "Saved",

    f"{saved} min"

    )









# =====================================================
# ALERT MODULE
# =====================================================


with alert_tab:


    st.subheader(

    "⚠️ Metro Disruption Alerts"

    )



    st.dataframe(

    alerts,

    use_container_width=True

    )



    line=st.selectbox(

    "Select Line",

    alerts.Line

    )



    data=alerts[

    alerts.Line==line

    ].iloc[0]



    if data.Status=="Normal":


        st.success(
        "🟢 Service Normal"
        )


    elif data.Status=="Minor Delay":


        st.warning(

        f"Delay {data.Delay} minutes"

        )


    elif data.Status=="Maintenance":


        st.error(
        "🔴 Maintenance Ongoing"
        )


    else:


        st.info(
        "🚧 Upcoming Metro Expansion"
        )