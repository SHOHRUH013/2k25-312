
from dataclasses import dataclass

@dataclass
class CityConfig:
    city_name: str
    num_lights: int
    num_buses: int
    strict_security: bool

class CityConfigBuilder:
    def __init__(self):
        self._city_name = "SmartCity"
        self._num_lights = 10
        self._num_buses = 5
        self._strict_security = False

    def set_city_name(self, name):
        self._city_name = name
        return self

    def set_num_lights(self, n):
        self._num_lights = n
        return self

    def set_num_buses(self, n):
        self._num_buses = n
        return self

    def set_strict_security(self, strict):
        self._strict_security = strict
        return self

    def build(self):
        return CityConfig(
            self._city_name,
            self._num_lights,
            self._num_buses,
            self._strict_security
        )
