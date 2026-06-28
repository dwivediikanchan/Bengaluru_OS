from fastapi import FastAPI


from api.routes import recommendation
from api.routes import housing
from api.routes import traffic
from api.routes import weather
from api.routes import civic
from api.routes import jobs
from api.routes import area_intelligence
from api.routes import explanation
from api.routes import city_chat
from api.routes import rent_prediction
from api.routes import salary_prediction
from api.routes import skill
from api.routes import smart_recommendation

app = FastAPI(

    title="Bengaluru Urban Intelligence API"

)



app.include_router(

    recommendation.router,

    prefix="/api"

)

app.include_router(

    housing.router,

    prefix="/api"

)

app.include_router(

    traffic.router,

    prefix="/api"

)

app.include_router(

    weather.router,

    prefix="/api"

)
app.include_router(

    civic.router,

    prefix="/api"

)
app.include_router(

    jobs.router,

    prefix="/api"

)
app.include_router(
    rent_prediction.router,
    prefix="/api"
)

app.include_router(
    area_intelligence.router,
    prefix="/api"
)
app.include_router(
    explanation.router,
    prefix="/api"
)
app.include_router(
    city_chat.router,
    prefix="/api"
)
app.include_router(

    salary_prediction.router,

    prefix="/api"

)
app.include_router(

    skill.router,

    prefix="/api"

)
app.include_router(

    smart_recommendation.router,

    prefix="/api"

)


@app.get("/")

def home():

    return {

        "message":

        "Bengaluru Intelligence API Running"

    }