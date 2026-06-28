import streamlit as st
import pandas as pd
import plotly.express as px


import sys
import os


ROOT=os.path.abspath(

    os.path.join(

        os.path.dirname(__file__),

        "../.."

    )

)


sys.path.append(ROOT)


from database.connection import get_connection





st.set_page_config(

page_title="Civic Intelligence",

page_icon="🏛️",

layout="wide"

)





st.title("🏛 Bengaluru Civic Intelligence")


st.write(

"""
Smart civic problem analysis system.

Understand Bengaluru infrastructure,
complaints and living quality.
"""

)







# ==========================================
# LOAD CIVIC DATA
# ==========================================


@st.cache_data
def load_civic():


    conn=get_connection()



    df=conn.execute(

    """

    SELECT

    area,

    complaint_type,

    complaint_count,

    status


    FROM civic


    """

    ).fetchdf()



    conn.close()


    return df





civic_df=load_civic()





if civic_df.empty:


    st.error(
    "Civic data unavailable"
    )

    st.stop()








# ==========================================
# CIVIC SCORE
# ==========================================


area_issue = civic_df.groupby(

"area"

)["complaint_count"].sum().reset_index()



def calculate_score(count):


    if count > 100:

        return 40


    elif count > 50:

        return 65


    else:

        return 90





area_issue["civic_score"] = area_issue.complaint_count.apply(

calculate_score

)










# ==========================================
# TABS
# ==========================================


tab1,tab2,tab3,tab4,tab5 = st.tabs(

[

"🏙 Civic Overview",

"📢 Civic Issues",

"📊 Civic Analysis",

"🏠 Living Quality",

"⚠ Alerts"

]

)









# ==========================================
# CIVIC OVERVIEW
# ==========================================


with tab1:


    st.subheader(

    "🏙 Area Civic Status"

    )



    area=st.selectbox(

    "Select Area",

    area_issue.area

    )



    row=area_issue[

    area_issue.area==area

    ].iloc[0]




    a,b,c=st.columns(3)



    a.metric(

    "Total Complaints",

    row.complaint_count

    )



    b.metric(

    "Civic Score",

    f"{row.civic_score}/100"

    )



    c.metric(

    "Area",

    area

    )




    if row.civic_score>=80:


        st.success(

        "🟢 Good civic condition"

        )


    elif row.civic_score>=60:


        st.warning(

        "🟡 Moderate civic issues"

        )


    else:


        st.error(

        "🔴 High civic problems"

        )









# ==========================================
# CIVIC ISSUES INTELLIGENCE
# ==========================================


with tab2:


    st.subheader(

    "📢 Civic Issues Intelligence"

    )


    st.write(

    """

    Analyze Bengaluru civic problems:

    🛣 Roads

    🚰 Water

    🗑 Garbage

    💡 Electricity

    🌊 Drainage

    🏗 Infrastructure


    """

    )




    issue_data = civic_df.groupby(

    "complaint_type"

    )["complaint_count"].sum().reset_index()



    issue_data = issue_data.sort_values(

    "complaint_count",

    ascending=False

    )




    fig = px.bar(

    issue_data,

    x="complaint_type",

    y="complaint_count",

    color="complaint_count",

    title="Civic Problem Distribution"

    )



    st.plotly_chart(

    fig,

    use_container_width=True

    )






    st.divider()



    selected_issue = st.selectbox(

    "Select Civic Issue",

    issue_data.complaint_type

    )




    issue_area = civic_df[

    civic_df.complaint_type==selected_issue

    ]



    total = issue_area.complaint_count.sum()



    affected = issue_area.area.nunique()



    c1,c2,c3 = st.columns(3)



    c1.metric(

    "Total Problems",

    total

    )



    c2.metric(

    "Affected Areas",

    affected

    )


    c3.metric(

    "Issue",

    selected_issue

    )





    st.subheader(

    "📍 Most Affected Areas"

    )




    affected_area = issue_area.sort_values(

    "complaint_count",

    ascending=False

    ).head(5)




    for _,item in affected_area.iterrows():


        if item.complaint_count > 50:


            st.error(

f"""

🔴 High Severity


Area:

{item.area}


Complaints:

{item.complaint_count}


Status:

{item.status}

"""

            )


        else:


            st.warning(

f"""

🟡 Issue Detected


Area:

{item.area}


Complaints:

{item.complaint_count}


Status:

{item.status}

"""

            )







    st.subheader(

    "💡 Civic Solution Insight"

    )



    issue = selected_issue.lower()



    if "road" in issue:


        st.info(

        "Improve road maintenance and pothole repair."

        )


    elif "water" in issue:


        st.info(

        "Improve water supply monitoring."

        )


    elif "garbage" in issue:


        st.info(

        "Increase waste collection frequency."

        )


    else:


        st.info(

        "Monitor issue areas and improve civic response."

        )









# ==========================================
# CIVIC ANALYSIS
# ==========================================


with tab3:


    st.subheader(

    "📊 Civic Problem Analysis"

    )



    fig = px.bar(

    area_issue,

    x="area",

    y="complaint_count",

    color="civic_score",

    title="Area Wise Civic Problems"

    )


    st.plotly_chart(

    fig,

    use_container_width=True

    )









# ==========================================
# LIVING QUALITY
# ==========================================


with tab4:


    st.subheader(

    "🏠 Civic Living Quality"

    )



    best = area_issue.sort_values(

    "civic_score",

    ascending=False

    )



    st.success(

f"""

Best Civic Areas:


{list(best.head(3).area)}


"""

    )



    selected = st.selectbox(

    "Compare Area",

    best.area,

    key="living"

    )



    row = best[

    best.area==selected

    ].iloc[0]



    st.metric(

    "Living Civic Score",

    f"{row.civic_score}/100"

    )









# ==========================================
# ALERTS
# ==========================================


with tab5:


    st.subheader(

    "⚠ Civic Alerts"

    )



    for _,row in area_issue.iterrows():



        if row.complaint_count>100:


            st.error(

f"""

🔴 Critical Civic Area


{row.area}


Problems:

{row.complaint_count}

"""

            )


        elif row.complaint_count>50:


            st.warning(

f"""

🟡 Needs Attention


{row.area}


Problems:

{row.complaint_count}

"""

            )


        else:


            st.success(

f"""

🟢 Stable


{row.area}

"""

            )




st.divider()


st.caption(

"🏛 Civic Intelligence | Bengaluru OS"

)