from core.singleton.city_singleton import CitySingleton
import singelton.city_singelton
from modules.transport.transport import TransportSystem
from modules.lighting.lighting import LightingSystem
from modules.security.security import SecuritySystem
from modules.energy.energy import EnergySystem

class SmartCityController:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Connected Subsystems
            cls._instance.city = CitySingleton()
            cls._instance.transport = TransportSystem()
            cls._instance.lighting = LightingSystem()
            cls._instance.security = SecuritySystem()
            cls._instance.energy = EnergySystem()

        return cls._instance

    def show_status(self):
        return {
            "city": self.city.info(),
            "transport": self.transport.status(),
            "lighting": self.lighting.status(),
            "security": self.security.status(),
            "energy": self.energy.status(),
        }

    def enable_night_mode(self):
        self.lighting.turn_on()
        self.security.activate_cameras()
        return "Night mode enabled."
