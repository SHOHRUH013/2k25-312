"""
Transport System Module
Part of the SmartCity infrastructure
"""
import random
import time

class TransportSystem:
    def __init__(self):
        self.traffic_level = random.randint(1, 10)
        self.public_transport_vehicles = 50
        self.traffic_lights = 200
        self.is_emergency_mode = False

    def optimize_traffic_flow(self):
        """Optimize city traffic flow"""
        old_level = self.traffic_level
        self.traffic_level = max(1, self.traffic_level - random.randint(1, 3))
        return f"Traffic optimized: {old_level} → {self.traffic_level}/10"

    def adjust_traffic_lights(self):
        """Adjust traffic lights based on current traffic"""
        adjustment = "synchronized" if self.traffic_level > 5 else "normal"
        return f"Traffic lights {adjustment} for current traffic"  # Fixed typo: adjustition -> adjustment

    def coordinate_public_transport(self):
        """Coordinate public transport vehicles"""
        if self.traffic_level > 7:
            return "Adding extra buses to routes due to high traffic"
        else:
            return "Public transport operating on regular schedule"

    def emergency_mode(self):
        """Activate emergency transport mode"""
        self.is_emergency_mode = True
        self.traffic_level = 1  # Clear traffic for emergencies
        return "🚑 EMERGENCY TRANSPORT MODE: All routes cleared for emergency vehicles"

    def get_status(self):
        """Get transport system status"""
        status = "NORMAL"
        if self.traffic_level > 7:
            status = "HEAVY"
        elif self.traffic_level > 4:
            status = "MODERATE"

        if self.is_emergency_mode:
            status = "EMERGENCY MODE"

        return f"Transport: {status} (Traffic: {self.traffic_level}/10)"