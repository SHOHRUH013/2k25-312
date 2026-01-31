class Vehicle:
    def __init__(self):
        self.vehicle_type = None
        self.route = None
        self.capacity = None
        self.fuel_type = None
        self.status = "в парке"

    def __str__(self):
        return f"{self.vehicle_type} | маршрут: {self.route} | вместимость: {self.capacity} | топливо: {self.fuel_type} | статус: {self.status}"

    def start_route(self):
        self.status = "в пути"
        return f"{self.vehicle_type} начал движение по маршруту {self.route}"

    def stop_route(self):
        self.status = "в парке"
        return f"{self.vehicle_type} завершил маршрут {self.route}"

    def get_info(self):
        return {
            "type": self.vehicle_type,
            "route": self.route,
            "capacity": self.capacity,
            "fuel_type": self.fuel_type,
            "status": self.status
        }

