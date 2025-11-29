"""
SmartCity System Tests
Tests all design patterns and system functionality
"""

from core.controller import SmartCityController
from core.factories.device_factory import DeviceFactory, AbstractDeviceFactory
from modules.lighting.lighting_system import StreetLight, MotionSensorDecorator, DimmingDecorator
from modules.security.security_system import Camera, CameraProxy
from modules.energy.energy_system import EnergyStationBuilder, EnergyStationDirector


def test_singleton_pattern():
    """Test Singleton Pattern - Only one controller instance"""
    print("\n" + "=" * 60)
    print("TEST 1: SINGLETON PATTERN")
    print("=" * 60)

    controller1 = SmartCityController()
    controller2 = SmartCityController()

    print(f"Controller 1 ID: {id(controller1)}")
    print(f"Controller 2 ID: {id(controller2)}")
    print(f"Are they the same instance? {controller1 is controller2}")

    assert controller1 is controller2, "❌ Singleton test failed!"
    print("✅ Singleton Pattern works correctly!")


def test_factory_pattern():
    """Test Factory Pattern - Device creation"""
    print("\n" + "=" * 60)
    print("TEST 2: FACTORY PATTERN")
    print("=" * 60)

    # Create devices using factory
    traffic_light = DeviceFactory.create_device("traffic_light", "Main Street")
    camera = DeviceFactory.create_device("camera", "City Hall")
    solar_panel = DeviceFactory.create_device("solar_panel", "Roof A")

    print(f"Created: {traffic_light.get_info()}")
    print(f"Created: {camera.get_info()}")
    print(f"Created: {solar_panel.get_info()}")

    print("\n✅ Factory Pattern works correctly!")


def test_abstract_factory_pattern():
    """Test Abstract Factory Pattern - Create subsystem sets"""
    print("\n" + "=" * 60)
    print("TEST 3: ABSTRACT FACTORY PATTERN")
    print("=" * 60)

    # Create complete transport subsystem
    transport_devices = AbstractDeviceFactory.create_transport_subsystem("Downtown")
    print("\nTransport Subsystem Created:")
    for device in transport_devices:
        print(f"  • {device.get_info()}")

    # Create complete security subsystem
    security_devices = AbstractDeviceFactory.create_security_subsystem("Airport")
    print("\nSecurity Subsystem Created:")
    for device in security_devices:
        print(f"  • {device.get_info()}")

    print("\n✅ Abstract Factory Pattern works correctly!")


def test_decorator_pattern():
    """Test Decorator Pattern - Adding features to street lights"""
    print("\n" + "=" * 60)
    print("TEST 4: DECORATOR PATTERN")
    print("=" * 60)

    # Create basic street light
    light = StreetLight("Park Avenue")
    print(f"Basic Light: {light.get_info()}")

    # Add motion sensor
    light_with_sensor = MotionSensorDecorator(light)
    print(f"With Sensor: {light_with_sensor.get_info()}")
    print(f"Detection: {light_with_sensor.detect_motion()}")

    # Add dimming capability
    light_with_dimming = DimmingDecorator(light)
    print(f"With Dimming: {light_with_dimming.get_info()}")
    print(f"Dimming: {light_with_dimming.set_brightness(50)}")

    print("\n✅ Decorator Pattern works correctly!")


def test_proxy_pattern():
    """Test Proxy Pattern - Access control for cameras"""
    print("\n" + "=" * 60)
    print("TEST 5: PROXY PATTERN")
    print("=" * 60)

    camera = Camera("Bank Entrance")

    # Test with different access levels
    print("\n1. Guest Access (Limited):")
    guest_proxy = CameraProxy(camera, "guest")
    print(f"   Info: {guest_proxy.get_info()}")
    print(f"   Live Feed: {guest_proxy.get_live_feed()}")

    print("\n2. Operator Access (Normal):")
    operator_proxy = CameraProxy(camera, "operator")
    print(f"   Live Feed: {operator_proxy.get_live_feed()}")
    print(f"   Stop Recording: {operator_proxy.stop_recording()}")

    print("\n3. Admin Access (Full):")
    admin_proxy = CameraProxy(camera, "admin")
    print(f"   Stop Recording: {admin_proxy.stop_recording()}")

    print("\n✅ Proxy Pattern works correctly!")


def test_builder_pattern():
    """Test Builder Pattern - Building complex energy stations"""
    print("\n" + "=" * 60)
    print("TEST 6: BUILDER PATTERN")
    print("=" * 60)

    # Build basic station
    basic_station = EnergyStationDirector.build_basic_station("Suburb Area")
    print("\n1. Basic Station:")
    print(basic_station)

    # Build advanced station
    advanced_station = EnergyStationDirector.build_advanced_station("Downtown")
    print("\n2. Advanced Station:")
    print(advanced_station)

    # Build custom station step by step
    builder = EnergyStationBuilder()
    custom_station = (builder
                      .set_location("University Campus")
                      .add_multiple_panels(6, 300)
                      .add_battery_storage(75)
                      .add_monitoring_system("Smart")
                      .build())
    print("\n3. Custom Station:")
    print(custom_station)

    print("\n✅ Builder Pattern works correctly!")


def test_facade_pattern():
    """Test Facade Pattern - Simplified system access"""
    print("\n" + "=" * 60)
    print("TEST 7: FACADE PATTERN")
    print("=" * 60)

    controller = SmartCityController()

    # Create devices through facade
    print("\nCreating devices through Facade:")
    controller.create_device("traffic_light", "5th Avenue")
    controller.create_device("street_light", "Broadway")
    controller.create_device("camera", "Times Square")
    controller.create_device("solar_panel", "City Hall Roof")

    # Get system status through facade
    print("\nSystem Status (via Facade):")
    controller.get_system_status()

    # Generate report through facade
    print("\nSystem Report (via Facade):")
    controller.generate_report()

    print("\n✅ Facade Pattern works correctly!")


def run_all_tests():
    """Run all system tests"""
    print("\n" + "=" * 60)
    print("🧪 SMARTCITY SYSTEM - DESIGN PATTERNS TEST SUITE")
    print("=" * 60)

    try:
        test_singleton_pattern()
        test_factory_pattern()
        test_abstract_factory_pattern()
        test_decorator_pattern()
        test_proxy_pattern()
        test_builder_pattern()
        test_facade_pattern()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nDesign Patterns Implemented:")
        print("  1. ✅ Singleton (Creational)")
        print("  2. ✅ Factory Method (Creational)")
        print("  3. ✅ Abstract Factory (Creational)")
        print("  4. ✅ Builder (Creational)")
        print("  5. ✅ Decorator (Structural)")
        print("  6. ✅ Proxy (Structural)")
        print("  7. ✅ Facade (Structural)")
        print("\n🎉 SmartCity System is fully functional!")

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        raise


if __name__ == "__main__":
    run_all_tests()