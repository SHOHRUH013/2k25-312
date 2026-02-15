"""
SmartCity Controller - Central Management System

Design Patterns Used:
1. Singleton - Ensures only one controller instance exists
2. Facade - Provides simplified interface to complex subsystems
"""

from modules.lighting.lighting_system import LightingSystem
from modules.transport.transport_manager import TransportManager
from modules.security.security_system import SecuritySystem
from modules.energy.energy_manager import EnergyManager
from core.factories.district_factory import DistrictFactory

class SmartCityController:
    """
    Pattern: SINGLETON
    Ensures only one instance of the city controller exists.
    
    Pattern: FACADE
    Provides a unified interface to all city subsystems.
    """
    
    _instance = None
    
    def __new__(cls):
        """Singleton implementation - ensures single instance."""
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        """Get the singleton instance of the controller."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        """Initialize the controller and subsystems."""
        if self._initialized:
            return
            
        self._initialized = True
        self.districts = []
        
        # Initialize subsystems (Facade pattern - hiding complexity)
        self.lighting = LightingSystem()
        self.transport = TransportManager()
        self.security = SecuritySystem()
        self.energy = EnergyManager()
        self.district_factory = DistrictFactory()
        
        print("🔧 SmartCity Controller initialized (Singleton)")
    
    def initialize_city(self):
        """Initialize the city with default districts."""
        print("🏗️ Building city infrastructure...")
        
        # Create different types of districts using Factory
        self.add_district("Downtown", "commercial")
        self.add_district("Residential Area", "residential")
        self.add_district("Industrial Zone", "industrial")
        
        print(f"✅ Created {len(self.districts)} districts")
    
    def add_district(self, name, district_type="mixed"):
        """
        Add a new district to the city.
        Uses Factory pattern to create appropriate district type.
        """
        district = self.district_factory.create_district(district_type, name)
        self.districts.append(district)
        print(f"➕ Added district: {district.get_info()}")
    
    def display_city_status(self):
        """Display comprehensive city status (Facade pattern in action)."""
        print("\n" + "="*60)
        print("📊 CITY STATUS REPORT")
        print("="*60)
        
        print(f"\n🏙️ Districts: {len(self.districts)}")
        for district in self.districts:
            print(f"   • {district.get_info()}")
        
        print(f"\n💡 Lighting: {self.lighting.get_status()}")
        print(f"🚗 Transport: {self.transport.get_status()}")
        print(f"🔒 Security: {self.security.get_status()}")
        print(f"⚡ Energy: {self.energy.get_status()}")
        print("="*60)
    
    def control_lighting(self, action, value=None):
        """Control city lighting system."""
        if action == "on":
            self.lighting.turn_on_all()
        elif action == "off":
            self.lighting.turn_off_all()
        elif action == "dim" and value is not None:
            self.lighting.set_brightness(value)
        print(f"💡 Lighting: {self.lighting.get_status()}")
    
    def manage_traffic(self, action):
        """Manage city traffic."""
        if action == "optimize":
            self.transport.optimize_traffic()
        elif action == "report":
            self.transport.generate_report()
    
    def add_vehicle(self, vehicle_type, vehicle_id):
        """Add a new vehicle to the transport system."""
        self.transport.add_vehicle(vehicle_type, vehicle_id)
    
    def security_check(self):
        """Perform security system check."""
        self.security.perform_check()
    
    def trigger_alarm(self, location):
        """Trigger security alarm at location."""
        self.security.trigger_alarm(location)
    
    def view_cameras(self):
        """View security camera feeds."""
        self.security.view_cameras()
    
    def check_energy(self):
        """Check energy consumption."""
        self.energy.display_consumption()
    
    def optimize_energy(self):
        """Optimize energy usage across the city."""
        self.energy.optimize()
        print("✅ Energy optimization complete")
    
    def switch_energy_source(self, source):
        """Switch to different energy source."""
        self.energy.switch_source(source)
    
    def emergency_mode(self):
        """Activate emergency protocols across all systems."""
        print("\n🚨 EMERGENCY MODE ACTIVATED")
        self.lighting.emergency_mode()
        self.transport.emergency_mode()
        self.security.emergency_mode()
        self.energy.emergency_mode()
        print("✅ All systems in emergency mode")
    
    def generate_report(self):
        """Generate comprehensive system report."""
        print("\n📋 GENERATING SYSTEM REPORT...")
        print("="*60)
        self.display_city_status()
        print("\n📈 Detailed Subsystem Reports:")
        self.lighting.generate_report()
        self.transport.generate_report()
        self.security.generate_report()
        self.energy.generate_report()
        print("="*60)
    
    def shutdown(self):
        """Safely shutdown all city systems."""
        print("🔌 Shutting down subsystems...")
        self.lighting.shutdown()
        self.transport.shutdown()
        self.security.shutdown()
        self.energy.shutdown()
        print("✅ All subsystems shut down")