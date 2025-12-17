from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.energy import EnergySystem

class SubsystemFactory:
    """Factory Method: создаёт нужные подсистемы по строковому идентификатору"""
    
    def create_subsystem(self, subsystem_type: str):
        if subsystem_type == "lighting":
            return LightingSystem()
        elif subsystem_type == "transport":
            return TransportSystem()
        elif subsystem_type == "energy":
            return EnergySystem()
        else:
            raise ValueError(f"Unknown subsystem: {subsystem_type}")