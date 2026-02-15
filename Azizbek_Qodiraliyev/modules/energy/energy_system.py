"""
Energy System Module
Manages city power distribution and consumption
"""
import random


class EnergySystem:
    def __init__(self):
        self.total_power_generated = 10000  # MW
        self.current_consumption = 7500  # MW
        self.renewable_ratio = 0.3
        self.grid_stability = 98.5  # %

    def distribute_power(self):
        """Distribute power across city sectors"""
        surplus = self.total_power_generated - self.current_consumption
        if surplus > 0:
            return f"Power distribution optimized. Surplus: {surplus} MW"
        else:
            return "⚠️ Power demand exceeds supply. Implementing load shedding."

    def toggle_renewable(self):
        """Toggle between renewable and conventional sources"""
        if self.renewable_ratio < 0.5:
            self.renewable_ratio = 0.8
            return "🌱 Renewable sources: MAXIMUM (80%)"
        else:
            self.renewable_ratio = 0.3
            return "⚡ Conventional sources: ACTIVATED (70%)"

    def emergency_mode(self):
        """Activate emergency power mode"""
        self.current_consumption = 3000  # Reduce to essential services only
        return "🚨 EMERGENCY POWER: Essential services only"

    def get_consumption_report(self):
        """Get energy consumption report"""
        renewable_power = self.total_power_generated * self.renewable_ratio
        conventional_power = self.total_power_generated * (1 - self.renewable_ratio)

        return (f"Energy Report:\n"
                f"Total Generated: {self.total_power_generated} MW\n"
                f"Current Consumption: {self.current_consumption} MW\n"
                f"Renewable: {renewable_power:.0f} MW ({self.renewable_ratio * 100:.0f}%)\n"
                f"Conventional: {conventional_power:.0f} MW\n"
                f"Grid Stability: {self.grid_stability}%")

    def get_status(self):
        """Get energy system status"""
        status = "STABLE"
        if self.current_consumption > self.total_power_generated * 0.9:
            status = "HIGH DEMAND"

        return (f"Energy: {status} - "
                f"Load: {self.current_consumption}/{self.total_power_generated} MW - "
                f"Renewable: {self.renewable_ratio * 100:.0f}%")