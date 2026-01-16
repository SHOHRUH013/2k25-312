class LightingConfiguration:
    def __init__(self):
        self.brightness = 100
        self.mode = "normal"
        self.auto_off_minutes = 0

    def __repr__(self):
        return (f"LightingConfiguration(brightness={self.brightness}, "
                f"mode='{self.mode}', auto_off_minutes={self.auto_off_minutes})")

class LightingBuilder:
    def __init__(self):
        self._cfg = LightingConfiguration()

    def set_brightness(self, percent: int):
        self._cfg.brightness = max(0, min(100, percent))
        return self

    def set_mode(self, mode: str):
        self._cfg.mode = mode
        return self

    def set_auto_off(self, minutes: int):
        self._cfg.auto_off_minutes = max(0, minutes)
        return self

    def build(self) -> LightingConfiguration:
        return self._cfg

