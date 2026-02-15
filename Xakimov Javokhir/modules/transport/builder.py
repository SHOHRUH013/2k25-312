from modules.transport.vehicle import Vehicle


class VehicleBuilder:
    # builder: пошаговое создание транспортного средства
    def __init__(self):
        self.vehicle = Vehicle()

    def set_type(self, vehicle_type):
        self.vehicle.vehicle_type = vehicle_type
        return self

    def set_route(self, route):
        self.vehicle.route = route
        return self

    def set_capacity(self, capacity):
        self.vehicle.capacity = capacity
        return self

    def set_fuel_type(self, fuel_type):
        self.vehicle.fuel_type = fuel_type
        return self

    def build(self):
        if not self.vehicle.vehicle_type:
            raise ValueError("тип транспортного средства не указан")
        if not self.vehicle.route:
            raise ValueError("маршрут не указан")
        return self.vehicle

