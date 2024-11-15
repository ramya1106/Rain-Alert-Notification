# Rain Alert Notification System

This project is a Python-based application that sends SMS alerts to users if it's going to rain in their location. It uses the OpenWeatherMap API to check weather conditions and Twilio for sending SMS notifications.

---

## Features

- Fetches weather data for a specified location using the OpenWeatherMap API.
- Sends an SMS alert if rain is detected.
- Allows configuration of sensitive data (API keys, phone numbers) via environment variables for better security.

---

## Requirements

- Python 3.7 or higher
- An active OpenWeatherMap API key
- Twilio account SID and Auth Token
- Environment variables for secure handling of API keys and phone numbers

---

## Installation

1. Clone this repository:

       git clone https://github.com/your-username/rain-alert.git
       cd rain-alert
   
2. Install the required Python libraries:

       pip install -r requirements.txt

3. Set up environment variables:

  - Create a .env file in the project directory or configure environment variables in your system.

        export API_KEY="your_openweathermap_api_key"
        export FROM_NUM="+your_twilio_phone_number"
        export TO_NUM="+recipient_phone_number"

