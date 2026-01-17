from modules.energy.energy_facade import EnergyFacade


class EnergySubsystem:
    def __init__(self, controller):
        self.facade = EnergyFacade(controller)

    def optimize(self):
        return self.facade.optimize_energy()

    def get_total_consumption(self):
        return self.facade.get_total_consumption()

    def register_lighting(self, location, consumption):
        self.facade.register_lighting_consumption(location, consumption)
        return f"энергопотребление освещения на {location} зарегистрировано: {consumption} кВт·ч"

    def register_transport(self, vehicle_id, consumption):
        self.facade.register_transport_consumption(vehicle_id, consumption)
        return f"энергопотребление транспорта {vehicle_id} зарегистрировано: {consumption} кВт·ч"

    def update_lighting(self, location, consumption):
        return self.facade.update_lighting_consumption(location, consumption)

    def update_transport(self, vehicle_id, consumption):
        return self.facade.update_transport_consumption(vehicle_id, consumption)

    def get_report(self):
        return self.facade.get_consumption_report()

    def execute(self, command, *args, **kwargs):
        if command == "optimize":
            return self.optimize()
        elif command == "total":
            return self.get_total_consumption()
        elif command == "register_lighting":
            return self.register_lighting(*args, **kwargs)
        elif command == "register_transport":
            return self.register_transport(*args, **kwargs)
        elif command == "update_lighting":
            return self.update_lighting(*args, **kwargs)
        elif command == "update_transport":
            return self.update_transport(*args, **kwargs)
        elif command == "report":
            return self.get_report()
        return "неизвестная команда"

