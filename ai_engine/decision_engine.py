print("🔥 FINAL SMART ENGINE LOADED")


class BengaluruDecisionEngine:


    def __init__(
        self,
        housing,
        metro,
        traffic,
        weather,
        jobs,
        civic
    ):

        self.housing = housing
        self.metro = metro
        self.traffic = traffic
        self.weather = weather
        self.jobs = jobs
        self.civic = civic



    def clean(self,x):

        return (
            str(x)
            .lower()
            .replace(" ","")
            .replace("-","")
        )



    def recommend_area(self, goal, priority):


        areas = self.metro["area"].unique()

        results=[]


        for area in areas:


            key=self.clean(area)


            score=0

            reasons=[]



            # --------------------------
            # HOUSING
            # --------------------------

            house=self.housing[

                self.housing["area"]
                .apply(self.clean)

                ==

                key

            ]


            if not house.empty:


                avg_rent=house["rent"].mean()



                if avg_rent <= 25000:

                    score+=25

                    reasons.append(
                        "🏠 Affordable housing"
                    )


                elif avg_rent <=35000:

                    score+=15

                    reasons.append(
                        "🏠 Balanced housing"
                    )


                else:

                    score+=8

                    reasons.append(
                        "🏠 Premium housing"
                    )




            # --------------------------
            # METRO
            # --------------------------


            metro=self.metro[

                self.metro["area"]
                .apply(self.clean)

                ==

                key

            ]



            if not metro.empty:


                conn_score = metro[
                    "connectivity_score"
                ].iloc[0]



                score += conn_score * 3


                reasons.append(

                    f"🚇 Connectivity {conn_score}/10"

                )





            # --------------------------
            # TRAFFIC
            # --------------------------


            traffic=self.traffic[

                self.traffic["area"]
                .apply(self.clean)

                ==

                key

            ]


            if not traffic.empty:


                speed=traffic["avg_speed"].mean()



                if speed >=30:


                    score+=20

                    reasons.append(
                        "🚗 Smooth traffic"
                    )


                elif speed>=20:


                    score+=10

                    reasons.append(
                        "🚦 Moderate traffic"
                    )


                else:


                    score-=5

                    reasons.append(
                        "🚦 Heavy traffic"
                    )





            # --------------------------
            # WEATHER
            # --------------------------


            weather=self.weather[

                self.weather["area"]
                .apply(self.clean)

                ==

                key

            ]


            if not weather.empty:


                rain=weather[
                    "rain_probability"
                ].iloc[0]



                if rain < 50:

                    score+=10

                    reasons.append(
                        "🌦 Comfortable weather"
                    )



                else:

                    score+=5





            # --------------------------
            # CIVIC
            # --------------------------


            civic=self.civic[

                self.civic["area"]
                .apply(self.clean)

                ==

                key

            ]


            if not civic.empty:


                complaints=civic[
                    "complaint_count"
                ].sum()



                if complaints <100:


                    score+=10

                    reasons.append(
                        "🏛 Good civic condition"
                    )



                else:

                    score-=5

                    reasons.append(
                        "🏛 Civic pressure"
                    )






            # --------------------------
            # GOAL INTELLIGENCE
            # --------------------------


            profiles={


                "whitefield":{

                    "career":25,
                    "investment":25,
                    "living":10

                },


                "electroniccity":{

                    "career":22,
                    "investment":18,
                    "living":20

                },


                "hsrlayout":{

                    "career":18,
                    "investment":15,
                    "living":25

                },


                "koramangala":{

                    "career":24,
                    "investment":18,
                    "living":25

                },


                "marathahalli":{

                    "career":12,
                    "investment":10,
                    "living":15

                }


            }



            profile=profiles.get(

                key,

                {}

            )



            if goal=="Best area for IT career":


                score += profile.get(
                    "career",
                    0
                )

                reasons.append(
                    "💼 Career ecosystem"
                )



            elif goal=="Best area to live":


                score += profile.get(
                    "living",
                    0
                )

                reasons.append(
                    "🏡 Livability"
                )



            elif goal=="Best investment area":


                score += profile.get(
                    "investment",
                    0
                )

                reasons.append(
                    "📈 Future growth"
                )



            elif goal=="Best connected area":


                score += profile.get(
                    "career",
                    0
                )

                reasons.append(
                    "🚇 Connectivity advantage"
                )




            results.append({

                "area":area,

                "score":round(score),

                "reasons":reasons

            })



        return sorted(

            results,

            key=lambda x:x["score"],

            reverse=True

        )