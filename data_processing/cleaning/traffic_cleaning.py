import pandas as pd
import os


def clean_traffic():

    input_file = (
        "data/raw/traffic/traffic.csv"
    )


    output_folder = (
        "data/cleaned"
    )


    output_file = (
        "data/cleaned/traffic_clean.csv"
    )


    # create folder

    os.makedirs(
        output_folder,
        exist_ok=True
    )


    # load data

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



    # clean area

    if "area" in df.columns:

        df["area"] = (

            df["area"]
            .astype(str)
            .str.lower()
            .str.strip()

        )



    # clean speed

    if "avg_speed" in df.columns:

        df["avg_speed"] = pd.to_numeric(

            df["avg_speed"],

            errors="coerce"

        )



    # clean traffic level

    if "traffic_level" in df.columns:

        df["traffic_level"] = (

            df["traffic_level"]
            .astype(str)
            .str.lower()
            .str.strip()

        )



    # remove missing

    df = df.dropna()



    # save

    df.to_csv(

        output_file,

        index=False

    )



    print(
        "Traffic cleaned successfully"
    )


    print(
        "Rows after cleaning:",
        len(df)
    )



clean_traffic()