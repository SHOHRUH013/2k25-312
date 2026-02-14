
class SmartCityController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, factory, config):
        self.factory = factory
        self.config = config
        self.lighting = factory.create_lighting(config.num_lights)

    def lighting_on(self):
        self.lighting.turn_on()

    def lighting_off(self):
        self.lighting.turn_off()

    def get_status(self):
        return f"Lighting: {'ON' if self.lighting.is_on else 'OFF'}"
