import random

class FakeWeatherAPI:
    def fetch(self):
        return {"temp_c": random.randint(-5, 40), "sunny": random.choice([True, False])}

class WeatherAdapter:
    def __init__(self, api=None):
        self._api = api or FakeWeatherAPI()

    def get_temperature_celsius(self) -> int:
        raw = self._api.fetch()
        return int(raw.get("temp_c", 0))

    def is_sunny(self) -> bool:
        raw = self._api.fetch()
        return bool(raw.get("sunny", False))

