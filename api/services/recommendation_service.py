import pandas as pd

from database.connection import get_connection



def get_recommendation(max_rent: int, priority: str):


    conn = get_connection()



    # Load tables

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



    # Rename jobs column

    jobs = jobs.rename(
        columns={
            "location":"area"
        }
    )



    # -------------------------
    # Merge data
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



    # -------------------------
    # Convert numeric values
    # -------------------------

    numeric_cols = [

        "rent",

        "salary",

        "avg_speed",

        "complaint_count"

    ]


    for col in numeric_cols:


        if col not in df.columns:

            df[col] = 0


        df[col] = pd.to_numeric(

            df[col],

            errors="coerce"

        )



    # Fill missing

    df = df.fillna(0)



    # -------------------------
    # Budget filter
    # -------------------------

    df = df[

        df["rent"] <= max_rent

    ]



    if df.empty:

        return []



    # -------------------------
    # Score calculation
    # -------------------------

    df["score"] = (

        (df["salary"] / 1000)

        +

        (df["avg_speed"] * 2)

        -

        (df["rent"] / 1000)

        -

        (df["complaint_count"] * 2)

    )



    # Make score positive

    minimum = df["score"].min()


    if minimum < 0:

        df["score"] = (

            df["score"]

            -

            minimum

        )



    # -------------------------
    # Sorting
    # -------------------------

    if "salary" in priority.lower():


        df = df.sort_values(

            by="salary",

            ascending=False

        )


    elif "traffic" in priority.lower():


        df = df.sort_values(

            by="avg_speed",

            ascending=False

        )


    else:


        df = df.sort_values(

            by="score",

            ascending=False

        )



    return df[

        [

            "area",

            "rent",

            "salary",

            "avg_speed",

            "score"

        ]

    ].head(5).to_dict(

        orient="records"

    )