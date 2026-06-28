from fastapi import APIRouter


from api.services.housing_service import get_housing_data



router = APIRouter()



@router.get("/housing")


def housing():


    return get_housing_data()