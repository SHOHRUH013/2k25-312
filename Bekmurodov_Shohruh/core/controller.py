from typing import Dict
import logging

from Bekmurodov_Shohruh.core.adapters.weather_adapter import WeatherServiceAdapter, ExternalWeatherAPI
from Bekmurodov_Shohruh.core.builders.lighting_builder import LightingSceneBuilder
from Bekmurodov_Shohruh.core.factories.transport_factory import TransportFactory, BusFactory, TramFactory
from Bekmurodov_Shohruh.core.proxy.security_proxy import SecuritySystemProxy
from Bekmurodov_Shohruh.modules.energy import EnergySystem
from Bekmurodov_Shohruh.modules.lighting import LightingSystem
from Bekmurodov_Shohruh.modules.security import SecuritySystem
from Bekmurodov_Shohruh.modules.transport import TransportSystem

logger = logging.getLogger("SmartCity")


class Singleton(type):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SmartCityController(metaclass=Singleton):
    def __init__(self) -> None:
        self.lighting = LightingSystem()
        self.transport = TransportSystem()
        self.energy = EnergySystem()
        self.security = SecuritySystemProxy(SecuritySystem())

        # Dependency injection (factories)
        self.factories: Dict[str, TransportFactory] = {
            "bus": BusFactory(),
            "tram": TramFactory(),
        }
        self.weather_service = WeatherServiceAdapter(ExternalWeatherAPI())

    def configure_lighting(self, area: str, brightness: int, schedule: str) -> None:
        builder = LightingSceneBuilder()
        scene = (
            builder
            .set_area(area)
            .set_brightness(brightness)
            .set_schedule(schedule)
            .build()
        )

        self.lighting.apply_scene(scene)
        self.energy.register_lighting(scene)

    def send_transport(self, route: str, t_type: str) -> None:
        factory = self.factories.get(t_type)
        if not factory:
            logger.error(f"Unknown transport type: {t_type}")
            return

        vehicle = factory.create_vehicle(route)
        self.transport.dispatch(vehicle)
        self.energy.register_transport(vehicle)

    def arm_security(self) -> None:
        self.security.authorize("ADMIN")
        self.security.arm()

    def disarm_security(self) -> None:
        self.security.authorize("ADMIN")
        self.security.disarm()

    def eco_mode(self) -> None:
        temp, is_day = self.weather_service.get_city_weather("Tashkent")
        logger.info(f"Weather: {temp}°C, daytime={is_day}")

        if is_day and temp > 22:
            logger.info("Eco mode: dimming lights...")
            self.lighting.dim_global(40)
