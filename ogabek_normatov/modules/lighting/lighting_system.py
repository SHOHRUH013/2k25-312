"""
Lighting System - Manages city lighting infrastructure

Design Pattern: COMPOSITE
Allows treating individual lights and groups of lights uniformly.
"""

from abc import ABC, abstractmethod

class LightComponent(ABC):
    """
    Pattern: COMPOSITE
    Abstract component for both individual lights and light groups.
    """
    
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def set_brightness(self, level):
        pass
    
    @abstractmethod
    def get_status(self):
        pass

class StreetLight(LightComponent):
    """Leaf component - individual street light."""
    
    def __init__(self, light_id):
        self.light_id = light_id
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
    
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
    
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            self.is_on = level > 0
    
    def get_status(self):
        status = "ON" if self.is_on else "OFF"
        return f"Light {self.light_id}: {status} (Brightness: {self.brightness}%)"

class LightGroup(LightComponent):
    """
    Composite component - group of lights.
    Can contain both individual lights and other groups.
    """
    
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def remove(self, component):
        self.children.remove(component)
    
    def turn_on(self):
        for child in self.children:
            child.turn_on()
    
    def turn_off(self):
        for child in self.children:
            child.turn_off()
    
    def set_brightness(self, level):
        for child in self.children:
            child.set_brightness(level)
    
    def get_status(self):
        statuses = [child.get_status() for child in self.children]
        return f"{self.name}: {len(self.children)} lights managed"

class LightingSystem:
    """Main lighting system controller using Composite pattern."""
    
    def __init__(self):
        # Create root composite
        self.root = LightGroup("City Lighting")
        self.emergency_active = False
        
        # Create district groups
        self._setup_districts()
    
    def _setup_districts(self):
        """Initialize lighting structure with districts and lights."""
        # Downtown district
        downtown = LightGroup("Downtown")
        for i in range(1, 6):
            downtown.add(StreetLight(f"DT-{i}"))
        self.root.add(downtown)
        
        # Residential district
        residential = LightGroup("Residential")
        for i in range(1, 9):
            residential.add(StreetLight(f"RES-{i}"))
        self.root.add(residential)
        
        # Industrial district
        industrial = LightGroup("Industrial")
        for i in range(1, 4):
            industrial.add(StreetLight(f"IND-{i}"))
        self.root.add(industrial)
    
    def turn_on_all(self):
        """Turn on all city lights."""
        self.root.turn_on()
        print("✅ All lights turned ON")
    
    def turn_off_all(self):
        """Turn off all city lights."""
        self.root.turn_off()
        print("✅ All lights turned OFF")
    
    def set_brightness(self, level):
        """Set brightness for all lights."""
        self.root.set_brightness(level)
        print(f"✅ Brightness set to {level}%")
    
    def get_status(self):
        """Get overall lighting status."""
        return self.root.get_status()
    
    def emergency_mode(self):
        """Activate emergency lighting (full brightness)."""
        self.emergency_active = True
        self.root.turn_on()
        print("🚨 Emergency lighting activated (100% brightness)")
    
    def generate_report(self):
        """Generate lighting system report."""
        print("\n💡 LIGHTING SYSTEM REPORT")
        print("-" * 40)
        print(self.root.get_status())
        for group in self.root.children:
            print(f"  • {group.get_status()}")
    
    def shutdown(self):
        """Shutdown lighting system."""
        self.turn_off_all()
        print("💡 Lighting system shutdown")