class SmartLight:
    def __init__(self):
        self.brightness = 0
        self.color_temp = "neutral"
        self.motion_sensor = False
        self.auto_mode = True
        self.name = "Unknown Light"
    
    def __str__(self):
        return f"{self.name} [{self.brightness}% | {self.color_temp} | {'Датчик' if self.motion_sensor else 'Нет датчика'}]"

class SmartLightBuilder:
    
    def __init__(self):
        self.light = SmartLight()
    
    def set_name(self, name):
        self.light.name = name
        return self
    
    def set_brightness(self, value):
        self.light.brightness = value
        return self
    
    def set_color_temperature(self, temp):
        self.light.color_temp = temp
        return self
    
    def with_motion_sensor(self):
        self.light.motion_sensor = True
        return self
    
    def enable_auto_mode(self):
        self.light.auto_mode = True
        return self
    
    def build(self):
        return self.light