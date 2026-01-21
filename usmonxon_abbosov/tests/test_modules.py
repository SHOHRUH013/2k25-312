import pytest
from core.controller import SmartCityController

def test_singleton_controller():
    a = SmartCityController.get_instance()
    b = SmartCityController.get_instance()
    assert a is b

def test_factory_and_modules_exist():
    controller = SmartCityController.get_instance()
    assert "lighting" in controller.modules
    assert "transport" in controller.modules

def test_transport_set_traffic():
    controller = SmartCityController.get_instance()
    transport = controller.modules["transport"]["module"]
    transport.set_traffic("alert")
    assert transport.traffic_light == "alert"
