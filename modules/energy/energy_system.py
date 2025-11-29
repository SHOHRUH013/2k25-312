"""
Energy System Module
Design Pattern: BUILDER (Creational)
Purpose: Constructs complex energy monitoring systems step-by-step
"""


class Device:
    """Base class for all smart city devices"""

    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        return f"{self.__class__.__name__} at {self.location}"


class SolarPanel(Device):
    """
    Solar Panel Device
    Generates renewable energy for the city
    """

    def __init__(self, location):
        super().__init__(location)
        self.capacity = 250  # Watts
        self.efficiency = 0.85
        self.current_output = 0

    def generate_power(self, sunlight_intensity):
        """Calculate power generation based on sunlight"""
        self.current_output = self.capacity * self.efficiency * (sunlight_intensity / 100)
        return self.current_output

    def get_info(self):
        return f"☀️ Solar Panel at {self.location} - Capacity: {self.capacity}W, Output: {self.current_output:.1f}W"


class EnergyStation:
    """
    Complex Energy Station
    Built using Builder pattern for step-by-step construction
    """

    def __init__(self):
        self.solar_panels = []
        self.battery_storage = None
        self.monitoring_system = None
        self.grid_connection = None
        self.location = "Unknown"

    def __str__(self):
        """String representation of energy station"""
        info = [f"\n⚡ Energy Station at {self.location}"]
        info.append(f"  Solar Panels: {len(self.solar_panels)}")

        if self.battery_storage:
            info.append(f"  Battery: {self.battery_storage}kWh")

        if self.monitoring_system:
            info.append(f"  Monitoring: {self.monitoring_system}")

        if self.grid_connection:
            info.append(f"  Grid: Connected ({self.grid_connection})")

        return "\n".join(info)


class EnergyStationBuilder:
    """
    BUILDER PATTERN (Creational)
    Purpose: Constructs complex EnergyStation objects step-by-step
    Benefits:
    - Separates construction from representation
    - Allows different configurations of energy stations
    - Makes code more readable and maintainable
    - Can create stations with varying complexity
    """

    def __init__(self):
        self._station = EnergyStation()

    def set_location(self, location):
        """Set station location"""
        self._station.location = location
        return self

    def add_solar_panel(self, capacity=250):
        """Add a solar panel to the station"""
        panel = SolarPanel(f"{self._station.location} - Panel {len(self._station.solar_panels) + 1}")
        panel.capacity = capacity
        self._station.solar_panels.append(panel)
        return self

    def add_multiple_panels(self, count, capacity=250):
        """Add multiple solar panels at once"""
        for _ in range(count):
            self.add_solar_panel(capacity)
        return self

    def add_battery_storage(self, capacity_kwh):
        """Add battery storage system"""
        self._station.battery_storage = capacity_kwh
        return self

    def add_monitoring_system(self, system_type="Advanced"):
        """Add monitoring system"""
        self._station.monitoring_system = system_type
        return self

    def add_grid_connection(self, connection_type="Two-way"):
        """Add grid connection"""
        self._station.grid_connection = connection_type
        return self

    def build(self):
        """Return the constructed energy station"""
        station = self._station
        self._station = EnergyStation()  # Reset for next build
        return station


class EnergyStationDirector:
    """
    Director class for building predefined station configurations
    """

    @staticmethod
    def build_basic_station(location):
        """Build a basic energy station with minimal features"""
        builder = EnergyStationBuilder()
        return (builder
                .set_location(location)
                .add_multiple_panels(4, 250)
                .add_monitoring_system("Basic")
                .build())

    @staticmethod
    def build_advanced_station(location):
        """Build an advanced energy station with all features"""
        builder = EnergyStationBuilder()
        return (builder
                .set_location(location)
                .add_multiple_panels(12, 400)
                .add_battery_storage(50)
                .add_monitoring_system("Advanced")
                .add_grid_connection("Two-way")
                .build())

    @staticmethod
    def build_industrial_station(location):
        """Build a large industrial energy station"""
        builder = EnergyStationBuilder()
        return (builder
                .set_location(location)
                .add_multiple_panels(50, 500)
                .add_battery_storage(200)
                .add_monitoring_system("Industrial IoT")
                .add_grid_connection("High-voltage")
                .build())


# Example usage demonstrating builder pattern
def demo_builder():
    """Demonstrate builder pattern with different station types"""

    print("=" * 60)
    print("BUILDER PATTERN DEMONSTRATION")
    print("=" * 60)

    # Build basic station
    print("\n1. Building Basic Station:")
    basic = EnergyStationDirector.build_basic_station("Residential Area")
    print(basic)

    # Build advanced station
    print("\n2. Building Advanced Station:")
    advanced = EnergyStationDirector.build_advanced_station("City Center")
    print(advanced)

    # Build custom station step by step
    print("\n3. Building Custom Station (Step-by-step):")
    builder = EnergyStationBuilder()
    custom = (builder
              .set_location("Technology Park")
              .add_multiple_panels(8, 350)
              .add_battery_storage(100)
              .add_monitoring_system("Smart Grid")
              .add_grid_connection("Bi-directional")
              .build())
    print(custom)

    # Build industrial station
    print("\n4. Building Industrial Station:")
    industrial = EnergyStationDirector.build_industrial_station("Industrial Zone")
    print(industrial)