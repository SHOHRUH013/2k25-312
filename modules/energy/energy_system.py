class Device:
    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        return f"{self.__class__.__name__} at {self.location}"


class SolarPanel(Device):
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
    def __init__(self):
        self.solar_panels = []
        self.battery_storage = None
        self.monitoring_system = None
        self.grid_connection = None
        self.location = "Unknown"

    def __str__(self):
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
    def __init__(self):
        self._station = EnergyStation()

    def set_location(self, location):
        self._station.location = location
        return self

    def add_solar_panel(self, capacity=250):
        panel = SolarPanel(f"{self._station.location} - Panel {len(self._station.solar_panels) + 1}")
        panel.capacity = capacity
        self._station.solar_panels.append(panel)
        return self

    def add_multiple_panels(self, count, capacity=250):
        for _ in range(count):
            self.add_solar_panel(capacity)
        return self

    def add_battery_storage(self, capacity_kwh):
        self._station.battery_storage = capacity_kwh
        return self

    def add_monitoring_system(self, system_type="Advanced"):
        self._station.monitoring_system = system_type
        return self

    def add_grid_connection(self, connection_type="Two-way"):
        self._station.grid_connection = connection_type
        return self

    def build(self):
        station = self._station
        self._station = EnergyStation()  # Reset for next build
        return station


class EnergyStationDirector:
    @staticmethod
    def build_basic_station(location):
        builder = EnergyStationBuilder()
        return (builder
                .set_location(location)
                .add_multiple_panels(4, 250)
                .add_monitoring_system("Basic")
                .build())

    @staticmethod
    def build_advanced_station(location):
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
    print("=" * 60)
    print("BUILDER PATTERN DEMONSTRATION")
    print("=" * 60)

    print("\n1. Building Basic Station:")
    basic = EnergyStationDirector.build_basic_station("Residential Area")
    print(basic)

    print("\n2. Building Advanced Station:")
    advanced = EnergyStationDirector.build_advanced_station("City Center")
    print(advanced)

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

    print("\n4. Building Industrial Station:")
    industrial = EnergyStationDirector.build_industrial_station("Industrial Zone")
    print(industrial)