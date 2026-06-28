from fastapi import APIRouter
from api.services.city_chat_service import city_chat

router = APIRouter()


@router.get("/city-chat")
def chat(query: str):
    return city_chat(query)