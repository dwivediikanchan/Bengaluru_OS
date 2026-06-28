import pandas as pd
import os


def clean_jobs():

    input_file = "data/raw/jobs/jobs.csv"

    output_folder = "data/cleaned"

    output_file = (
        "data/cleaned/jobs_clean.csv"
    )


    # create folder automatically

    os.makedirs(
        output_folder,
        exist_ok=True
    )


    df = pd.read_csv(
        input_file
    )


    # remove duplicates

    df = df.drop_duplicates()


    # clean column names

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )


    # clean skills column

    if "skills" in df.columns:

        df["skills"] = (
            df["skills"]
            .astype(str)
            .str.lower()
            .str.strip()
        )


    # remove missing values

    df = df.dropna()



    df.to_csv(
        output_file,
        index=False
    )


    print(
        "Jobs cleaned successfully"
    )


    print(
        f"Rows after cleaning: {len(df)}"
    )



clean_jobs()