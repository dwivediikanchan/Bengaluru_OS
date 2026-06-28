from ml_models.rent_prediction.predict import predict_rent



rent = predict_rent(

    "Whitefield",

    2,

    1.5

)


print(
    "Predicted Rent:",
    rent
)