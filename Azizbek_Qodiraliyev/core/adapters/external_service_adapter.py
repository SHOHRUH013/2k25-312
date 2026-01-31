"""
Adapter Pattern: Adapts external weather service to our system interface
Allows integration of third-party services without changing existing code
"""
import random
from abc import ABC, abstractmethod


# External Weather Service (incompatible interface)
class ExternalWeatherService:
    """Third-party weather service with incompatible interface"""

    def fetch_weather_data(self, location):
        """Returns weather data in external format"""
        return {
            'temperature_f': random.randint(20, 100),
            'humidity_percent': random.randint(10, 95),
            'wind_speed_mph': random.randint(0, 30),
            'condition_code': random.choice(['SUNNY', 'RAINY', 'CLOUDY'])
        }


# Our System's Expected Interface
class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, location):
        pass

    @abstractmethod
    def is_weather_alert(self):
        pass


# Adapter
class WeatherServiceAdapter(WeatherService):
    """Adapter that makes ExternalWeatherService compatible with our system"""

    def __init__(self, external_service: ExternalWeatherService):
        self.external_service = external_service
        self._condition_map = {
            'SUNNY': 'Clear',
            'RAINY': 'Rain',
            'CLOUDY': 'Cloudy'
        }

    def get_weather(self, location):
        """Adapts external weather data to our system's format"""
        external_data = self.external_service.fetch_weather_data(location)

        # Convert temperature from Fahrenheit to Celsius
        temp_c = (external_data['temperature_f'] - 32) * 5 / 9

        # Convert wind speed from mph to km/h
        wind_kmh = external_data['wind_speed_mph'] * 1.60934

        # Map condition codes
        condition = self._condition_map.get(
            external_data['condition_code'], 'Unknown'
        )

        # Return in our system's expected format
        return {
            'temperature': round(temp_c, 1),
            'humidity': external_data['humidity_percent'],
            'wind_speed': round(wind_kmh, 1),
            'condition': condition,
            'location': location
        }

    def is_weather_alert(self):
        """Determine if weather conditions warrant an alert"""
        weather_data = self.get_weather("SmartCity")
        return (weather_data['wind_speed'] > 50 or
                weather_data['temperature'] > 35 or
                weather_data['condition'] == 'Rain')


# Weather Integration Manager
class WeatherIntegrationManager:
    """Manages weather integration using adapter pattern"""

    def __init__(self):
        external_service = ExternalWeatherService()
        self.weather_service = WeatherServiceAdapter(external_service)

    def get_weather_report(self):
        """Get formatted weather report"""
        weather = self.weather_service.get_weather("SmartCity")
        alert = " ⚠️ WEATHER ALERT" if self.weather_service.is_weather_alert() else ""

        report = [
            "🌤️  SmartCity Weather Report:",
            f"📍 Location: {weather['location']}",
            f"🌡️ Temperature: {weather['temperature']}°C",
            f"💧 Humidity: {weather['humidity']}%",
            f"💨 Wind Speed: {weather['wind_speed']} km/h",
            f"☁️ Condition: {weather['condition']}",
            f"{alert}"
        ]

        return "\n".join(report)

    def should_adjust_city_operations(self):
        """Determine if city operations need adjustment based on weather"""
        return self.weather_service.is_weather_alert()