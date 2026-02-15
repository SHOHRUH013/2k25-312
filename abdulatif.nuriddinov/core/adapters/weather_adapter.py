"""
Adapter Pattern Implementation
Purpose: Convert the interface of external weather service into an interface
that the SmartCity system expects. This allows integration of third-party services.
"""
import random
from datetime import datetime


# External Weather Service (Incompatible interface)
class ExternalWeatherService:
    def fetch_weather_data_raw(self, city):
        # Simulating external service with different interface
        return {
            'temp_c': random.uniform(-10, 35),
            'humidity_percent': random.uniform(30, 90),
            'wind_speed_kmh': random.uniform(0, 50),
            'condition': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy']),
            'timestamp': datetime.now().isoformat()
        }


# Target interface expected by SmartCity
class WeatherService:
    def get_weather(self, city):
        pass


# Adapter
class WeatherServiceAdapter(WeatherService):
    def __init__(self, external_service):
        self.external_service = external_service

    def get_weather(self, city):
        raw_data = self.external_service.fetch_weather_data_raw(city)

        # Adapt the data to expected format
        adapted_data = {
            'temperature': round(raw_data['temp_c'], 1),
            'humidity': round(raw_data['humidity_percent']),
            'wind_speed': round(raw_data['wind_speed_kmh']),
            'condition': raw_data['condition'],
            'timestamp': raw_data['timestamp'],
            'recommendations': self._generate_recommendations(raw_data)
        }
        return adapted_data

    def _generate_recommendations(self, weather_data):
        recommendations = []

        if weather_data['condition'] == 'Rainy':
            recommendations.append("Activate drainage systems")
            recommendations.append("Reduce street lighting intensity")

        if weather_data['temp_c'] > 30:
            recommendations.append("Increase public water fountain flow")
            recommendations.append("Activate cooling centers")

        if weather_data['wind_speed_kmh'] > 40:
            recommendations.append("Secure outdoor equipment")
            recommendations.append("Monitor tree stability")

        return recommendations