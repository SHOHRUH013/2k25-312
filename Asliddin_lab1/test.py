import unittest
from core.singelton.city_singelton import CitySingleton
from core.builders.lighting_builder import LightingBuilder
from core.builders.transport_builder import TransportRouteBuilder
from core.factories.device_factory import DeviceFactory
from core.adapters.weather_adaptor import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy
from modules.security.security import RealSecuritySystem

class TestSmartCity(unittest.TestCase):

    def test_singleton(self):
        a = CitySingleton()
        b = CitySingleton()
        self.assertIs(a, b)
        self.assertIn("SmartCity", a.info())

    def test_lighting_builder(self):
        lb = LightingBuilder()
        cfg = lb.set_brightness(80).set_mode("eco").set_auto_off(5).build()
        self.assertEqual(cfg.brightness, 80)
        self.assertEqual(cfg.mode, "eco")

    def test_transport_builder(self):
        tb = TransportRouteBuilder()
        route = tb.set_number(3).add_stop("A").add_stop("B").set_speed_limit(50).build()
        self.assertEqual(route.number, 3)
        self.assertIn("A", route.stops)

    def test_device_factory(self):
        f = DeviceFactory()
        cam = f.create_device("camera", id_=1, resolution="1080p")
        self.assertEqual(cam.type, "Camera")
        with self.assertRaises(ValueError):
            f.create_device("unknown")

    def test_weather_adapter(self):
        wa = WeatherAdapter()
        t = wa.get_temperature_celsius()
        self.assertIsInstance(t, int)

    def test_security_proxy(self):
        real = RealSecuritySystem()
        proxy = SecurityProxy(real_security=real, auth_checker=lambda u: u.get("role")=="admin")
        admin = {"role":"admin"}
        user = {"role":"user"}
        self.assertIn("Cam", proxy.view_cameras(admin))
        with self.assertRaises(PermissionError):
            proxy.view_cameras(user)

if __name__ == "__main__":
    unittest.main()
