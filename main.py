import requests


def fetch_weather(city):
    api_key = "0238391c95f54d84b1672008240807" 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        weather_description = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        print(f"Weather in {location}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
    elif response.status_code == 401:
        print("Unauthorized: Invalid API key or access restricted.")
    else:
        print(f"Failed to fetch weather data for {city}. Error {response.status_code}.")


def main():
    city = input("Enter city name: ")
    fetch_weather(city)


if __name__ == "__main__":
    main()
