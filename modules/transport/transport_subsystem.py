from modules.transport.builder import VehicleBuilder


class TransportSubsystem:
    def __init__(self):
        self.vehicles = {}
        self.next_id = 1

    def add_vehicle(self, vehicle_type, route, capacity=None, fuel_type=None):
        builder = VehicleBuilder()
        builder.set_type(vehicle_type)
        builder.set_route(route)
        if capacity:
            builder.set_capacity(capacity)
        if fuel_type:
            builder.set_fuel_type(fuel_type)
        
        vehicle = builder.build()
        vehicle_id = f"T{self.next_id}"
        self.vehicles[vehicle_id] = vehicle
        self.next_id += 1
        return f"транспорт {vehicle_id} добавлен: {vehicle}"

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            return f"транспорт {vehicle_id} удален"
        return f"транспорт {vehicle_id} не найден"

    def start_route(self, vehicle_id):
        if vehicle_id in self.vehicles:
            return self.vehicles[vehicle_id].start_route()
        return f"транспорт {vehicle_id} не найден"

    def stop_route(self, vehicle_id):
        if vehicle_id in self.vehicles:
            return self.vehicles[vehicle_id].stop_route()
        return f"транспорт {vehicle_id} не найден"

    def get_status(self, vehicle_id=None):
        if vehicle_id:
            if vehicle_id in self.vehicles:
                return self.vehicles[vehicle_id].get_info()
            return None
        return {vid: vehicle.get_info() for vid, vehicle in self.vehicles.items()}

    def execute(self, command, *args, **kwargs):
        if command == "add":
            return self.add_vehicle(*args, **kwargs)
        elif command == "remove":
            return self.remove_vehicle(*args, **kwargs)
        elif command == "start":
            return self.start_route(*args, **kwargs)
        elif command == "stop":
            return self.stop_route(*args, **kwargs)
        elif command == "status":
            return self.get_status(*args, **kwargs)
        return "неизвестная команда"

