from fastapi import APIRouter, HTTPException

from api.services.rent_prediction_service import predict_rent



router = APIRouter()



@router.post("/predict-rent")
def rent_prediction(data: dict):

    try:

        result = predict_rent(data)


        return {

            "predicted_rent": result

        }


    except Exception as e:


        print("ERROR:", e)


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )