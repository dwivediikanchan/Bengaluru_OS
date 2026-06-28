import requests



BASE_URL = "http://127.0.0.1:8000"



def test_skill_api():


    response = requests.get(

        BASE_URL + "/api/skill-trends"

    )


    assert response.status_code == 200