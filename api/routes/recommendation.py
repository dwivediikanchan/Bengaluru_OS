from fastapi import APIRouter, HTTPException

from api.services.recommendation_service import get_recommendation



router = APIRouter()



@router.get("/recommend")
def recommend(max_rent: int, priority: str):

    try:

        result = get_recommendation(
            max_rent,
            priority
        )

        return result


    except Exception as e:

        print("ERROR:", e)

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )