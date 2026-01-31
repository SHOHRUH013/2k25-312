from modules.energy.power_monitor import PowerMonitor


class EnergyFacade:
    # facade: упрощенный интерфейс для управления энергопотреблением
    def __init__(self, controller):
        self.controller = controller
        self.monitor = PowerMonitor()

    def optimize_energy(self):
        """оптимизация энергопотребления всех подсистем"""
        results = []
        
        lighting = self.controller.get_subsystem("lighting")
        if lighting:
            status = lighting.get_status()
            for location, light_data in status.items():
                if light_data["is_on"] and light_data["brightness"] > 70:
                    lighting.set_brightness(location, 70)
                    results.append(f"яркость на {location} снижена до 70%")
        
        transport = self.controller.get_subsystem("transport")
        if transport:
            status = transport.get_status()
            for vehicle_id, vehicle_data in status.items():
                if vehicle_data["status"] == "в парке":
                    results.append(f"транспорт {vehicle_id} в парке - энергопотребление минимально")
        
        return results

    def get_total_consumption(self):
        """получение общего энергопотребления"""
        return self.monitor.get_total()

    def register_lighting_consumption(self, location, consumption):
        """регистрация энергопотребления освещения"""
        self.monitor.register_consumer(f"lighting_{location}", consumption)

    def register_transport_consumption(self, vehicle_id, consumption):
        """регистрация энергопотребления транспорта"""
        self.monitor.register_consumer(f"transport_{vehicle_id}", consumption)

    def update_lighting_consumption(self, location, consumption):
        """обновление энергопотребления освещения"""
        self.monitor.update_consumption(f"lighting_{location}", consumption)

    def update_transport_consumption(self, vehicle_id, consumption):
        """обновление энергопотребления транспорта"""
        self.monitor.update_consumption(f"transport_{vehicle_id}", consumption)

    def get_consumption_report(self):
        """получение отчета по энергопотреблению"""
        consumption = self.monitor.get_consumption()
        total = self.monitor.get_total()
        return {
            "consumption_by_source": consumption,
            "total_consumption": total,
            "units": "кВт·ч"
        }

