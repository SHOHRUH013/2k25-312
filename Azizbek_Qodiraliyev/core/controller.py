"""
Central controller using Facade and Singleton patterns
Facade Pattern: Provides simplified interface to complex subsystem
Singleton Pattern: Ensures only one instance of controller exists
"""
from core.singleton.config_manager import ConfigManager
from core.proxy.security_proxy import SecurityProxy
from modules.transport.transport_system import TransportSystem
from modules.lighting.lighting_system import LightingSystem
from modules.security.security_system import SecuritySystem
from modules.energy.energy_system import EnergySystem

class SmartCityController:
    _instance = None

    def __init__(self):
        if SmartCityController._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.config = ConfigManager()
            self.transport_system = TransportSystem()
            self.lighting_system = LightingSystem()
            self.security_system = SecurityProxy(SecuritySystem())  # Proxy Pattern
            self.energy_system = EnergySystem()
            SmartCityController._instance = self

    @classmethod
    def get_instance(cls):
        """Singleton pattern: Get the single instance of controller"""
        if cls._instance is None:
            cls._instance = SmartCityController()
        return cls._instance

    # Facade Pattern: Simplified methods that hide subsystem complexity
    def optimize_traffic(self):
        """Facade method: Simplifies traffic optimization"""
        try:
            print("🔄 Optimizing city traffic...")
            result1 = self.transport_system.optimize_traffic_flow()
            result2 = self.transport_system.adjust_traffic_lights()
            print(f"✅ {result1}")
            print(f"✅ {result2}")
        except Exception as e:
            print(f"❌ Error optimizing traffic: {e}")

    def get_traffic_status(self):
        """Facade method: Gets comprehensive traffic status"""
        try:
            return self.transport_system.get_status()
        except Exception as e:
            return f"❌ Error getting traffic status: {e}"

    def manage_public_transport(self):
        """Facade method: Manages public transport system"""
        try:
            result = self.transport_system.coordinate_public_transport()
            print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error managing public transport: {e}")

    def adjust_street_lighting(self, intensity):
        """Facade method: Adjusts street lighting"""
        try:
            print(f"💡 Adjusting street lighting to {intensity}%")
            result = self.lighting_system.set_intensity(intensity)
            if result:
                print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error adjusting lighting: {e}")

    def get_lighting_status(self):
        """Facade method: Gets lighting system status"""
        try:
            return self.lighting_system.get_status()
        except Exception as e:
            return f"❌ Error getting lighting status: {e}"

    def toggle_emergency_lighting(self):
        """Facade method: Toggles emergency lighting"""
        try:
            result = self.lighting_system.emergency_mode()
            print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error toggling emergency lighting: {e}")

    def monitor_surveillance(self):
        """Facade method: Monitors security surveillance"""
        try:
            return self.security_system.monitor_cameras()
        except PermissionError as e:
            raise PermissionError(e)
        except Exception as e:
            return f"❌ Error monitoring surveillance: {e}"

    def activate_emergency_alert(self):
        """Facade method: Activates emergency alerts"""
        try:
            return self.security_system.emergency_alert()
        except PermissionError as e:
            raise PermissionError(e)
        except Exception as e:
            return f"❌ Error activating emergency alert: {e}"

    def get_security_status(self):
        """Facade method: Gets security system status"""
        try:
            return self.security_system.get_status()
        except PermissionError as e:
            raise PermissionError(e)
        except Exception as e:
            return f"❌ Error getting security status: {e}"

    def optimize_energy_distribution(self):
        """Facade method: Optimizes energy distribution"""
        try:
            print("⚡ Optimizing energy distribution...")
            result = self.energy_system.distribute_power()
            print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error optimizing energy distribution: {e}")

    def get_energy_consumption(self):
        """Facade method: Gets energy consumption data"""
        try:
            return self.energy_system.get_consumption_report()
        except Exception as e:
            return f"❌ Error getting energy consumption: {e}"

    def toggle_renewable_sources(self):
        """Facade method: Toggles renewable energy sources"""
        try:
            result = self.energy_system.toggle_renewable()
            print(f"✅ {result}")
        except Exception as e:
            print(f"❌ Error toggling renewable sources: {e}")

    def get_system_status(self):
        """Facade method: Gets complete system status"""
        print("\n📊 SmartCity System Status:")
        print("-" * 30)
        try:
            print(f"Transport: {self.transport_system.get_status()}")
            print(f"Lighting: {self.lighting_system.get_status()}")
            security_status = self.security_system.get_status()
            print(f"Security: {security_status}")
        except PermissionError:
            print("Security: 🔒 Authentication required")
        except Exception as e:
            print(f"Security: ❌ Error: {e}")
        try:
            print(f"Energy: {self.energy_system.get_status()}")
        except Exception as e:
            print(f"Energy: ❌ Error: {e}")

    def activate_emergency_protocol(self):
        """Facade method: Activates emergency protocol across all systems"""
        print("🚨 ACTIVATING EMERGENCY PROTOCOL!")
        try:
            # Use direct methods to avoid proxy authentication in emergencies
            transport_result = self.transport_system.emergency_mode()
            lighting_result = self.lighting_system.emergency_mode()
            energy_result = self.energy_system.emergency_mode()

            print(f"✅ {transport_result}")
            print(f"✅ {lighting_result}")
            print(f"✅ {energy_result}")

            # Try security but don't fail if authentication is required
            try:
                security_result = self.security_system.emergency_alert()
                print(f"✅ {security_result}")
            except PermissionError:
                print("⚠️ Security system requires authentication - using direct emergency mode")
                real_security = self.security_system._real_system
                security_result = real_security.emergency_alert()
                print(f"✅ {security_result}")

            print("✅ Emergency protocol activated across all systems!")
        except Exception as e:
            print(f"⚠️ Emergency protocol partially activated: {e}")