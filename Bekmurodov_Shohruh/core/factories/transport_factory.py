from abc import ABC, abstractmethod

from Bekmurodov_Shohruh.modules.transport import Vehicle, Bus, Tram


class TransportFactory(ABC):
    @abstractmethod
    def create_vehicle(self, route: str) -> Vehicle:
        pass


class BusFactory(TransportFactory):
    def create_vehicle(self, route: str) -> Vehicle:
        return Bus(route)


class TramFactory(TransportFactory):
    def create_vehicle(self, route: str) -> Vehicle:
        return Tram(route)
