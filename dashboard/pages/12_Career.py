import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


st.set_page_config(

    page_title="Career Intelligence",

    page_icon="💼",

    layout="wide"

)


st.title("💼 Bengaluru Career Intelligence")


st.markdown("""

### AI powered career growth platform


Understand:

- 🔥 Future skills

- 💰 Salary growth

- 📈 Industry demand

- 🎯 Career roadmap


""")



# =====================================================
# CAREER DATA
# =====================================================


career_df = pd.DataFrame({

"Industry":[

"Artificial Intelligence",

"Data Science",

"Software Development",

"Cloud Computing",

"Cyber Security",

"EV Technology",

"FinTech",

"Healthcare Tech"

],


"Demand":[

95,

90,

92,

85,

80,

75,

82,

78

],


"Salary Growth":[

35,

32,

30,

28,

25,

22,

27,

24

]

})




# =====================================================
# TABS
# =====================================================


tab1,tab2,tab3,tab4 = st.tabs([


"📊 Career Dashboard",

"🔥 Trending Skills",

"💰 Salary Intelligence",

"🎯 Career Roadmap",




])



# =====================================================
# TAB 1
# CAREER DASHBOARD
# =====================================================


with tab1:


    st.subheader(
        "📊 Bengaluru Job Market Intelligence"
    )


    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "Top Industry",

        "AI"

    )


    c2.metric(

        "Demand Score",

        "95/100"

    )


    c3.metric(

        "Salary Growth",

        "+35%"

    )


    c4.metric(

        "Future Outlook",

        "Excellent"

    )


    st.divider()



    fig = px.bar(

        career_df,

        x="Industry",

        y="Demand",

        color="Demand",

        title="Industry Demand Forecast"

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



    st.subheader(

        "🔥 Best Career Opportunities"

    )


    top = career_df.sort_values(

        "Demand",

        ascending=False

    ).head(5)



    for _,row in top.iterrows():


        st.success(

f"""

### 🚀 {row['Industry']}


Demand:

{row['Demand']}/100


Salary Growth:

+{row['Salary Growth']}%


Career Outlook:

★★★★★

"""

        )
# =====================================================
# TAB 2
# TRENDING SKILLS INTELLIGENCE
# =====================================================


with tab2:


    st.subheader("🔥 Future Skills Intelligence")


    st.write(

        "Discover the most valuable skills for Bengaluru's future job market."

    )


    st.divider()



    # ---------------------------------
    # Skill Data
    # ---------------------------------


    skills_df = pd.DataFrame({

        "Skill":[

            "Generative AI",

            "Machine Learning",

            "Data Analytics",

            "Cloud Computing",

            "Full Stack Development",

            "Cyber Security",

            "MLOps",

            "EV Technology",

            "Robotics",

            "Blockchain"

        ],


        "Demand":[

            98,

            95,

            90,

            88,

            86,

            82,

            85,

            75,

            78,

            70

        ],


        "Difficulty":[

            "Advanced",

            "Advanced",

            "Medium",

            "Medium",

            "Medium",

            "Advanced",

            "Advanced",

            "Medium",

            "Advanced",

            "Advanced"

        ]

    })



    # ---------------------------------
    # Skill Ranking Chart
    # ---------------------------------


    fig = px.bar(

        skills_df,

        x="Skill",

        y="Demand",

        color="Demand",

        title="Future Skill Demand"

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
    # Top Skills Cards
    # ---------------------------------


    st.subheader(

        "🚀 Top Skills To Learn"

    )



    top_skills = skills_df.sort_values(

        "Demand",

        ascending=False

    ).head(5)



    for _,row in top_skills.iterrows():


        st.success(

f"""

## ⭐ {row['Skill']}


Future Demand:

{row['Demand']}/100


Difficulty:

{row['Difficulty']}


Career Impact:

★★★★★


AI Recommendation:

High priority skill for Bengaluru job market.

"""

        )



    st.divider()



    # ---------------------------------
    # Skill Gap Analyzer
    # ---------------------------------


    st.subheader(

        "🎯 Skill Gap Analyzer"

    )



    current_skill = st.selectbox(

        "Your Current Skill",

        [

            "Python",

            "Java",

            "SQL",

            "Web Development",

            "Data Science",

            "None"

        ],

        key="current_skill"

    )



    target = st.selectbox(

        "Target Career",

        [

            "AI Engineer",

            "Data Scientist",

            "Cloud Engineer",

            "Full Stack Developer",

            "Cyber Security Analyst"

        ],

        key="target_skill"

    )



    roadmap = {


        "AI Engineer":[

            "Python",

            "Machine Learning",

            "Deep Learning",

            "Generative AI",

            "MLOps"

        ],


        "Data Scientist":[

            "Python",

            "Statistics",

            "SQL",

            "Machine Learning",

            "Visualization"

        ],


        "Cloud Engineer":[

            "Linux",

            "AWS",

            "Docker",

            "Kubernetes",

            "DevOps"

        ],


        "Full Stack Developer":[

            "HTML",

            "React",

            "Backend",

            "Database",

            "System Design"

        ],


        "Cyber Security Analyst":[

            "Networking",

            "Security",

            "Linux",

            "Ethical Hacking"

        ]

    }



    st.info(

f"""

## 🤖 AI Skill Roadmap


Current Skill:

**{current_skill}**


Target:

**{target}**



Recommended Learning Path:


"""

    )


    for skill in roadmap[target]:


        st.write(

            "➡️ " + skill

        )



    st.success(

        "Follow this roadmap to become job-ready."

    )
# =====================================================
# TAB 3
# SALARY INTELLIGENCE
# =====================================================


with tab3:


    st.subheader("💰 Bengaluru Salary Intelligence")


    st.write(

        "Estimate salary growth based on role, experience and future demand."

    )


    st.divider()



    # ---------------------------------
    # Inputs
    # ---------------------------------


    c1,c2 = st.columns(2)



    with c1:


        role = st.selectbox(

            "💼 Select Role",

            [

                "Software Engineer",

                "Data Scientist",

                "AI Engineer",

                "Cloud Engineer",

                "Full Stack Developer",

                "Cyber Security Analyst"

            ],

            key="salary_role"

        )



    with c2:


        experience = st.slider(

            "📈 Experience (Years)",

            0,

            15,

            2,

            key="experience"

        )



    current_salary = st.slider(

        "💰 Current Salary (LPA)",

        2,

        80,

        8,

        key="current_salary"

    )



    # ---------------------------------
    # Salary Prediction Engine
    # ---------------------------------


    role_factor = {


        "Software Engineer":1.35,


        "Data Scientist":1.45,


        "AI Engineer":1.60,


        "Cloud Engineer":1.40,


        "Full Stack Developer":1.30,


        "Cyber Security Analyst":1.38

    }



    future_salary = round(

        current_salary

        *

        role_factor[role]

        *

        (1 + experience*0.05),

        2

    )



    growth_percent = round(

        ((future_salary-current_salary)

        /

        current_salary)

        *

        100,

        1

    )



    st.divider()



    s1,s2,s3,s4 = st.columns(4)



    s1.metric(

        "Current Salary",

        f"{current_salary} LPA"

    )


    s2.metric(

        "Future Salary",

        f"{future_salary} LPA"

    )


    s3.metric(

        "Growth",

        f"+{growth_percent}%"

    )


    s4.metric(

        "Career Demand",

        "High"

    )



    st.progress(

        min(future_salary/100,1)

    )



    st.divider()



    # ---------------------------------
    # Salary Growth Chart
    # ---------------------------------


    years = list(

        range(

            2025,

            2036

        )

    )


    salary_projection=[]


    for y in years:


        diff = y-2025


        value = current_salary * (

            1 +

            diff*0.08

        )


        salary_projection.append(

            round(value,2)

        )



    fig = px.line(

        x=years,

        y=salary_projection,

        markers=True,

        title=f"{role} Salary Projection"

    )


    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="Salary LPA",

        height=450

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # ---------------------------------
    # Role Comparison
    # ---------------------------------


    st.subheader(

        "📊 Role Comparison"

    )


    comparison = pd.DataFrame({

        "Role":[

            "AI Engineer",

            "Data Scientist",

            "Cloud Engineer",

            "Software Engineer",

            "Full Stack"

        ],


        "Future Demand":[

            98,

            95,

            88,

            90,

            86

        ],


        "Salary Potential":[

            95,

            92,

            88,

            85,

            82

        ]

    })



    fig2 = px.scatter(

        comparison,

        x="Future Demand",

        y="Salary Potential",

        text="Role",

        size="Salary Potential",

        title="Career Opportunity Map"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )



    st.divider()



    st.success(

f"""

## 🤖 AI Salary Advice


Role:

**{role}**


Current Salary:

**{current_salary} LPA**


2035 Projection:

**{future_salary} LPA**


Recommendation:


Focus on high-demand skills and continuous learning
because Bengaluru's technology ecosystem will keep
increasing salary opportunities.

"""

    )
# =====================================================
# TAB 4
# CAREER ROADMAP + RESUME ANALYZER
# =====================================================


with tab4:


    st.subheader("🎯 AI Career Roadmap")


    st.write(

        "Create your career path or upload your resume for AI analysis."

    )


    st.divider()



    roadmap_tab, resume_tab = st.tabs([

        "🛣 Career Roadmap",

        "📄 Resume Analyzer"

    ])



    # =================================================
    # MANUAL ROADMAP
    # =================================================


    with roadmap_tab:


        current = st.selectbox(

            "Current Role",

            [

                "Student",

                "Software Developer",

                "Data Analyst",

                "Data Scientist",

                "Engineer",

                "Other"

            ],

            key="current_role"

        )



        target = st.selectbox(

            "Target Career",

            [

                "AI Engineer",

                "Data Scientist",

                "ML Engineer",

                "Cloud Engineer",

                "Full Stack Developer",

                "Cyber Security"

            ],

            key="target_role"

        )



        roadmap = {


        "AI Engineer":[

            "Python",

            "Statistics",

            "Machine Learning",

            "Deep Learning",

            "Generative AI",

            "MLOps"

        ],


        "Data Scientist":[

            "Python",

            "SQL",

            "Statistics",

            "Machine Learning",

            "Power BI"

        ],


        "ML Engineer":[

            "ML Algorithms",

            "Deep Learning",

            "Model Deployment",

            "Cloud",

            "Docker"

        ],


        "Cloud Engineer":[

            "Linux",

            "AWS",

            "Docker",

            "Kubernetes",

            "DevOps"

        ],


        "Full Stack Developer":[

            "HTML",

            "React",

            "Backend",

            "Database",

            "System Design"

        ],


        "Cyber Security":[

            "Networking",

            "Linux",

            "Security",

            "Ethical Hacking"

        ]

        }



        st.success(

f"""

## 🚀 Roadmap


From:

**{current}**


To:

**{target}**


Recommended Path:

"""

        )


        for step in roadmap[target]:


            st.write(

                "➡️ " + step

            )



        st.info(

            "Estimated preparation time: 6-12 months depending on consistency."

        )





    # =================================================
    # RESUME ANALYZER
    # =================================================


    with resume_tab:


        st.subheader(

            "📄 AI Resume Analyzer"

        )



        uploaded = st.file_uploader(

            "Upload Resume / Career Document",

            type=[

                "pdf",

                "docx",

                "txt"

            ]

        )



        if uploaded:


            st.success(

                "Document uploaded successfully."

            )


            text = ""



            if uploaded.type == "text/plain":


                text = uploaded.read().decode()



            else:


                text = str(uploaded)



            # Simple AI-style extraction


            skills = [

                "Python",

                "SQL",

                "Machine Learning",

                "Data Science",

                "AI",

                "Cloud",

                "React",

                "Java",

                "AWS",

                "Docker"

            ]



            found=[]


            for skill in skills:


                if skill.lower() in text.lower():

                    found.append(skill)



            st.divider()



            st.subheader(

                "🧠 Resume Intelligence"

            )



            c1,c2,c3 = st.columns(3)



            c1.metric(

                "Skills Detected",

                len(found)

            )


            c2.metric(

                "Career Strength",

                "High"

                if len(found)>5

                else "Medium"

            )


            c3.metric(

                "AI Match Score",

                f"{min(len(found)*12,95)}%"

            )



            st.divider()



            st.markdown(

                "### ✅ Detected Skills"

            )



            if found:


                for s in found:


                    st.success(s)


            else:


                st.warning(

                    "No major skills detected."

                )



            st.divider()



            missing = [

                "Generative AI",

                "System Design",

                "Cloud",

                "MLOps"

            ]



            st.markdown(

                "### 📈 Recommended Improvements"

            )



            for m in missing:


                st.info(

                    "Learn: " + m

                )



            st.success(

f"""

## 🤖 AI Career Analysis


Your profile shows potential for technology roles.


Recommended Growth Direction:


AI + Data + Cloud


Next Steps:


✓ Improve missing skills

✓ Build projects

✓ Gain practical experience

✓ Apply for targeted roles


"""

            )