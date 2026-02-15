"""
District Factory - Creates different types of city districts

Design Pattern: FACTORY METHOD
Defines an interface for creating objects, letting subclasses decide which class to instantiate.
"""

from abc import ABC, abstractmethod

class District(ABC):
    """Abstract base class for all district types."""
    
    def __init__(self, name):
        self.name = name
        self.population = 0
        self.buildings = []
    
    @abstractmethod
    def get_type(self):
        """Return the type of district."""
        pass
    
    def get_info(self):
        """Return district information."""
        return f"{self.name} ({self.get_type()})"

class ResidentialDistrict(District):
    """Residential district with homes and apartments."""
    
    def __init__(self, name):
        super().__init__(name)
        self.population = 5000
        self.buildings = ["Apartment Complex", "Houses", "Parks"]
    
    def get_type(self):
        return "Residential"

class CommercialDistrict(District):
    """Commercial district with shops and offices."""
    
    def __init__(self, name):
        super().__init__(name)
        self.population = 2000
        self.buildings = ["Shopping Mall", "Offices", "Restaurants"]
    
    def get_type(self):
        return "Commercial"

class IndustrialDistrict(District):
    """Industrial district with factories and warehouses."""
    
    def __init__(self, name):
        super().__init__(name)
        self.population = 500
        self.buildings = ["Factory", "Warehouse", "Processing Plant"]
    
    def get_type(self):
        return "Industrial"

class MixedDistrict(District):
    """Mixed-use district with various building types."""
    
    def __init__(self, name):
        super().__init__(name)
        self.population = 3000
        self.buildings = ["Mixed-use Buildings", "Community Center"]
    
    def get_type(self):
        return "Mixed-Use"

class DistrictFactory:
    """
    Pattern: FACTORY METHOD
    Creates appropriate district types based on input.
    """
    
    def create_district(self, district_type, name):
        """
        Factory method to create different types of districts.
        
        Args:
            district_type: Type of district (residential/commercial/industrial/mixed)
            name: Name of the district
            
        Returns:
            District object of appropriate type
        """
        district_type = district_type.lower()
        
        if district_type == "residential":
            return ResidentialDistrict(name)
        elif district_type == "commercial":
            return CommercialDistrict(name)
        elif district_type == "industrial":
            return IndustrialDistrict(name)
        elif district_type == "mixed":
            return MixedDistrict(name)
        else:
            # Default to mixed district
            return MixedDistrict(name)