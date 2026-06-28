from fastapi import APIRouter, Query
from api.services.explanation_service import explain_area



router = APIRouter()



@router.get("/explain-area")
def explain_area_api(area: str = Query(...)):

    return {
        "area": area,
        "reason": explain_area(area)
    }