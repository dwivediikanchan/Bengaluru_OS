from database.connection import get_connection

from genai.chatbot import ask_city_ai




def get_smart_recommendation(data):


    budget = data.get(

        "budget",

        0

    )


    profession = data.get(

        "profession",

        ""

    )


    preference = data.get(

        "preference",

        []

    )



    conn = get_connection()



    df = conn.execute(

    """

    SELECT

        area,

        rent_score,

        traffic_score,

        metro_score,

        weather_score,

        civic_score,

        area_score

    FROM area_score

    """

    ).fetchdf()



    conn.close()



    if df.empty:


        return {


            "message": "No area data available"

        }




    df["final_score"] = df["area_score"]




    if "Metro Connectivity" in preference:


        df["final_score"] += (

            df["metro_score"] * 0.2

        )



    if "Low Traffic" in preference:


        df["final_score"] += (

            df["traffic_score"] * 0.2

        )



    if "Low Rent" in preference:


        df["final_score"] += (

            df["rent_score"] * 0.2

        )




    result = df.sort_values(

        by="final_score",

        ascending=False

    ).head(3)




    recommendations = []



    for _, row in result.iterrows():



        prompt = f"""

Explain why {row['area']} is a good Bengaluru recommendation.



Area Score:
{row['final_score']}



Rent Score:
{row['rent_score']}



Traffic Score:
{row['traffic_score']}



Metro Score:
{row['metro_score']}



Profession:
{profession}



User Preference:
{preference}



Give a short practical explanation.

"""



        explanation = ask_city_ai(

            prompt

        )




        recommendations.append(

        {


            "area":

            row["area"],



            "score":

            round(

                float(row["final_score"]),

                2

            ),



            "ai_explanation":

            explanation

        }

        )



    return {


        "top_recommendations":

        recommendations

    }