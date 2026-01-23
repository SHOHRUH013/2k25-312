"""
Transport Management Subsystem
Uses: Observer pattern internally for traffic updates
"""

from datetime import datetime
from abc import ABC, abstractmethod

class TrafficObserver(ABC):
    @abstractmethod
    def update_traffic(self, area, data):
        pass

class TransportManager:
    def __init__(self):
        self._traffic_data = {}
        self._observers = []
        self._eco_mode = False

    def set_eco_mode(self, enabled):
        self._eco_mode = enabled

    def update_traffic(self, area, density, avg_speed):
        """Update traffic information for an area"""
        self._traffic_data[area] = {
            'density': density,  # percentage
            'avg_speed': avg_speed,  # km/h
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'congestion': density > 70
        }
        self._notify_observers(area)
        return self._traffic_data[area]

    def optimize_traffic_lights(self, area):
        """Optimize traffic lights based on current conditions"""
        if area not in self._traffic_data:
            return "No data available"

        data = self._traffic_data[area]
        if data['congestion']:
            return f"Increasing green light duration at {area} by 30%"
        elif data['avg_speed'] > 60:
            return f"Normal traffic flow at {area}"
        else:
            return f"Adjusting sequence at {area}"

    def get_public_transport_schedule(self, route):
        """Get public transport schedule"""
        schedules = {
            'A1': ['06:00', '07:30', '09:00', '12:00', '15:30', '18:00', '20:30'],
            'B2': ['06:15', '08:00', '10:30', '13:00', '16:30', '19:00', '21:30'],
            'C3': ['05:45', '07:15', '09:45', '12:30', '15:00', '17:30', '22:00']
        }
        return schedules.get(route, [])

    def register_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self, area):
        for observer in self._observers:
            observer.update_traffic(area, self._traffic_data[area])