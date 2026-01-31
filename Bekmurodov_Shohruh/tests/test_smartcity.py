import pytest
from unittest.mock import MagicMock

from Bekmurodov_Shohruh.core.controller import SmartCityController
from Bekmurodov_Shohruh.core.builders.lighting_builder import LightingSceneBuilder
from Bekmurodov_Shohruh.core.factories.transport_factory import BusFactory, TramFactory
from Bekmurodov_Shohruh.core.proxy.security_proxy import SecuritySystemProxy
from Bekmurodov_Shohruh.core.adapters.weather_adapter import ExternalWeatherAPI, WeatherServiceAdapter

from Bekmurodov_Shohruh.modules.transport import Vehicle
from Bekmurodov_Shohruh.modules.security import SecuritySystem
from Bekmurodov_Shohruh.modules.energy import EnergySystem
from Bekmurodov_Shohruh.modules.lighting import LightingSystem


def test_singleton_controller():
    c1 = SmartCityController()
    c2 = SmartCityController()
    assert c1 is c2, "SmartCityController must implement the Singleton pattern."


def test_lighting_scene_builder():
    builder = LightingSceneBuilder()

    scene = (
        builder
        .set_area("Central Park")
        .set_brightness(85)
        .set_schedule("18:00-05:00")
        .build()
    )

    assert scene.area == "Central Park"
    assert scene.brightness == 85
    assert scene.schedule == "18:00-05:00"


def test_bus_factory_creates_bus():
    factory = BusFactory()
    bus = factory.create_vehicle("A-B")

    assert isinstance(bus, Vehicle)
    assert bus.name == "Bus"
    assert bus.route == "A-B"


def test_tram_factory_creates_tram():
    factory = TramFactory()
    tram = factory.create_vehicle("C-D")

    assert isinstance(tram, Vehicle)
    assert tram.name == "Tram"
    assert tram.route == "C-D"


def test_security_proxy_requires_authorization():
    real = SecuritySystem()
    proxy = SecuritySystemProxy(real)

    # Should fail without authorization
    with pytest.raises(PermissionError):
        proxy.arm()


def test_security_proxy_authorized_actions():
    real = SecuritySystem()
    proxy = SecuritySystemProxy(real)

    proxy.authorize("ADMIN")  # valid token

    proxy.arm()
    assert real._armed is True

    proxy.disarm()
    assert real._armed is False


def test_weather_adapter_normalizes_data(monkeypatch):
    api = ExternalWeatherAPI()

    monkeypatch.setattr(
        api,
        "fetch_data",
        lambda city: {"city": city, "temperature_c": 27, "period": "day"},
    )

    adapter = WeatherServiceAdapter(api)

    temp, is_day = adapter.get_city_weather("Tashkent")

    assert temp == 27
    assert is_day is True


def test_controller_configures_lighting(monkeypatch):
    controller = SmartCityController()
    controller.lighting = MagicMock(spec=LightingSystem)
    controller.energy = MagicMock(spec=EnergySystem)

    controller.configure_lighting("Center", 70, "19:00-06:00")

    controller.lighting.apply_scene.assert_called_once()
    controller.energy.register_lighting.assert_called_once()


def test_controller_dispatches_transport(monkeypatch):
    controller = SmartCityController()
    controller.transport = MagicMock()
    controller.energy = MagicMock()

    controller.send_transport("A-B", "bus")

    controller.transport.dispatch.assert_called_once()
    controller.energy.register_transport.assert_called_once()


def test_eco_mode_reduces_brightness(monkeypatch):
    controller = SmartCityController()

    controller.lighting = MagicMock()
    mock_adapter = MagicMock()
    mock_adapter.get_city_weather.return_value = (30, True)
    controller.weather_service = mock_adapter

    controller.eco_mode()

    controller.lighting.dim_global.assert_called_with(40)


def test_eco_mode_no_change_when_cold(monkeypatch):
    controller = SmartCityController()
    controller.lighting = MagicMock()

    mock_adapter = MagicMock()
    mock_adapter.get_city_weather.return_value = (10, True)
    controller.weather_service = mock_adapter

    controller.eco_mode()

    controller.lighting.dim_global.assert_not_called()
