"""
SmartCity System - Unit Tests

Tests all design patterns and core functionality.
"""

import unittest
from core.controller import SmartCityController
from core.factories.district_factory import DistrictFactory, ResidentialDistrict
from modules.lighting.lighting_system import LightingSystem, StreetLight, LightGroup
from modules.transport.transport_manager import TransportManager, BusBuilder, VehicleDirector
from modules.security.security_system import SecuritySystem, SecurityCameraProxy
from modules.energy.energy_manager import EnergyManager, SolarPanel, BatteryStorageDecorator

class TestSingletonPattern(unittest.TestCase):
    """Test Singleton pattern implementation in SmartCityController."""
    
    def test_singleton_instance(self):
        """Test that only one instance of controller exists."""
        controller1 = SmartCityController.get_instance()
        controller2 = SmartCityController.get_instance()
        
        self.assertIs(controller1, controller2, 
                     "Controllers should be the same instance")
    
    def test_singleton_state(self):
        """Test that singleton maintains state."""
        controller = SmartCityController.get_instance()
        initial_district_count = len(controller.districts)
        
        controller.add_district("Test District", "residential")
        
        new_controller = SmartCityController.get_instance()
        self.assertEqual(len(new_controller.districts), initial_district_count + 1,
                        "State should be maintained across instances")

class TestFactoryPattern(unittest.TestCase):
    """Test Factory Method pattern in district creation."""
    
    def setUp(self):
        self.factory = DistrictFactory()
    
    def test_create_residential_district(self):
        """Test creation of residential district."""
        district = self.factory.create_district("residential", "Test Area")
        self.assertEqual(district.get_type(), "Residential")
        self.assertEqual(district.name, "Test Area")
    
    def test_create_commercial_district(self):
        """Test creation of commercial district."""
        district = self.factory.create_district("commercial", "Business Park")
        self.assertEqual(district.get_type(), "Commercial")
    
    def test_create_industrial_district(self):
        """Test creation of industrial district."""
        district = self.factory.create_district("industrial", "Factory Zone")
        self.assertEqual(district.get_type(), "Industrial")
    
    def test_default_district_type(self):
        """Test default district creation."""
        district = self.factory.create_district("unknown", "Unknown Area")
        self.assertEqual(district.get_type(), "Mixed-Use")

class TestCompositePattern(unittest.TestCase):
    """Test Composite pattern in lighting system."""
    
    def setUp(self):
        self.light1 = StreetLight("L1")
        self.light2 = StreetLight("L2")
        self.group = LightGroup("Test Group")
        self.group.add(self.light1)
        self.group.add(self.light2)
    
    def test_individual_light_control(self):
        """Test controlling individual lights."""
        self.light1.turn_on()
        self.assertTrue(self.light1.is_on)
        self.assertEqual(self.light1.brightness, 100)
    
    def test_group_control(self):
        """Test controlling group of lights."""
        self.group.turn_on()
        self.assertTrue(self.light1.is_on)
        self.assertTrue(self.light2.is_on)
    
    def test_brightness_control(self):
        """Test setting brightness on group."""
        self.group.set_brightness(50)
        self.assertEqual(self.light1.brightness, 50)
        self.assertEqual(self.light2.brightness, 50)
    
    def test_nested_groups(self):
        """Test nested light groups."""
        main_group = LightGroup("Main")
        sub_group = LightGroup("Sub")
        light3 = StreetLight("L3")
        
        sub_group.add(light3)
        main_group.add(self.group)
        main_group.add(sub_group)
        
        main_group.turn_on()
        self.assertTrue(light3.is_on)

class TestBuilderPattern(unittest.TestCase):
    """Test Builder pattern in vehicle construction."""
    
    def test_build_bus(self):
        """Test building a bus with all features."""
        builder = BusBuilder()
        director = VehicleDirector(builder)
        
        bus = director.construct_vehicle("B001")
        
        self.assertEqual(bus.vehicle_type, "Bus")
        self.assertEqual(bus.vehicle_id, "B001")
        self.assertEqual(bus.capacity, 50)
        self.assertEqual(bus.fuel_type, "Diesel")
        self.assertTrue(bus.gps_enabled)
    
    def test_vehicle_attributes(self):
        """Test that builder sets all attributes correctly."""
        builder = BusBuilder()
        director = VehicleDirector(builder)
        vehicle = director.construct_vehicle("TEST")
        
        self.assertIsNotNone(vehicle.vehicle_type)
        self.assertIsNotNone(vehicle.vehicle_id)
        self.assertGreater(vehicle.capacity, 0)
        self.assertIsNotNone(vehicle.fuel_type)

class TestProxyPattern(unittest.TestCase):
    """Test Proxy pattern in security cameras."""
    
    def test_lazy_initialization(self):
        """Test that camera is not initialized until accessed."""
        proxy = SecurityCameraProxy("CAM-TEST", "Test Location")
        
        # Real camera should not exist yet
        self.assertIsNone(proxy._real_camera)
        
        # Access camera feed - should trigger initialization
        feed = proxy.get_feed()
        
        # Real camera should now exist
        self.assertIsNotNone(proxy._real_camera)
        self.assertIn("CAM-TEST", feed)
    
    def test_access_logging(self):
        """Test that proxy logs access attempts."""
        proxy = SecurityCameraProxy("CAM-TEST", "Test Location")
        
        proxy.get_feed()
        proxy.record()
        
        self.assertEqual(len(proxy.access_log), 2)
        self.assertTrue(any("feed_requested" in log for log in proxy.access_log))
        self.assertTrue(any("recording_started" in log for log in proxy.access_log))

class TestDecoratorPattern(unittest.TestCase):
    """Test Decorator pattern in energy system."""
    
    def test_base_solar_panel(self):
        """Test basic solar panel without decorators."""
        solar = SolarPanel()
        
        self.assertEqual(solar.generate_power(), 500)
        self.assertEqual(solar.get_cost(), 0.05)
        self.assertEqual(solar.get_description(), "Solar Panel Array")
    
    def test_battery_decorator(self):
        """Test battery storage decorator."""
        solar = SolarPanel()
        solar_with_battery = BatteryStorageDecorator(solar)
        
        # Battery should increase effective power by 10%
        base_power = solar.generate_power()
        decorated_power = solar_with_battery.generate_power()
        
        self.assertGreater(decorated_power, base_power)
        self.assertIn("Battery Storage", solar_with_battery.get_description())
    
    def test_multiple_decorators(self):
        """Test stacking multiple decorators."""
        from modules.energy.energy_manager import SmartGridDecorator
        
        solar = SolarPanel()
        with_battery = BatteryStorageDecorator(solar)
        with_grid = SmartGridDecorator(with_battery)
        
        # Each decorator should add to the description
        description = with_grid.get_description()
        self.assertIn("Solar Panel", description)
        self.assertIn("Battery Storage", description)
        self.assertIn("Smart Grid", description)

class TestAdapterPattern(unittest.TestCase):
    """Test Adapter pattern in transport system."""
    
    def test_traffic_adapter(self):
        """Test that adapter converts legacy format correctly."""
        from modules.transport.transport_manager import LegacyTrafficSystem, TrafficSystemAdapter
        
        legacy = LegacyTrafficSystem()
        adapter = TrafficSystemAdapter(legacy)
        
        traffic_data = adapter.get_traffic_status()
        
        # Check that data is in expected format
        self.assertIn("congestion_level", traffic_data)
        self.assertIn("average_speed", traffic_data)
        self.assertIn("incidents", traffic_data)
        self.assertIn("status", traffic_data)
        
        # Check data types
        self.assertIsInstance(traffic_data["congestion_level"], int)
        self.assertIsInstance(traffic_data["status"], str)

class TestFacadePattern(unittest.TestCase):
    """Test Facade pattern in SmartCityController."""
    
    def test_facade_simplifies_subsystems(self):
        """Test that facade provides simple interface to complex subsystems."""
        controller = SmartCityController.get_instance()
        
        # Facade should allow simple operations without knowing subsystem details
        try:
            controller.control_lighting("on")
            controller.security_check()
            controller.check_energy()
            success = True
        except Exception:
            success = False
        
        self.assertTrue(success, "Facade should simplify subsystem access")
    
    def test_unified_status(self):
        """Test that facade provides unified status view."""
        controller = SmartCityController.get_instance()
        
        # Should be able to get status without directly accessing subsystems
        lighting_status = controller.lighting.get_status()
        transport_status = controller.transport.get_status()
        
        self.assertIsNotNone(lighting_status)
        self.assertIsNotNone(transport_status)

class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def test_system_initialization(self):
        """Test that the entire system initializes correctly."""
        controller = SmartCityController.get_instance()
        controller.initialize_city()
        
        self.assertGreater(len(controller.districts), 0)
        self.assertIsNotNone(controller.lighting)
        self.assertIsNotNone(controller.transport)
        self.assertIsNotNone(controller.security)
        self.assertIsNotNone(controller.energy)
    
    def test_emergency_mode(self):
        """Test that emergency mode affects all subsystems."""
        controller = SmartCityController.get_instance()
        
        try:
            controller.emergency_mode()
            success = True
        except Exception:
            success = False
        
        self.assertTrue(success, "Emergency mode should work across all systems")

def run_tests():
    """Run all tests with detailed output."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSingletonPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestFactoryPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestCompositePattern))
    suite.addTests(loader.loadTestsFromTestCase(TestBuilderPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestProxyPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestDecoratorPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestAdapterPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestFacadePattern))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    run_tests()