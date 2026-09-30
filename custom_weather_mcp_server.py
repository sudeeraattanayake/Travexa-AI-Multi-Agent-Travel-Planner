from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv


load_dotenv()

mcp = FastMCP("Weather MCP Server")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


@mcp.tool()
def get_current_weather(city: str):

    if not OPENWEATHER_API_KEY:
        return {
            "error": "OPENWEATHER_API_KEY is missing."
        }

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": OPENWEATHER_API_KEY,
                "units": "metric"
            },
            timeout=15
        )

        data = response.json()

        if response.status_code != 200:
            return data

        return {
            "city": data["name"],
            "temperature_c": data["main"]["temp"],
            "feels_like_c": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }

    except requests.RequestException as exc:
        return {
            "error": f"Weather API request failed: {exc}"
        }

    except Exception as exc:
        return {
            "error": f"Weather data processing failed: {exc}"
        }


@mcp.tool()
def get_forecast(city: str):

    if not OPENWEATHER_API_KEY:
        return {
            "error": "OPENWEATHER_API_KEY is missing."
        }

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = response.json()

        if response.status_code != 200:
            return data

        forecast = []

        # Return first 5 forecast entries
        for item in data["list"][:5]:

            forecast.append(
                {
                    "datetime": item["dt_txt"],
                    "temperature_c": item["main"]["temp"],
                    "condition": item["weather"][0]["description"],
                }
            )

        return {
            "city": data.get("city", {}).get("name", city),
            "forecast": forecast
        }

    except requests.RequestException as exc:
        return {
            "error": f"Forecast API request failed: {exc}"
        }

    except Exception as exc:
        return {
            "error": f"Forecast data processing failed: {exc}"
        }


if __name__ == "__main__":
    mcp.run()
