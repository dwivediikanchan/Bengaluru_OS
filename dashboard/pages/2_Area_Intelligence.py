import sys
import os


sys.path.insert(

    0,

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            "../../"

        )

    )

)



import streamlit as st
import pandas as pd



from dashboard.utils.api import get_data

from visualizations.area_charts import show_area_chart





st.title(

    "🏙️ Bengaluru Area Intelligence"

)





try:


    # Load directly from database

    df = get_data(

        "area_score"

    )



    if not df.empty:



        st.subheader(

            "📍 Area Performance"

        )



        st.dataframe(

            df,

            use_container_width=True

        )



        show_area_chart(

            df.to_dict(

                orient="records"

            )

        )



    else:


        st.warning(

            "No area data available"

        )





except Exception as e:


    st.error(

        f"Error loading area intelligence: {e}"

    )