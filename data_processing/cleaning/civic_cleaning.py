import pandas as pd
import os


def clean_civic():

    input_file = (
        "data/raw/civic/civic.csv"
    )


    output_file = (
        "data/cleaned/civic_clean.csv"
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


    df.columns = (

        df.columns
        .str.lower()
        .str.strip()

    )


    df = df.drop_duplicates()



    if "area" in df.columns:

        df["area"] = (

            df["area"]
            .astype(str)
            .str.lower()
            .str.strip()

        )



    if "complaint_count" in df.columns:

        df["complaint_count"] = pd.to_numeric(

            df["complaint_count"],

            errors="coerce"

        )



    if "status" in df.columns:

        df["status"] = (

            df["status"]
            .astype(str)
            .str.lower()
            .str.strip()

        )



    df = df.dropna()



    df.to_csv(

        output_file,

        index=False

    )



    print(
        "Civic cleaned successfully"
    )


    print(
        "Rows after cleaning:",
        len(df)
    )



clean_civic()