import pandas as pd

from database.connection import get_connection




def get_area_intelligence():


    conn = get_connection()



    # -------------------------
    # Load data
    # -------------------------


    housing = conn.execute(
        """
        SELECT *
        FROM housing
        """
    ).fetchdf()



    traffic = conn.execute(
        """
        SELECT *
        FROM traffic
        """
    ).fetchdf()



    jobs = conn.execute(
        """
        SELECT *
        FROM jobs
        """
    ).fetchdf()



    civic = conn.execute(
        """
        SELECT *
        FROM civic
        """
    ).fetchdf()



    weather = conn.execute(
        """
        SELECT *
        FROM weather
        """
    ).fetchdf()



    conn.close()



    # -------------------------
    # Normalize area names
    # -------------------------


    housing["area"] = (
        housing["area"]
        .astype(str)
        .str.lower()
        .str.strip()
    )



    traffic["area"] = (
        traffic["area"]
        .astype(str)
        .str.lower()
        .str.strip()
    )



    jobs["location"] = (
        jobs["location"]
        .astype(str)
        .str.lower()
        .str.strip()
    )



    civic["area"] = (
        civic["area"]
        .astype(str)
        .str.lower()
        .str.strip()
    )



    weather["area"] = (
        weather["area"]
        .astype(str)
        .str.lower()
        .str.strip()
    )



    # rename jobs column

    jobs = jobs.rename(
        columns={
            "location":"area"
        }
    )



    # -------------------------
    # Merge all intelligence
    # -------------------------


    df = housing.merge(

        traffic,

        on="area",

        how="left"

    )



    df = df.merge(

        jobs,

        on="area",

        how="left"

    )



    df = df.merge(

        civic,

        on="area",

        how="left"

    )



    df = df.merge(

        weather,

        on="area",

        how="left"

    )



    # -------------------------
    # Convert numbers
    # -------------------------


    numeric_columns = [

        "rent",

        "salary",

        "avg_speed",

        "complaint_count",

        "temperature"

    ]



    for col in numeric_columns:


        if col not in df.columns:

            df[col] = 0


        df[col] = pd.to_numeric(

            df[col],

            errors="coerce"

        )



    df = df.fillna(0)



    # -------------------------
    # Area score
    # -------------------------


    df["area_score"] = (

        (df["salary"] / 1000)

        +

        (df["avg_speed"] * 2)

        -

        (df["rent"] / 1000)

        -

        (df["complaint_count"] * 2)

    )



    # -------------------------
    # Coordinates
    # -------------------------


    coordinates = {


        "hsr layout":

        (12.9116,77.6389),


        "whitefield":

        (12.9698,77.7500),


        "electronic city":

        (12.8399,77.6770),


        "koramangala":

        (12.9352,77.6245),


        "indiranagar":

        (12.9784,77.6408),


        "marathahalli":

        (12.9591,77.6974)

    }



    df["latitude"] = df["area"].apply(

        lambda x:

        coordinates.get(

            x,

            (12.9716,77.5946)

        )[0]

    )



    df["longitude"] = df["area"].apply(

        lambda x:

        coordinates.get(

            x,

            (12.9716,77.5946)

        )[1]

    )



    # sort best areas

    df = df.sort_values(

        by="area_score",

        ascending=False

    )



    return df