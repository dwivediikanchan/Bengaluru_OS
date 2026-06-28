from fastapi import APIRouter
from api.services.area_intelligence_service import get_area_intelligence



router = APIRouter()



@router.get("/area-intelligence")
def area_intelligence():

    return get_area_intelligence().to_dict(
        orient="records"
    )