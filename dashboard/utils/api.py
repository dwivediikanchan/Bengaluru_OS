import requests



BASE_URL = "http://127.0.0.1:8000/api"



def get_api(endpoint):


    response = requests.get(

        f"{BASE_URL}/{endpoint}"

    )


    return response.json()