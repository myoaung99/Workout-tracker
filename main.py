import requests
import json
import datetime as dt
from requests.api import head

APP_KEY = "0f071914677de40f241e02e244fa427a"
APP_ID = "03d83ae5"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_POST_ENDPOINT = "https://api.sheety.co/512281c0f92b08daff1844bf687d7a88/workoutTracking/workouts"

# q = input("Tell me how did you exercise today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
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

for i in range(0, len(result["exercises"])):
    date = dt.datetime.today().strftime("%Y/%m/%d")
    time = dt.datetime.now().time().strftime("%H:%M:%S")
    exercise = result["exercises"][i]["name"].title()
    duration = result["exercises"][i]["duration_min"]
    calories = result["exercises"][i]["nf_calories"]

    # print(
    #     f"Now: {date}\nTime: {time}\nExercise: {exercise}\nDuration: {duration}\nCalories: {calories}")

    body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }

    response = requests.post(url=SHEETY_POST_ENDPOINT,
                             params=json.dumps(body, separators=(',', ':')))
    status_from_post = response.text

print(status_from_post)
