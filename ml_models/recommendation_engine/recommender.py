import pandas as pd
import sys
from pathlib import Path



# -------------------------
# Add Project Root
# -------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]


sys.path.append(
    str(PROJECT_ROOT)
)



# -------------------------
# Database Import
# -------------------------

from database.connection import get_connection




def recommend_area(

    salary,

    max_rent_percentage=40

):


    conn = get_connection()



    # Get data from DuckDB

    df = conn.execute(

        """

        SELECT *

        FROM area_score

        """

    ).fetchdf()



    conn.close()




    # Calculate rent limit


    affordable_rent = (

        salary

        *

        max_rent_percentage

        /

        100

    )




    # Filter areas


    result = df[

        df["rent"]

        <=

        affordable_rent

    ]




    # If no area available

    if result.empty:


        result = df




    # Sort best areas


    result = result.sort_values(

        by="area_score",

        ascending=False

    )



    return result.head(5)






# -------------------------
# Test
# -------------------------

if __name__ == "__main__":


    recommendation = recommend_area(

        80000,

        40

    )


    print(

        recommendation

    )