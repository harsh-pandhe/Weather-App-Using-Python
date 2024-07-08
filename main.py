import tkinter as tk
from tkinter import messagebox
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

        # Display weather information in a message box
        result = (
            f"Weather in {location}:\n"
            f"Description: {weather_description}\n"
            f"Temperature: {temperature} °C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h"
        )
        messagebox.showinfo("Weather Report", result)
    elif response.status_code == 401:
        messagebox.showerror(
            "Error", "Unauthorized: Invalid API key or access restricted."
        )
    else:
        messagebox.showerror(
            "Error",
            f"Failed to fetch weather data for {city}. Error {response.status_code}.",
        )


def on_submit():
    city = city_entry.get()
    if city:
        fetch_weather(city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")


def main():
    global city_entry
    root = tk.Tk()
    root.title("Weather App")

    label = tk.Label(root, text="Enter city name:")
    label.pack(pady=10)

    city_entry = tk.Entry(root, width=30)
    city_entry.pack(pady=5)

    submit_btn = tk.Button(root, text="Fetch Weather", command=on_submit)
    submit_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
