import folium
from streamlit_folium import st_folium



def show_map(df):


    m = folium.Map(

        location=[12.9716, 77.5946],

        zoom_start=11

    )



    for _, row in df.iterrows():


        if (

            "latitude" in df.columns

            and

            "longitude" in df.columns

        ):


            folium.Marker(

                [

                    row["latitude"],

                    row["longitude"]

                ],

                popup=f"""

                Area: {row['area']}

                Score: {row.get('area_score','N/A')}

                """

            ).add_to(m)



    st_folium(

        m,

        width=900,

        height=600

    )