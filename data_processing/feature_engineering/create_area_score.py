import pandas as pd
import os



# -------------------------
# Helper Function
# -------------------------

def clean_area(df):

    df["area"] = (
        df["area"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    return df



# -------------------------
# Create Output Folder
# -------------------------

os.makedirs(
    "data/processed",
    exist_ok=True
)



# -------------------------
# Load Data
# -------------------------


housing = clean_area(

    pd.read_csv(
        "data/cleaned/housing_clean.csv"
    )

)



traffic = clean_area(

    pd.read_csv(
        "data/cleaned/traffic_clean.csv"
    )

)



metro = clean_area(

    pd.read_csv(
        "data/raw/metro/metro.csv"
    )

)



weather = clean_area(

    pd.read_csv(
        "data/cleaned/weather_clean.csv"
    )

)



civic = clean_area(

    pd.read_csv(
        "data/cleaned/civic_clean.csv"
    )

)




# -------------------------
# Housing Score
# Lower rent = better
# -------------------------


rent = (

    housing
    .groupby("area")["rent"]
    .mean()
    .reset_index()

)



rent["rent_score"] = (

    100 -

    (

        (

        rent["rent"]

        -

        rent["rent"].min()

        )

        /

        (

        rent["rent"].max()

        -

        rent["rent"].min()

        )

        *100

    )

)




# -------------------------
# Traffic Score
# Higher speed = better
# -------------------------


traffic_score = (

    traffic
    .groupby("area")["avg_speed"]
    .mean()
    .reset_index()

)



traffic_score["traffic_score"] = (

    traffic_score["avg_speed"]

    /

    traffic_score["avg_speed"].max()

    *100

)




traffic_score = traffic_score[
    [
        "area",
        "traffic_score"
    ]
]





# -------------------------
# Metro Score
# -------------------------


metro["metro_score"] = (

    metro["connectivity_score"]

    /

    metro["connectivity_score"].max()

    *100

)



metro = metro[
    [
        "area",
        "metro_score"
    ]
]





# -------------------------
# Weather Score
# Less rain risk = better
# -------------------------


weather_score = (

    weather
    .groupby("area")["rain_probability"]
    .mean()
    .reset_index()

)



weather_score["weather_score"] = (

    100 -

    weather_score["rain_probability"]

)



weather_score = weather_score[
    [
        "area",
        "weather_score"
    ]
]






# -------------------------
# Civic Score
# Less complaints = better
# -------------------------


civic_score = (

    civic
    .groupby("area")["complaint_count"]
    .sum()
    .reset_index()

)



civic_score["civic_score"] = (

    100 -

    (

        civic_score["complaint_count"]

        /

        civic_score["complaint_count"].max()

        *100

    )

)



civic_score = civic_score[
    [
        "area",
        "civic_score"
    ]
]






# -------------------------
# Merge All Intelligence
# -------------------------


area = rent



area = area.merge(

    traffic_score,

    on="area",

    how="left"

)



area = area.merge(

    metro,

    on="area",

    how="left"

)



area = area.merge(

    weather_score,

    on="area",

    how="left"

)



area = area.merge(

    civic_score,

    on="area",

    how="left"

)




# -------------------------
# Handle Missing Values
# -------------------------


area = area.fillna(0)






# -------------------------
# Final Area Score
# -------------------------


area["area_score"] = (

    area["rent_score"] * 0.25

    +

    area["traffic_score"] * 0.25

    +

    area["metro_score"] * 0.20

    +

    area["weather_score"] * 0.15

    +

    area["civic_score"] * 0.15

)





# Sort Best Areas First


area = area.sort_values(

    by="area_score",

    ascending=False

)




# Save


area.to_csv(

    "data/processed/area_intelligence_score.csv",

    index=False

)




print(
    "Area Intelligence Created Successfully"
)


print(area)