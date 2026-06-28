from fastapi import APIRouter


from api.services.civic_service import get_civic_data




router = APIRouter()




@router.get("/civic")

def civic():


    return get_civic_data()