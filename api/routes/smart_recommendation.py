from fastapi import APIRouter, HTTPException


from api.services.smart_recommendation_service import get_smart_recommendation




router = APIRouter()




@router.post("/smart-recommendation")

def smart_recommendation(data: dict):


    try:


        result = get_smart_recommendation(

            data

        )


        return result



    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )