"""
Lighting Management Subsystem
Uses: Strategy pattern for different lighting modes
"""
from abc import ABC, abstractmethod
from datetime import datetime


# Strategy Interface
class LightingStrategy(ABC):
    @abstractmethod
    def adjust_intensity(self, current_intensity, conditions):
        pass


# Concrete Strategies
class StandardLightingStrategy(LightingStrategy):
    def adjust_intensity(self, current_intensity, conditions):
        return min(100, current_intensity + 10 if conditions['dark'] else max(30, current_intensity - 20))


class EnergySavingStrategy(LightingStrategy):
    def adjust_intensity(self, current_intensity, conditions):
        if conditions['traffic_density'] > 50:
            return 70
        elif conditions['weather'] == 'Rainy':
            return 80
        else:
            return 40


class FestivalLightingStrategy(LightingStrategy):
    def adjust_intensity(self, current_intensity, conditions):
        return 100  # Full brightness for festivals


class LightingManager:
    def __init__(self):
        self._street_lights = {}
        self._strategy = StandardLightingStrategy()
        self._energy_saving = False

    def set_energy_saving(self, enabled):
        self._energy_saving = enabled
        self._strategy = EnergySavingStrategy() if enabled else StandardLightingStrategy()

    def set_strategy(self, strategy):
        self._strategy = strategy

    def control_lighting(self, street, conditions):
        """Control lighting based on conditions"""
        current_intensity = self._street_lights.get(street, {'intensity': 0})['intensity']

        new_intensity = self._strategy.adjust_intensity(current_intensity, conditions)

        self._street_lights[street] = {
            'intensity': new_intensity,
            'status': 'ON' if new_intensity > 0 else 'OFF',
            'last_updated': datetime.now().strftime("%H:%M:%S"),
            'energy_consumption': new_intensity * 0.1  # kWh
        }

        action = "increased" if new_intensity > current_intensity else "decreased" if new_intensity < current_intensity else "maintained"
        return f"Lighting at {street} {action} to {new_intensity}%"

    def schedule_lighting(self, time):
        """Schedule lighting based on time of day"""
        hour = int(time.split(':')[0])

        if 18 <= hour <= 23 or 0 <= hour <= 6:
            return "Night mode: 70% intensity"
        elif 6 < hour < 18:
            return "Day mode: 30% intensity (only safety lighting)"
        else:
            return "Evening mode: 100% intensity"

    def get_energy_usage(self):
        """Calculate total energy usage"""
        total = sum(light['energy_consumption'] for light in self._street_lights.values())
        return round(total, 2)