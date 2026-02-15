"""
Energy Management Subsystem
"""

from datetime import datetime

class EnergyManager:
    def __init__(self):
        self._consumption_data = {}
        self._renewable_sources = {
            'solar': 0,
            'wind': 0,
            'hydro': 0
        }
        self._renewable_priority = False

    def set_renewable_priority(self, enabled):
        self._renewable_priority = enabled

    def monitor_consumption(self, sector, consumption):
        """Monitor energy consumption for a sector"""
        self._consumption_data[sector] = {
            'consumption_kwh': consumption,
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'peak_hours': 7 <= datetime.now().hour <= 22
        }
        return self._consumption_data[sector]

    def optimize_distribution(self):
        """Optimize energy distribution based on consumption"""
        total_consumption = sum(data['consumption_kwh'] for data in self._consumption_data.values())

        if total_consumption > 5000:  # High consumption threshold
            return "Activating peak load management: Reducing non-essential services"
        elif self._renewable_priority and self._get_renewable_output() > 2000:
            return "Using renewable sources primarily: 80% renewable, 20% grid"
        else:
            return "Normal distribution: 50% renewable, 50% grid"

    def update_renewable_output(self, source, output):
        """Update renewable energy output"""
        if source in self._renewable_sources:
            self._renewable_sources[source] = output

    def _get_renewable_output(self):
        return sum(self._renewable_sources.values())

    def get_energy_report(self):
        """Generate energy report"""
        total_consumption = sum(data['consumption_kwh'] for data in self._consumption_data.values())
        renewable_output = self._get_renewable_output()

        return {
            'total_consumption_kwh': total_consumption,
            'renewable_output_kwh': renewable_output,
            'grid_dependency_percent': max(0, ((
                                                           total_consumption - renewable_output) / total_consumption * 100) if total_consumption > 0 else 0),
            'renewable_sources': self._renewable_sources,
            'sectors_monitored': list(self._consumption_data.keys()),
            'recommendation': self.optimize_distribution()
        }