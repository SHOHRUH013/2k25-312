"""
Comprehensive tests for SmartCity System
Tests all design patterns and system functionality
"""
import unittest
from core.controller import SmartCityController
from core.singleton.config_manager import ConfigManager
from core.factories.abstract_factory import (
    ResidentialSectorFactory, CommercialSectorFactory, SectorSetupManager
)
from core.factories.factory_method import SensorManager
from core.builders.system_builder import SmartCitySystemBuilder, AdvancedCityBuilder
from core.adapters.external_service_adapter import WeatherIntegrationManager
from core.proxy.security_proxy import SecurityProxy, RealSecuritySystem


class TestSmartCitySystem(unittest.TestCase):

    def test_singleton_pattern(self):
        """Test Singleton Pattern implementation"""
        config1 = ConfigManager.get_instance()
        config2 = ConfigManager.get_instance()
        self.assertIs(config1, config2, "Singleton instances should be the same")

        config1.set("test_key", "test_value")
        self.assertEqual(config2.get("test_key"), "test_value", "Singleton state should be shared")

    def test_abstract_factory_pattern(self):
        """Test Abstract Factory Pattern"""
        residential_factory = ResidentialSectorFactory()
        commercial_factory = CommercialSectorFactory()

        residential_manager = SectorSetupManager(residential_factory)
        commercial_manager = SectorSetupManager(commercial_factory)

        residential_setup = residential_manager.setup_sector()
        commercial_setup = commercial_manager.setup_sector()

        self.assertEqual(len(residential_setup), 3, "Residential sector should have 3 components")
        self.assertEqual(len(commercial_setup), 3, "Commercial sector should have 3 components")

        self.assertIn("residential", residential_setup[0].lower())
        self.assertIn("commercial", commercial_setup[0].lower())

    def test_factory_method_pattern(self):
        """Test Factory Method Pattern"""
        sensor_manager = SensorManager()
        deployments = sensor_manager.deploy_sensor_network()

        self.assertEqual(len(deployments), 4, "Should deploy 4 types of sensors")
        self.assertTrue(any("Traffic Sensor" in deploy for deploy in deployments))
        self.assertTrue(any("Lighting Sensor" in deploy for deploy in deployments))

    def test_builder_pattern(self):
        """Test Builder Pattern"""
        builder = SmartCitySystemBuilder()
        system = (builder
                  .add_transport_system()
                  .add_lighting_system()
                  .add_security_system()
                  .add_energy_system()
                  .build())

        self.assertTrue(system.is_operational, "System should be operational after build")
        self.assertIsNotNone(system.transport, "Transport system should be built")
        self.assertIsNotNone(system.lighting, "Lighting system should be built")

    def test_adapter_pattern(self):
        """Test Adapter Pattern"""
        weather_manager = WeatherIntegrationManager()
        report = weather_manager.get_weather_report()

        self.assertIsInstance(report, str, "Weather report should be a string")
        self.assertIn("SmartCity", report, "Report should include location")
        self.assertIn("Temperature", report, "Report should include temperature")

    def test_proxy_pattern(self):
        """Test Proxy Pattern"""
        real_system = RealSecuritySystem()
        proxy = SecurityProxy(real_system)

        # Test authentication
        self.assertTrue(proxy.authenticate('admin', 'admin123'))
        self.assertTrue(proxy.authenticate('operator', 'op123'))
        self.assertFalse(proxy.authenticate('admin', 'wrongpassword'))

    def test_facade_pattern(self):
        """Test Facade Pattern through controller"""
        controller = SmartCityController.get_instance()

        # Test facade methods
        status = controller.get_traffic_status()
        self.assertIsInstance(status, str, "Traffic status should be a string")

        lighting_status = controller.get_lighting_status()
        self.assertIsInstance(lighting_status, str, "Lighting status should be a string")

    def test_system_integration(self):
        """Test complete system integration"""
        controller = SmartCityController.get_instance()

        # Test emergency protocol
        controller.activate_emergency_protocol()

        # Test system status
        controller.get_system_status()

        # Test individual subsystems
        controller.optimize_traffic()
        controller.optimize_energy_distribution()

        print("✅ All integration tests passed!")


def run_performance_test():
    """Run performance and functionality tests"""
    print("\n" + "=" * 50)
    print("🧪 SMART CITY SYSTEM COMPREHENSIVE TEST")
    print("=" * 50)

    # Test Singleton
    print("\n1. Testing Singleton Pattern...")
    config = ConfigManager.get_instance()
    config.set("city_name", "TestCity")
    print(f"   ✅ Config value: {config.get('city_name')}")

    # Test Abstract Factory
    print("\n2. Testing Abstract Factory Pattern...")
    residential_factory = ResidentialSectorFactory()
    residential_manager = SectorSetupManager(residential_factory)
    residential_setup = residential_manager.setup_sector()
    print(f"   ✅ Residential setup: {len(residential_setup)} components")

    # Test Factory Method
    print("\n3. Testing Factory Method Pattern...")
    sensor_manager = SensorManager()
    deployments = sensor_manager.deploy_sensor_network()
    print(f"   ✅ Deployed {len(deployments)} sensor types")

    # Test Builder
    print("\n4. Testing Builder Pattern...")
    builder = SmartCitySystemBuilder()
    system = (builder
              .add_transport_system()
              .add_lighting_system()
              .build())
    print(f"   ✅ Built system: {system}")

    # Test Adapter
    print("\n5. Testing Adapter Pattern...")
    weather_manager = WeatherIntegrationManager()
    report = weather_manager.get_weather_report()
    print(f"   ✅ Weather report generated: {len(report)} characters")

    # Test Proxy
    print("\n6. Testing Proxy Pattern...")
    real_system = RealSecuritySystem()
    proxy = SecurityProxy(real_system)
    proxy.authenticate('admin', 'admin123')
    status = proxy.get_status()
    print(f"   ✅ Security status: {status}")

    print("\n🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    # Run unit tests
    unittest.main(exit=False, verbosity=2)

    # Run comprehensive performance test
    run_performance_test()