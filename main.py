import requests
from datetime import datetime
import os

# Placeholder values for demonstration
WEIGHT_KG = 70  # Example weight
HEIGHT_CM = 175  # Example height
AGE = 25  # Example age

today = datetime.now()

APPLICATION_ID = os.environ.get("APPLICATION_ID").strip()
API_KEY = os.environ.get("API_KEY").strip()


EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT").strip()

TOKEN = os.environ.get("TOKEN").strip()


# ------------------- Making a request for the Natural Language Processing API -------------------- #

e_headers = {
    "Content-Type": 'application/json',
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY
}

e_parameters = {
    "query": input("How did you exercise today?: "),
    "gender": "female",
    'weight_kg': WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

e_response = requests.post(url=EXERCISE_ENDPOINT, json=e_parameters, headers=e_headers)
result = e_response.json()


# ------------------- Making a request for the Sheety API  -------------------- #


""" Getting today's date and time for the parameters """

today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
      "workout": {
          "date": today_date,
          "time": today_time,
          "exercise": exercise["name"].title(),
          "duration": exercise["duration_min"],
          "calories": exercise["nf_calories"]
        }
    }


s_headers = {
    "Authorization": f"Basic {TOKEN}"
}

s_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=s_headers)

print(s_response.text)

