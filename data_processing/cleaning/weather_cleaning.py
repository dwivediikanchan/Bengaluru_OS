import pandas as pd
import os


def clean_weather():

    input_file = (
        "data/raw/weather/weather.csv"
    )

    output_file = (
        "data/cleaned/weather_clean.csv"
    )


    os.makedirs(
        "data/cleaned",
        exist_ok=True
    )


    df = pd.read_csv(
        input_file
    )


    print(
        "Original rows:",
        len(df)
    )


    # clean columns

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )


    # remove duplicates

    df = df.drop_duplicates()



    # area cleaning

    if "area" in df.columns:

        df["area"] = (
            df["area"]
            .astype(str)
            .str.lower()
            .str.strip()
        )


    # numeric conversion

    numeric_cols = [

        "temperature",

        "rain_probability",

        "humidity"

    ]


    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(

                df[col],

                errors="coerce"

            )


    df = df.dropna()



    df.to_csv(

        output_file,

        index=False

    )


    print(
        "Weather cleaned successfully"
    )


    print(
        "Rows after cleaning:",
        len(df)
    )



clean_weather()