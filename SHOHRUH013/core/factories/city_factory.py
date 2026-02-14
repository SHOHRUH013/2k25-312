
from modules.lighting.lighting import BasicLightingSystem

class BasicCityFactory:
    def create_lighting(self, num_lights):
        return BasicLightingSystem(num_lights)

class AdvancedCityFactory(BasicCityFactory):
    pass
