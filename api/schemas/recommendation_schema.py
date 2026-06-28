from pydantic import BaseModel



class RecommendationRequest(BaseModel):

    salary:int

    rent_percentage:int = 40