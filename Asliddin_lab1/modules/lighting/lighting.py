from core.adapters.weather_adaptor import WeatherAdapter


class LightingSystem:
    def __init__(self, weather_adapter=None):
        self._state = "OFF"
        self._cfg = None
        self._weather = weather_adapter or WeatherAdapter()

    def apply_configuration(self, cfg):
        self._cfg = cfg
        print(f"[Lighting] Konfiguratsiya qo'llandi: {cfg}")

    def turn_on(self):
        self._state = "ON"
        print("[Lighting] Barcha ko'cha chiroqlari yoqildi.")

    def status(self):
        weather = self._weather.get_temperature_celsius()
        cfg = repr(self._cfg) if self._cfg else "default"
        return f"state={self._state}, config={cfg}, weather={weather}C"

