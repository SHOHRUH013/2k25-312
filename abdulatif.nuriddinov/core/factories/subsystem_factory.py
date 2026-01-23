"""
Abstract Factory Pattern Implementation
Purpose: Provide an interface for creating families of related or dependent subsystems
without specifying their concrete classes. This allows easy addition of new subsystems.
"""
from abc import ABC, abstractmethod
from modules.transport.transport_manager import TransportManager
from modules.lighting.lighting_manager import LightingManager
from modules.security.security_manager import SecurityManager
from modules.energy.energy_manager import EnergyManager


# Abstract Factory
class SubsystemFactory(ABC):
    @abstractmethod
    def create_transport_system(self):
        pass

    @abstractmethod
    def create_lighting_system(self):
        pass

    @abstractmethod
    def create_security_system(self):
        pass

    @abstractmethod
    def create_energy_system(self):
        pass


# Concrete Factory for standard city systems
class StandardCityFactory(SubsystemFactory):
    def create_transport_system(self):
        return TransportManager()

    def create_lighting_system(self):
        return LightingManager()

    def create_security_system(self):
        return SecurityManager()

    def create_energy_system(self):
        return EnergyManager()


# Concrete Factory for eco-friendly systems (extensibility example)
class EcoCityFactory(SubsystemFactory):
    def create_transport_system(self):
        transport = TransportManager()
        transport.set_eco_mode(True)
        return transport

    def create_lighting_system(self):
        lighting = LightingManager()
        lighting.set_energy_saving(True)
        return lighting

    def create_security_system(self):
        return SecurityManager()

    def create_energy_system(self):
        energy = EnergyManager()
        energy.set_renewable_priority(True)
        return energy