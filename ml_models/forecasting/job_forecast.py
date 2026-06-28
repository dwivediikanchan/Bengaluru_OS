import pandas as pd
from prophet import Prophet


df = pd.read_csv(
    "data/raw/trends/job_trends.csv"
)


df["month"] = pd.to_datetime(
    df["month"] + "-2025"
)


df = df.rename(
    columns={
        "month":"ds",
        "job_count":"y"
    }
)


model = Prophet()


model.fit(df)


future = model.make_future_dataframe(
    periods=6,
    freq="ME"
)


forecast = model.predict(
    future
)


print(
    forecast[
        ["ds","yhat"]
    ].tail(6)
)