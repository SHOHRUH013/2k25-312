class Device:
    def __init__(self, id_):
        self.id = id_

class Camera(Device):
    def __init__(self, id_, resolution="720p"):
        super().__init__(id_)
        self.type = "Camera"
        self.resolution = resolution

class MotionSensor(Device):
    def __init__(self, id_, sensitivity=5):
        super().__init__(id_)
        self.type = "MotionSensor"
        self.sensitivity = sensitivity

class LightPole(Device):
    def __init__(self, id_, watt=60):
        super().__init__(id_)
        self.type = "LightPole"
        self.watt = watt

class DeviceFactory:
    def create_device(self, device_type: str, **kwargs):
        if device_type == "camera":
            return Camera(**kwargs)
        if device_type == "motion":
            return MotionSensor(**kwargs)
        if device_type == "lightpole":
            return LightPole(**kwargs)
        raise ValueError(f"Unknown device_type: {device_type}")
