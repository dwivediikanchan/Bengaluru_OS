import joblib

model = joblib.load(
    "ml_models/salary_prediction/model.pkl"
)

def predict_salary(
    experience,
    skill_count
):

    prediction = model.predict(
        [[experience,
          skill_count]]
    )

    return round(
        prediction[0],
        2
    )