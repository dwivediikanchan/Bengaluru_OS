from fastapi import APIRouter, HTTPException


from api.services.salary_prediction_service import predict_salary



router = APIRouter()



@router.post("/predict-salary")

def salary_prediction(data: dict):


    try:


        result = predict_salary(

            data

        )


        return {


            "predicted_salary": result


        }


    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )