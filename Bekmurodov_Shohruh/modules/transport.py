from dataclasses import dataclass
import logging

logger = logging.getLogger("Transport")


@dataclass
class Vehicle:
    route: str
    name: str
    energy_per_km: float


class Bus(Vehicle):
    def __init__(self, route: str):
        super().__init__(route, "Bus", 4.5)


class Tram(Vehicle):
    def __init__(self, route: str):
        super().__init__(route, "Tram", 3.0)


class TransportSystem:
    def dispatch(self, vehicle: Vehicle) -> None:
        logger.info(f"Vehicle dispatched: {vehicle.name} on route {vehicle.route}")
