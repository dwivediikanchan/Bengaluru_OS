import re



def analyze_resume(text):


    skills = [

        "python",
        "sql",
        "machine learning",
        "aws",
        "docker",
        "fastapi",
        "tensorflow",
        "pandas",
        "numpy",
        "power bi"

    ]



    found = []



    text = text.lower()



    for skill in skills:


        if skill in text:


            found.append(skill)



    missing = [

        "aws",
        "docker",
        "fastapi"

    ]



    missing = [

        skill

        for skill in missing

        if skill not in found

    ]



    return {


        "skills_found": found,


        "missing_skills": missing,


        "recommendation":

        "Focus on cloud, deployment and ML engineering skills"

    }