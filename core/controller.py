"""
Core Controller Module
Design Patterns:
1. Singleton - Ensures only one instance of SmartCityController exists
2. Facade - Provides simplified interface to complex subsystems
"""


class SingletonMeta(type):
    """
    SINGLETON PATTERN (Creational)
    Purpose: Ensure only one instance of a class exists
    Usage: Metaclass for creating singleton classes
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SmartCityController(metaclass=SingletonMeta):
    """
    FACADE PATTERN (Structural)
    Purpose: Provides unified interface to all city subsystems
    Usage: Central controller that simplifies access to complex subsystems

    SINGLETON PATTERN
    Purpose: Ensures only one controller instance manages the entire city
    """

    def __init__(self):
        """Initialize controller if first instance"""
        if not hasattr(self, '_initialized'):
            self._devices = []
            self._subsystems = {
                'transport': [],
                'lighting': [],
                'security': [],
                'energy': []
            }
            self._initialized = True
            print("🏗️ SmartCity Controller initialized (Singleton)")

    def create_device(self, device_type, location):
        """
        FACADE METHOD
        Simplifies device creation by hiding factory complexity
        """
        from core.factories.device_factory import DeviceFactory

        device = DeviceFactory.create_device(device_type, location)
        self._devices.append(device)

        # Categorize device
        if device_type in ['traffic_light', 'public_transport']:
            self._subsystems['transport'].append(device)
        elif device_type == 'street_light':
            self._subsystems['lighting'].append(device)
        elif device_type == 'camera':
            self._subsystems['security'].append(device)
        elif device_type == 'solar_panel':
            self._subsystems['energy'].append(device)

        return device

    def get_system_status(self):
        """
        FACADE METHOD
        Provides simple way to check all subsystems status
        """
        print("\n📍 Active Devices:")

        for subsystem, devices in self._subsystems.items():
            if devices:
                print(f"\n  {subsystem.upper()}:")
                for device in devices:
                    print(f"    • {device.get_info()}")

        print(f"\n📊 Total devices: {len(self._devices)}")

    def generate_report(self):
        """
        FACADE METHOD
        Generates comprehensive system report
        """
        print("\n🏙️ SmartCity System Report")
        print(f"Total Devices: {len(self._devices)}")
        print(f"\nSubsystem Breakdown:")

        for subsystem, devices in self._subsystems.items():
            print(f"  • {subsystem.capitalize()}: {len(devices)} devices")

        print("\n✅ All systems operational")