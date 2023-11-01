import streamlit as st
import requests

# OpenWeatherMap API key (replace with your own key)
api_key = "f68cd9c5b8108939e167bab9fba5d8c1"

# Create a Streamlit web app
st.title("Weather App")

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# User input for city name
city_name = st.text_input("Enter a city name:")
if city_name:
    weather_data = get_weather(city_name, api_key)

    if weather_data["cod"] == 200:
        # Display current weather information
        st.write(f"Current Weather in {city_name}:")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Condition: {weather_data['weather'][0]['description']}")

        # Display a five-day weather forecast (you can customize this)
        st.write("Five-Day Weather Forecast:")
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        forecast_params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # Change to "imperial" for Fahrenheit
        }
        forecast_response = requests.get(forecast_url, params=forecast_params)
        forecast_data = forecast_response.json()
        for day in forecast_data["list"]:
            st.write(f"Date: {day['dt_txt']}, Temperature: {day['main']['temp']}°C, Condition: {day['weather'][0]['description']}")

    else:
        st.write(f"City not found: {city_name}")

# Display interesting weather facts
st.write("Interesting Weather Facts:")
st.write("- Lightning can make the air five times hotter than the sun's surface.")
st.write("- The world's largest snowflake was 15 inches wide and 8 inches thick.")
st.write("- The hottest temperature ever recorded on Earth was 134°F (56.7°C) in Death Valley, California.")

# Note: This example provides only basic functionality. You can extend it with more features and data as needed.
