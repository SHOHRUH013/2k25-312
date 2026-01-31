"""
Abstract Factory Pattern: Creates families of related objects
for different city sectors (residential, commercial, industrial)
"""
from abc import ABC, abstractmethod


# Abstract Products
class LightingSystem(ABC):
    @abstractmethod
    def install(self):
        pass


class SecuritySystem(ABC):
    @abstractmethod
    def deploy(self):
        pass


class EnergySystem(ABC):
    @abstractmethod
    def setup(self):
        pass


# Concrete Products for Residential Sector
class ResidentialLighting(LightingSystem):
    def install(self):
        return "Installing energy-efficient LED lighting for residential area"


class ResidentialSecurity(SecuritySystem):
    def deploy(self):
        return "Deploying basic surveillance system for residential area"


class ResidentialEnergy(EnergySystem):
    def setup(self):
        return "Setting up solar-powered energy system for residential area"


# Concrete Products for Commercial Sector
class CommercialLighting(LightingSystem):
    def install(self):
        return "Installing high-intensity smart lighting for commercial area"


class CommercialSecurity(SecuritySystem):
    def deploy(self):
        return "Deploying advanced AI surveillance for commercial area"


class CommercialEnergy(EnergySystem):
    def setup(self):
        return "Setting up hybrid energy system for commercial area"


# Abstract Factory
class CitySectorFactory(ABC):
    @abstractmethod
    def create_lighting(self) -> LightingSystem:
        pass

    @abstractmethod
    def create_security(self) -> SecuritySystem:
        pass

    @abstractmethod
    def create_energy(self) -> EnergySystem:
        pass


# Concrete Factories
class ResidentialSectorFactory(CitySectorFactory):
    def create_lighting(self) -> LightingSystem:
        return ResidentialLighting()

    def create_security(self) -> SecuritySystem:
        return ResidentialSecurity()

    def create_energy(self) -> EnergySystem:
        return ResidentialEnergy()


class CommercialSectorFactory(CitySectorFactory):
    def create_lighting(self) -> LightingSystem:
        return CommercialLighting()

    def create_security(self) -> SecuritySystem:
        return CommercialSecurity()

    def create_energy(self) -> EnergySystem:
        return CommercialEnergy()


class IndustrialSectorFactory(CitySectorFactory):
    def create_lighting(self) -> LightingSystem:
        return CommercialLighting()  # Reuse commercial for industrial

    def create_security(self) -> SecuritySystem:
        return CommercialSecurity()  # Reuse commercial for industrial

    def create_energy(self) -> EnergySystem:
        class IndustrialEnergy(EnergySystem):
            def setup(self):
                return "Setting up high-capacity grid energy for industrial area"

        return IndustrialEnergy()


# Factory Client
class SectorSetupManager:
    def __init__(self, factory: CitySectorFactory):
        self.factory = factory
        self.lighting = None
        self.security = None
        self.energy = None

    def setup_sector(self):
        """Setup complete sector using abstract factory"""
        self.lighting = self.factory.create_lighting()
        self.security = self.factory.create_security()
        self.energy = self.factory.create_energy()

        return [
            self.lighting.install(),
            self.security.deploy(),
            self.energy.setup()
        ]