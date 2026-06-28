from fastapi import APIRouter, HTTPException

from api.services.traffic_service import predict_traffic



router = APIRouter()



@router.post("/predict-traffic")

def traffic_prediction(data: dict):


    try:

        result = predict_traffic(data)


        return {

            "traffic_prediction": result

        }


    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )