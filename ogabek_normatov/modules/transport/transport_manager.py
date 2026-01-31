"""
Transport Management System

Design Patterns:
1. BUILDER - Complex vehicle construction
2. ADAPTER - Integration with external traffic system
"""

from abc import ABC, abstractmethod

# BUILDER PATTERN

class Vehicle:
    """Complex vehicle object built step by step."""
    
    def __init__(self):
        self.vehicle_type = None
        self.vehicle_id = None
        self.capacity = 0
        self.fuel_type = None
        self.gps_enabled = False
        self.route = None
    
    def __str__(self):
        return (f"{self.vehicle_type} {self.vehicle_id} "
                f"(Capacity: {self.capacity}, Fuel: {self.fuel_type}, "
                f"GPS: {self.gps_enabled})")

class VehicleBuilder(ABC):
    """
    Pattern: BUILDER
    Abstract builder for constructing vehicles step by step.
    """
    
    def __init__(self):
        self.vehicle = Vehicle()
    
    @abstractmethod
    def set_type(self):
        pass
    
    @abstractmethod
    def set_capacity(self):
        pass
    
    @abstractmethod
    def set_fuel_type(self):
        pass
    
    def set_gps(self):
        self.vehicle.gps_enabled = True
        return self
    
    def set_route(self, route):
        self.vehicle.route = route
        return self
    
    def build(self):
        return self.vehicle

class BusBuilder(VehicleBuilder):
    """Concrete builder for buses."""
    
    def set_type(self):
        self.vehicle.vehicle_type = "Bus"
        return self
    
    def set_capacity(self):
        self.vehicle.capacity = 50
        return self
    
    def set_fuel_type(self):
        self.vehicle.fuel_type = "Diesel"
        return self

class CarBuilder(VehicleBuilder):
    """Concrete builder for cars."""
    
    def set_type(self):
        self.vehicle.vehicle_type = "Car"
        return self
    
    def set_capacity(self):
        self.vehicle.capacity = 4
        return self
    
    def set_fuel_type(self):
        self.vehicle.fuel_type = "Electric"
        return self

class TramBuilder(VehicleBuilder):
    """Concrete builder for trams."""
    
    def set_type(self):
        self.vehicle.vehicle_type = "Tram"
        return self
    
    def set_capacity(self):
        self.vehicle.capacity = 100
        return self
    
    def set_fuel_type(self):
        self.vehicle.fuel_type = "Electric"
        return self

class VehicleDirector:
    """Director that constructs vehicles using builders."""
    
    def __init__(self, builder):
        self.builder = builder
    
    def construct_vehicle(self, vehicle_id):
        """Construct a complete vehicle."""
        self.builder.vehicle.vehicle_id = vehicle_id
        return (self.builder
                .set_type()
                .set_capacity()
                .set_fuel_type()
                .set_gps()
                .build())

# ADAPTER PATTERN

class LegacyTrafficSystem:
    """
    Legacy traffic management system with incompatible interface.
    (Simulates external system)
    """
    
    def __init__(self):
        self.traffic_data = {
            "congestion_level": 3,
            "average_speed": 45,
            "incidents": 2
        }
    
    def get_traffic_info(self):
        """Returns traffic data in old format."""
        return f"TRAFFIC|{self.traffic_data['congestion_level']}|{self.traffic_data['average_speed']}|{self.traffic_data['incidents']}"

class TrafficSystemAdapter:
    """
    Pattern: ADAPTER
    Adapts the legacy traffic system to work with our modern interface.
    """
    
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system
    
    def get_traffic_status(self):
        """Converts legacy format to modern dictionary format."""
        raw_data = self.legacy_system.get_traffic_info()
        parts = raw_data.split("|")
        
        return {
            "congestion_level": int(parts[1]),
            "average_speed": int(parts[2]),
            "incidents": int(parts[3]),
            "status": self._interpret_congestion(int(parts[1]))
        }
    
    def _interpret_congestion(self, level):
        """Convert numeric level to human-readable status."""
        if level <= 2:
            return "Light"
        elif level <= 4:
            return "Moderate"
        else:
            return "Heavy"

# TRANSPORT MANAGER

class TransportManager:
    """Main transport management system."""
    
    def __init__(self):
        self.vehicles = []
        
        # Setup adapter for legacy traffic system
        legacy_system = LegacyTrafficSystem()
        self.traffic_adapter = TrafficSystemAdapter(legacy_system)
        
        # Initialize with some default vehicles
        self._initialize_fleet()
    
    def _initialize_fleet(self):
        """Initialize the vehicle fleet using Builder pattern."""
        # Create buses
        for i in range(1, 4):
            director = VehicleDirector(BusBuilder())
            bus = director.construct_vehicle(f"B{i:03d}")
            self.vehicles.append(bus)
        
        # Create trams
        for i in range(1, 3):
            director = VehicleDirector(TramBuilder())
            tram = director.construct_vehicle(f"T{i:03d}")
            self.vehicles.append(tram)
    
    def add_vehicle(self, vehicle_type, vehicle_id):
        """Add a new vehicle using Builder pattern."""
        builder = None
        
        if vehicle_type.lower() == "bus":
            builder = BusBuilder()
        elif vehicle_type.lower() == "car":
            builder = CarBuilder()
        elif vehicle_type.lower() == "tram":
            builder = TramBuilder()
        else:
            print(f"❌ Unknown vehicle type: {vehicle_type}")
            return
        
        director = VehicleDirector(builder)
        vehicle = director.construct_vehicle(vehicle_id)
        self.vehicles.append(vehicle)
        print(f"✅ Added vehicle: {vehicle}")
    
    def optimize_traffic(self):
        """Optimize traffic flow using adapted traffic data."""
        traffic_status = self.traffic_adapter.get_traffic_status()
        
        print("\n🚦 OPTIMIZING TRAFFIC FLOW")
        print(f"Current Status: {traffic_status['status']}")
        print(f"Congestion Level: {traffic_status['congestion_level']}/5")
        print(f"Average Speed: {traffic_status['average_speed']} km/h")
        print(f"Active Incidents: {traffic_status['incidents']}")
        
        if traffic_status['congestion_level'] > 3:
            print("⚠️  High congestion detected - rerouting vehicles")
        else:
            print("✅ Traffic flow is optimal")
    
    def get_status(self):
        """Get transport system status."""
        return f"{len(self.vehicles)} vehicles active"
    
    def generate_report(self):
        """Generate transport report."""
        print("\n🚗 TRANSPORT SYSTEM REPORT")
        print("-" * 40)
        print(f"Total Vehicles: {len(self.vehicles)}")
        
        vehicle_types = {}
        for vehicle in self.vehicles:
            v_type = vehicle.vehicle_type
            vehicle_types[v_type] = vehicle_types.get(v_type, 0) + 1
        
        for v_type, count in vehicle_types.items():
            print(f"  • {v_type}s: {count}")
        
        # Show traffic status via adapter
        traffic = self.traffic_adapter.get_traffic_status()
        print(f"\nTraffic Status: {traffic['status']}")
    
    def emergency_mode(self):
        """Activate emergency transport protocols."""
        print("🚨 Emergency transport mode: Priority routing activated")
    
    def shutdown(self):
        """Shutdown transport system."""
        print("🚗 Transport system shutdown")