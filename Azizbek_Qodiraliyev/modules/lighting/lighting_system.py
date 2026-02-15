"""
Lighting System Module
Manages city street lighting infrastructure
"""
import random
from datetime import datetime

class LightingSystem:
    def __init__(self):
        self.intensity = 70
        self.energy_consumption = 0
        self.total_lights = 10000
        self.operational_lights = 9800
        self.is_emergency_lighting = False

    def set_intensity(self, level):
        """Set lighting intensity (0-100)"""
        if 0 <= level <= 100:
            self.intensity = level
            self.energy_consumption = (level / 100) * 5000  # kW
            return f"Lighting intensity set to {level}%"
        else:
            return "Invalid intensity level (0-100)"

    def emergency_mode(self):
        """Activate emergency lighting"""
        self.is_emergency_lighting = True
        self.intensity = 100
        return "🚨 EMERGENCY LIGHTING: All lights at maximum intensity"

    def calculate_energy_savings(self):
        """Calculate energy savings from current settings"""
        base_consumption = 5000  # kW at 100%
        current_consumption = (self.intensity / 100) * base_consumption
        savings = base_consumption - current_consumption
        return savings

    def get_status(self):
        """Get lighting system status"""
        status = "NORMAL"
        if self.is_emergency_lighting:
            status = "EMERGENCY"

        operational_rate = (self.operational_lights / self.total_lights) * 100

        return (f"Lighting: {status} - Intensity: {self.intensity}% - "
                f"Operational: {operational_rate:.1f}%")