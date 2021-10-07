import requests
from requests.api import head

APP_KEY = "0f071914677de40f241e02e244fa427a"
APP_ID = "03d83ae5"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# q = input("How did you do your exercise today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

data = {
    "query": "run 3 miles",
    "gender": "male",
    "weight_kg": 54.43,
    "height_cm": 170.18,
    "age": 21
}

response = requests.post(url=EXERCISE_ENDPOINT, json=data, headers=headers)
result = response.json()

print(result)
