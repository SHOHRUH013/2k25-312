"""
Builder Pattern: Constructs complex SmartCity system step by step
Allows creating different configurations of the city system
"""
from modules.transport.transport_system import TransportSystem
from modules.lighting.lighting_system import LightingSystem
from modules.security.security_system import SecuritySystem
from modules.energy.energy_system import EnergySystem


class SmartCitySystem:
    """Product class representing the complete smart city system"""

    def __init__(self):
        self.transport = None
        self.lighting = None
        self.security = None
        self.energy = None
        self.is_operational = False

    def __str__(self):
        status = "OPERATIONAL" if self.is_operational else "SETUP MODE"
        components = []
        if self.transport: components.append("Transport")
        if self.lighting: components.append("Lighting")
        if self.security: components.append("Security")
        if self.energy: components.append("Energy")

        return f"SmartCity System [{status}] - Components: {', '.join(components)}"


class SmartCitySystemBuilder:
    """Builder class for constructing SmartCity system"""

    def __init__(self):
        self.system = SmartCitySystem()

    def add_transport_system(self):
        """Add transportation subsystem"""
        print("🚗 Building Transport System...")
        self.system.transport = TransportSystem()
        return self

    def add_lighting_system(self):
        """Add lighting subsystem"""
        print("💡 Building Lighting System...")
        self.system.lighting = LightingSystem()
        return self

    def add_security_system(self):
        """Add security subsystem"""
        print("🚨 Building Security System...")
        self.system.security = SecuritySystem()
        return self

    def add_energy_system(self):
        """Add energy subsystem"""
        print("⚡ Building Energy System...")
        self.system.energy = EnergySystem()
        return self

    def set_operational(self):
        """Mark system as operational"""
        self.system.is_operational = True
        return self

    def build(self):
        """Return the fully constructed system"""
        if any([self.system.transport, self.system.lighting,
                self.system.security, self.system.energy]):
            self.system.is_operational = True
            print("✅ SmartCity System built successfully!")
        else:
            print("⚠️  System built but no components added")

        return self.system


class AdvancedCityBuilder(SmartCitySystemBuilder):
    """Extended builder for advanced city features"""

    def add_ai_management(self):
        """Add AI management system (extended functionality)"""
        print("🤖 Adding AI Management System...")
        # Additional AI functionality would be implemented here
        return self

    def add_environmental_monitoring(self):
        """Add environmental monitoring (extended functionality)"""
        print("🌿 Adding Environmental Monitoring...")
        # Additional environmental monitoring would be implemented here
        return self