import pandas as pd
import os


def clean_housing():

    input_file = (
        "data/raw/housing/housing.csv"
    )

    output_folder = (
        "data/cleaned"
    )

    output_file = (
        "data/cleaned/housing_clean.csv"
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


    # clean column names

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )


    # remove duplicates

    df = df.drop_duplicates()


    # clean area names

    if "area" in df.columns:

        df["area"] = (
            df["area"]
            .astype(str)
            .str.lower()
            .str.strip()
        )


    # clean rent column

    if "rent" in df.columns:

        df["rent"] = (

            df["rent"]
            .astype(str)
            .str.replace(
                ",",
                ""
            )

        )

        df["rent"] = pd.to_numeric(
            df["rent"],
            errors="coerce"
        )


    # clean bhk

    if "bhk" in df.columns:

        df["bhk"] = pd.to_numeric(
            df["bhk"],
            errors="coerce"
        )


    # remove missing

    df = df.dropna()


    # save cleaned data

    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Housing cleaned successfully"
    )


    print(
        "Rows after cleaning:",
        len(df)
    )



clean_housing()