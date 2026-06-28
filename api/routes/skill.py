from fastapi import APIRouter


from api.services.skill_service import get_skill_trends



router = APIRouter()



@router.get("/skill-trends")

def skill_trends():


    return get_skill_trends()