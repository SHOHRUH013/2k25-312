class TransportRoute:
    def __init__(self):
        self.number = None
        self.stops = []
        self.speed_limit = None

    def __repr__(self):
        return f"TransportRoute(number={self.number}, stops={self.stops}, speed_limit={self.speed_limit})"

class TransportRouteBuilder:
    def __init__(self):
        self._route = TransportRoute()

    def set_number(self, number: int):
        self._route.number = number
        return self

    def add_stop(self, stop: str):
        self._route.stops.append(stop)
        return self

    def set_speed_limit(self, speed: int):
        self._route.speed_limit = speed
        return self

    def build(self) -> TransportRoute:
        return self._route
