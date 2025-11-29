"""
Device Factory Module
Design Pattern: FACTORY METHOD (Creational)
Purpose: Creates different types of city devices without specifying exact classes
Usage: Central factory for creating all device types in the smart city
"""

from modules.transport.transport_system import TrafficLight, PublicTransport
from modules.lighting.lighting_system import StreetLight
from modules.security.security_system import Camera
from modules.energy.energy_system import SolarPanel


class DeviceFactory:
    """
    FACTORY METHOD PATTERN (Creational)
    Purpose: Encapsulates object creation logic
    Benefits:
    - Decouples device creation from usage
    - Easy to add new device types
    - Centralized creation logic
    """

    @staticmethod
    def create_device(device_type, location):
        """
        Factory method to create devices based on type

        Args:
            device_type (str): Type of device to create
            location (str): Location identifier

        Returns:
            Device object of requested type
        """
        device_map = {
            'traffic_light': TrafficLight,
            'public_transport': PublicTransport,
            'street_light': StreetLight,
            'camera': Camera,
            'solar_panel': SolarPanel
        }

        device_class = device_map.get(device_type.lower())

        if device_class is None:
            raise ValueError(f"Unknown device type: {device_type}")

        return device_class(location)


class AbstractDeviceFactory:
    """
    ABSTRACT FACTORY PATTERN (Creational)
    Purpose: Creates families of related devices
    Usage: Can create entire subsystem sets at once
    """

    @staticmethod
    def create_transport_subsystem(base_location):
        """Create complete transportation subsystem"""
        devices = [
            TrafficLight(f"{base_location} - Intersection 1"),
            TrafficLight(f"{base_location} - Intersection 2"),
            PublicTransport(f"{base_location} - Route A")
        ]
        return devices

    @staticmethod
    def create_security_subsystem(base_location):
        """Create complete security subsystem"""
        devices = [
            Camera(f"{base_location} - North"),
            Camera(f"{base_location} - South"),
            Camera(f"{base_location} - East"),
            Camera(f"{base_location} - West")
        ]
        return devices

    @staticmethod
    def create_energy_subsystem(base_location):
        """Create complete energy subsystem"""
        devices = [
            SolarPanel(f"{base_location} - Roof 1"),
            SolarPanel(f"{base_location} - Roof 2"),
            SolarPanel(f"{base_location} - Ground Array")
        ]
        return devices