import requests
import os
import datetime as dt
from requests.api import head

# APP_KEY = "0f071914677de40f241e02e244fa427a"
# APP_ID = "03d83ae5"
# TOKEN = "Bearer adjfalsdjfalksjfajdfajslkfjaskfjijijwefjefKJKALKLDJFLAKSDJFLKAJFKJADKD"
APP_ID = os.environ["03d83ae5"]
API_KEY = os.environ["0f071914677de40f241e02e244fa427a"]
TOKEN = os.environ["Bearer adjfalsdjfalksjfajdfajslkfjaskfjijijwefjefKJKALKLDJFLAKSDJFLKAJFKJADKD"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_POST_ENDPOINT = "https://api.sheety.co/512281c0f92b08daff1844bf687d7a88/workoutTracking/workouts"

# q = input("Tell me how did you exercise today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = {
    "query": "run 3k and cyclying 5 miles",
    "gender": "male",
    "weight_kg": 54.43,
    "height_cm": 170.18,
    "age": 21
}

response = requests.post(url=EXERCISE_ENDPOINT, json=data, headers=headers)
result = response.json()
print(result)

for i in range(0, len(result["exercises"])):
    date = dt.datetime.today().strftime("%Y/%m/%d")
    time = dt.datetime.now().time().strftime("%H:%M:%S")
    exercise = result["exercises"][i]["name"].title()
    duration = result["exercises"][i]["duration_min"]
    calories = result["exercises"][i]["nf_calories"]

    body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }

    headers = {
        "Authorization": TOKEN
    }

    response = requests.post(url=SHEETY_POST_ENDPOINT,
                             json=body, headers=headers)
    status_from_post = response.text

print(status_from_post)
