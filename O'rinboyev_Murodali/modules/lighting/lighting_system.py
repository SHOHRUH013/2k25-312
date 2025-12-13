class Device:
    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        return f"{self.__class__.__name__} at {self.location}"


class StreetLight(Device):
    def __init__(self, location):
        super().__init__(location)
        self.is_on = False
        self.brightness = 100

    def turn_on(self):
        self.is_on = True
        return "Light turned ON"

    def turn_off(self):
        self.is_on = False
        return "Light turned OFF"

    def get_info(self):
        state = "ON" if self.is_on else "OFF"
        return f"💡 Street Light at {self.location} - {state} (Brightness: {self.brightness}%)"


class LightDecorator(Device):
    def __init__(self, light):
        self._light = light
        self.location = light.location

    def turn_on(self):
        return self._light.turn_on()

    def turn_off(self):
        return self._light.turn_off()

    def get_info(self):
        return self._light.get_info()


class MotionSensorDecorator(LightDecorator):
    def __init__(self, light):
        super().__init__(light)
        self.motion_detected = False

    def detect_motion(self):
        self.motion_detected = True
        self._light.turn_on()
        return "Motion detected! Light activated"

    def get_info(self):
        base_info = self._light.get_info()
        return f"{base_info} + Motion Sensor"


class DimmingDecorator(LightDecorator):
    def __init__(self, light):
        super().__init__(light)

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self._light.brightness = level
            return f"Brightness set to {level}%"
        return "Invalid brightness level"

    def get_info(self):
        base_info = self._light.get_info()
        return f"{base_info} + Dimming Control"


class EnergyMonitorDecorator(LightDecorator):
    def __init__(self, light):
        super().__init__(light)
        self.power_consumption = 0.0

    def calculate_consumption(self):
        if self._light.is_on:
            self.power_consumption = (self._light.brightness / 100) * 50  # 50W max
        else:
            self.power_consumption = 0.0
        return self.power_consumption

    def get_info(self):
        base_info = self._light.get_info()
        consumption = self.calculate_consumption()
        return f"{base_info} + Energy Monitor ({consumption:.1f}W)"