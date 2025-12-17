from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.energy import EnergySystem
from core.subsystem_factory import SubsystemFactory
from core.proxy import SecurityProxy  # ← ВОТ ТУТ БЫЛА ОШИБКА! Теперь правильно

class CityController:
    _instance = None
    
    def __init__(self):
        if CityController._instance is not None:
            raise RuntimeError("Use get_instance() for Singleton!")
            
        factory = SubsystemFactory()
        self.lighting = factory.create_subsystem("lighting")
        self.transport = factory.create_subsystem("transport")
        self.security = SecurityProxy()  # Proxy из core/proxy.py
        self.energy = factory.create_subsystem("energy")
    
    @staticmethod
    def get_instance():
        """Singleton: единственный контроллер города"""
        if CityController._instance is None:
            CityController._instance = CityController()
        return CityController._instance
    
    # Facade
    def manage_lighting(self):
        self.lighting.menu()
    
    def manage_transport(self):
        self.transport.menu()
    
    def manage_security(self):
        self.security.access_control_menu()
    
    def manage_energy(self):
        self.energy.show_stats()
    
    def show_status(self):
        print("\nОБЩИЙ СТАТУС УМНОГО ГОРОДА")
        print(f"Активных фонарей: {self.lighting.active_count()}")
        print(f"Светофоров в системе: {self.transport.traffic_lights_count()}")
        print(f"Камер под контролем: {self.security.camera_count}")
        print(f"Энергопотребление: {self.energy.current_consumption()} кВт⋅ч")