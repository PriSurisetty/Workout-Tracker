# Workout Tracker

## Description

A workout tracking API project that records exercise data, including duration and calories burned, by integrating with the Nutritionix API and logs the data using Sheety.


[Watch the video](https://github.com/user-attachments/assets/ce531c4d-17be-495f-9c04-f2031df2c1a6)


![Workout-Tracker-Recording-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/205bf5b1-2a89-4a7f-a7b9-6e03b64f09bf)



## Features

- Records exercise details such as name, duration, and calories burned.
- Utilizes the Nutritionix API (A natural language processing API) to process exercise input.
- Logs exercise data to a Google Sheet via Sheety.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
2. **Install the required libraries:**
   ```bash
   pip install requests

3. **Set up environment variables:**

- APPLICATION_ID: Your Nutritionix API application ID.
- API_KEY: Your Nutritionix API key.
- SHEETY_ENDPOINT: The endpoint for your Sheety API.
- TOKEN: Authorization token for Sheety.

## Usage: 
1. Run the script:
   ```bash
   python workout_tracker.py

2. Input your exercise details when prompted:

  For example, if you enter Running when asked about your exercise, the script will:
  
  - Send a request to the Nutritionix API with the details of your exercise (e.g., "Running").
  - Receive the details from the API, such as the duration and calories burned.
  - Log this exercise data to your Google Sheet via the Sheety API, including:
  - The date and time of the exercise.
  - The name of the exercise.
  - The duration in minutes.
  - The number of calories burned.
  - The exercise data will be neatly organized in your Google Sheet for easy tracking.


## Example:

- When prompted with:
   ```bash
   How did you exercise today?: I ran for 30 minutes

The script will process the input and return information like:

Exercise: Running
Duration: 30 minutes
Calories: 300 kcal
This information is then logged to your Google Sheet with the current date and time.
