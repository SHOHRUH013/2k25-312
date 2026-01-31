"""
Energy Management System

Design Pattern: DECORATOR
Adds additional features to energy sources dynamically.
"""

from abc import ABC, abstractmethod

class EnergySource(ABC):
    """
    Pattern: DECORATOR
    Abstract component for energy sources.
    """
    
    @abstractmethod
    def generate_power(self):
        """Return power generation amount in kW."""
        pass
    
    @abstractmethod
    def get_cost(self):
        """Return cost per kWh."""
        pass
    
    @abstractmethod
    def get_description(self):
        """Return description of the energy source."""
        pass

class CoalPowerPlant(EnergySource):
    """Concrete component - basic coal power plant."""
    
    def generate_power(self):
        return 1000  # kW
    
    def get_cost(self):
        return 0.08  # $/kWh
    
    def get_description(self):
        return "Coal Power Plant"

class SolarPanel(EnergySource):
    """Concrete component - solar panel array."""
    
    def generate_power(self):
        return 500  # kW
    
    def get_cost(self):
        return 0.05  # $/kWh
    
    def get_description(self):
        return "Solar Panel Array"

class WindTurbine(EnergySource):
    """Concrete component - wind turbine farm."""
    
    def generate_power(self):
        return 800  # kW
    
    def get_cost(self):
        return 0.06  # $/kWh
    
    def get_description(self):
        return "Wind Turbine Farm"

# DECORATORS

class EnergySourceDecorator(EnergySource):
    """
    Pattern: DECORATOR
    Base decorator class that wraps an energy source.
    """
    
    def __init__(self, energy_source):
        self._energy_source = energy_source
    
    def generate_power(self):
        return self._energy_source.generate_power()
    
    def get_cost(self):
        return self._energy_source.get_cost()
    
    def get_description(self):
        return self._energy_source.get_description()

class BatteryStorageDecorator(EnergySourceDecorator):
    """
    Decorator: Adds battery storage capability.
    Stores excess energy for later use.
    """
    
    def __init__(self, energy_source):
        super().__init__(energy_source)
        self.storage_capacity = 200  # kWh
        self.stored_energy = 0
    
    def generate_power(self):
        base_power = self._energy_source.generate_power()
        # Add 10% more effective power due to storage buffering
        return base_power * 1.1
    
    def get_description(self):
        return f"{self._energy_source.get_description()} + Battery Storage (200 kWh)"

class SmartGridDecorator(EnergySourceDecorator):
    """
    Decorator: Adds smart grid optimization.
    Reduces energy waste through intelligent distribution.
    """
    
    def __init__(self, energy_source):
        super().__init__(energy_source)
        self.efficiency_boost = 1.15
    
    def generate_power(self):
        base_power = self._energy_source.generate_power()
        return base_power * self.efficiency_boost
    
    def get_cost(self):
        # Smart grid reduces operational costs
        base_cost = self._energy_source.get_cost()
        return base_cost * 0.9
    
    def get_description(self):
        return f"{self._energy_source.get_description()} + Smart Grid (+15% efficiency)"

class CarbonCaptureDecorator(EnergySourceDecorator):
    """
    Decorator: Adds carbon capture technology.
    Reduces environmental impact of fossil fuel plants.
    """
    
    def __init__(self, energy_source):
        super().__init__(energy_source)
        self.capture_rate = 0.9  # 90% CO2 capture
    
    def get_cost(self):
        # Carbon capture adds cost
        base_cost = self._energy_source.get_cost()
        return base_cost * 1.2
    
    def get_description(self):
        return f"{self._energy_source.get_description()} + Carbon Capture (90% reduction)"

# ENERGY MANAGER

class EnergyManager:
    """Main energy management system using Decorator pattern."""
    
    def __init__(self):
        # Start with a basic coal plant
        self.primary_source = CoalPowerPlant()
        
        # Store decorated versions
        self.enhanced_sources = []
        
        # Initialize with some decorators
        self._setup_enhanced_sources()
        
        self.total_consumption = 2500  # kW
        self.emergency_mode_active = False
    
    def _setup_enhanced_sources(self):
        """Setup enhanced energy sources using decorators."""
        # Solar with battery storage
        solar = SolarPanel()
        solar_with_battery = BatteryStorageDecorator(solar)
        self.enhanced_sources.append(solar_with_battery)
        
        # Wind with smart grid
        wind = WindTurbine()
        wind_with_grid = SmartGridDecorator(wind)
        self.enhanced_sources.append(wind_with_grid)
        
        # Coal with carbon capture and smart grid
        coal = CoalPowerPlant()
        coal_with_capture = CarbonCaptureDecorator(coal)
        coal_enhanced = SmartGridDecorator(coal_with_capture)
        self.enhanced_sources.append(coal_enhanced)
    
    def display_consumption(self):
        """Display current energy consumption and generation."""
        print("\n⚡ ENERGY CONSUMPTION REPORT")
        print("-" * 50)
        print(f"Total City Consumption: {self.total_consumption} kW")
        
        total_generation = sum(source.generate_power() for source in self.enhanced_sources)
        print(f"Total Generation: {total_generation:.0f} kW")
        
        balance = total_generation - self.total_consumption
        if balance >= 0:
            print(f"✅ Energy Balance: +{balance:.0f} kW (surplus)")
        else:
            print(f"⚠️  Energy Balance: {balance:.0f} kW (deficit)")
        
        print("\n📊 Active Energy Sources:")
        for source in self.enhanced_sources:
            power = source.generate_power()
            cost = source.get_cost()
            print(f"  • {source.get_description()}")
            print(f"    Power: {power:.0f} kW | Cost: ${cost:.3f}/kWh")
    
    def switch_source(self, source_type):
        """Switch to a different energy source."""
        if source_type == "renewable":
            print("\n🌱 Switching to renewable energy sources...")
            # Keep only solar and wind
            self.enhanced_sources = [s for s in self.enhanced_sources 
                                    if "Solar" in s.get_description() 
                                    or "Wind" in s.get_description()]
            print("✅ Now running on 100% renewable energy")
        elif source_type == "efficient":
            print("\n⚡ Optimizing for maximum efficiency...")
            # Add more smart grid decorators
            print("✅ Efficiency mode activated")
    
    def optimize(self):
        """Optimize energy distribution and usage."""
        print("\n🔧 OPTIMIZING ENERGY SYSTEM")
        
        # Calculate current efficiency
        total_gen = sum(s.generate_power() for s in self.enhanced_sources)
        efficiency = (min(total_gen, self.total_consumption) / self.total_consumption) * 100
        
        print(f"Current Efficiency: {efficiency:.1f}%")
        
        if efficiency < 100:
            print("⚠️  Adding supplementary sources...")
            # Add another renewable source
            wind = WindTurbine()
            wind_enhanced = SmartGridDecorator(wind)
            self.enhanced_sources.append(wind_enhanced)
            print(f"✅ Added: {wind_enhanced.get_description()}")
        else:
            print("✅ System operating at optimal efficiency")
    
    def emergency_mode(self):
        """Activate emergency power protocols."""
        self.emergency_mode_active = True
        print("🚨 Emergency power mode: Priority systems only")
        self.total_consumption = 1500  # Reduce to essential services
        print(f"Consumption reduced to {self.total_consumption} kW")
    
    def get_status(self):
        """Get energy system status."""
        total_gen = sum(s.generate_power() for s in self.enhanced_sources)
        sources_count = len(self.enhanced_sources)
        return f"{sources_count} sources active, {total_gen:.0f} kW total"
    
    def generate_report(self):
        """Generate comprehensive energy report."""
        print("\n⚡ ENERGY SYSTEM REPORT")
        print("-" * 50)
        
        total_generation = sum(s.generate_power() for s in self.enhanced_sources)
        avg_cost = sum(s.get_cost() for s in self.enhanced_sources) / len(self.enhanced_sources)
        
        print(f"Active Sources: {len(self.enhanced_sources)}")
        print(f"Total Generation: {total_generation:.0f} kW")
        print(f"Average Cost: ${avg_cost:.3f}/kWh")
        print(f"City Consumption: {self.total_consumption} kW")
        
        renewable_count = sum(1 for s in self.enhanced_sources 
                            if "Solar" in s.get_description() 
                            or "Wind" in s.get_description())
        
        renewable_pct = (renewable_count / len(self.enhanced_sources)) * 100
        print(f"Renewable Energy: {renewable_pct:.0f}%")
    
    def shutdown(self):
        """Shutdown energy system."""
        print("⚡ Energy system shutdown")