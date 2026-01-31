import random

from Bekmurodov_Shohruh.core.interfaces.i_weather_service import IWeatherService


class ExternalWeatherAPI:
    def fetch_data(self, city: str) -> dict:
        return {
            "city": city,
            "temperature_c": random.randint(5, 40),
            "period": random.choice(["day", "night"]),
        }


class WeatherServiceAdapter(IWeatherService):
    def __init__(self, api: ExternalWeatherAPI):
        self._api = api

    def get_city_weather(self, city: str):
        raw = self._api.fetch_data(city)
        temperature = raw["temperature_c"]
        is_day = raw["period"] == "day"
        return temperature, is_day
