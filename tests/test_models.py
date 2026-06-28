import os



def test_ml_models_exist():


    models = [

        "ml_models/rent_prediction/model.pkl",

        "ml_models/salary_prediction/model.pkl",

        "ml_models/traffic_forecasting/model.pkl",

        "ml_models/skill_forecasting/model.pkl"

    ]


    for model in models:


        assert os.path.exists(model)