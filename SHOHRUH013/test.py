
import unittest
from core.controller import SmartCityController
from core.factories.city_factory import BasicCityFactory
from core.builders.city_builder import CityConfigBuilder

class TestSmartCity(unittest.TestCase):

    def setUp(self):
        factory = BasicCityFactory()
        config = (
            CityConfigBuilder()
            .set_city_name("TestCity")
            .set_num_lights(3)
            .set_num_buses(2)
            .set_strict_security(False)
            .build()
        )
        self.controller = SmartCityController(factory=factory, config=config)

    def test_lighting(self):
        self.controller.lighting_on()
        self.assertIn("ON", self.controller.get_status())

if __name__ == "__main__":
    unittest.main()
