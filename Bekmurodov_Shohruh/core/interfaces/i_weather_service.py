from abc import ABC, abstractmethod
from typing import Tuple


class IWeatherService(ABC):

    @abstractmethod
    def get_city_weather(self, city: str) -> Tuple[int, bool]:
        raise NotImplementedError
