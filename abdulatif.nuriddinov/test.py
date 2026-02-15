"""
Unit tests for SmartCity System
"""
import unittest
from unittest.mock import Mock, patch
from core.singleton.config_manager import ConfigManager
from core.factories.subsystem_factory import StandardCityFactory, EcoCityFactory
from core.builders.alert_builder import CityAlertBuilder, AlertDirector
from core.adapters.weather_adapter import WeatherServiceAdapter, ExternalWeatherService
from core.proxy.security_proxy import SecurityProxy
from core.controller import SmartCityController


class TestConfigManager(unittest.TestCase):
    def test_singleton_pattern(self):
        """Test that ConfigManager is a singleton"""
        config1 = ConfigManager()
        config2 = ConfigManager()
        self.assertIs(config1, config2)

    def test_config_operations(self):
        """Test configuration operations"""
        config = ConfigManager()
        config.set('test_key', 'test_value')
        self.assertEqual(config.get('test_key'), 'test_value')


class TestAbstractFactory(unittest.TestCase):
    def test_standard_factory(self):
        """Test StandardCityFactory creates correct subsystems"""
        factory = StandardCityFactory()
        transport = factory.create_transport_system()
        lighting = factory.create_lighting_system()
        security = factory.create_security_system()
        energy = factory.create_energy_system()

        self.assertIsNotNone(transport)
        self.assertIsNotNone(lighting)
        self.assertIsNotNone(security)
        self.assertIsNotNone(energy)

    def test_eco_factory(self):
        """Test EcoCityFactory creates eco-friendly subsystems"""
        factory = EcoCityFactory()
        transport = factory.create_transport_system()
        lighting = factory.create_lighting_system()

        # These should have eco mode enabled
        self.assertTrue(hasattr(transport, '_eco_mode') or hasattr(lighting, '_energy_saving'))


class TestBuilderPattern(unittest.TestCase):
    def test_alert_builder(self):
        """Test alert builder creates alerts correctly"""
        builder = CityAlertBuilder()
        alert = (builder
                 .set_type("Test")
                 .set_severity("High")
                 .set_message("Test message")
                 .set_location("Test location")
                 .build())

        self.assertEqual(alert.type, "Test")
        self.assertEqual(alert.severity, "High")
        self.assertEqual(alert.message, "Test message")
        self.assertEqual(alert.location, "Test location")

    def test_alert_director(self):
        """Test alert director constructs specific alerts"""
        builder = CityAlertBuilder()
        director = AlertDirector(builder)

        alert = director.construct_traffic_alert("Main Street", "High")
        self.assertEqual(alert.type, "Traffic")
        self.assertEqual(alert.location, "Main Street")
        self.assertEqual(alert.severity, "High")


class TestAdapterPattern(unittest.TestCase):
    def test_weather_adapter(self):
        """Test weather adapter converts external service data"""
        external_service = ExternalWeatherService()
        adapter = WeatherServiceAdapter(external_service)

        weather_data = adapter.get_weather("TestCity")

        self.assertIn('temperature', weather_data)
        self.assertIn('condition', weather_data)
        self.assertIn('recommendations', weather_data)
        self.assertIsInstance(weather_data['recommendations'], list)


class TestProxyPattern(unittest.TestCase):
    def test_security_proxy_access(self):
        """Test security proxy controls access"""
        mock_security = Mock()
        proxy = SecurityProxy(mock_security)

        # Test unauthorized access
        result = proxy.monitor_area('unauthorized_user', 'CAM-001')
        self.assertIsNone(result)

        # Test authorized access
        mock_security.monitor_area.return_value = {'status': 'ACTIVE'}
        result = proxy.monitor_area('admin', 'CAM-001')
        self.assertIsNotNone(result)


class TestController(unittest.TestCase):
    def test_controller_singleton(self):
        """Test controller is a singleton"""
        controller1 = SmartCityController()
        controller2 = SmartCityController()
        self.assertIs(controller1, controller2)

    def test_facade_methods(self):
        """Test facade methods work correctly"""
        controller = SmartCityController()

        status = controller.get_city_status()
        self.assertIn('city', status)
        self.assertIn('system_status', status)
        self.assertIn('subsystems', status)

        # Test alert creation
        alert = controller.create_alert("Test", "Location", "Low")
        self.assertEqual(alert.type, "Test")
        self.assertEqual(alert.location, "Location")


class TestIntegration(unittest.TestCase):
    def test_system_integration(self):
        """Test integrated system functionality"""
        # Create controller (which initializes all subsystems)
        controller = SmartCityController()

        # Test all subsystems are initialized
        self.assertIsNotNone(controller.transport)
        self.assertIsNotNone(controller.lighting)
        self.assertIsNotNone(controller.security_proxy)
        self.assertIsNotNone(controller.energy)

        # Test facade method
        city_status = controller.get_city_status()
        self.assertEqual(city_status['city'], controller.city_name)

        # Test factory pattern
        self.assertIsInstance(controller.factory, StandardCityFactory)


def run_tests():
    """Run all tests"""
    test_suite = unittest.TestLoader().loadTestsFromModule(__name__)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    run_tests()