from fastapi import APIRouter


from api.services.jobs_service import get_jobs_data




router = APIRouter()




@router.get("/jobs")

def jobs():


    return get_jobs_data()