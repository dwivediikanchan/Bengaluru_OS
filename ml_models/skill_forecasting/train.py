import sys
import os


sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../.."

        )

    )

)



import joblib
import pandas as pd



from database.connection import get_connection



from collections import Counter




conn = get_connection()



df = conn.execute(

"""
SELECT skills

FROM jobs

"""

).fetchdf()



conn.close()




skill_list = []



for skills in df["skills"]:


    skills = str(skills).lower()


    items = skills.split(",")


    for skill in items:

        skill_list.append(

            skill.strip()

        )




skill_count = Counter(skill_list)



result = pd.DataFrame(

    skill_count.items(),

    columns=[

        "skill",

        "count"

    ]

)



result = result.sort_values(

    by="count",

    ascending=False

)




joblib.dump(

    result,

    "ml_models/skill_forecasting/model.pkl"

)



print(

    "Skill forecasting model created"

)



print(result.head())