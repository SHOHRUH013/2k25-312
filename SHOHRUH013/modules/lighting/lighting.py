
class BasicLightingSystem:
    def __init__(self, num_lights):
        self.num_lights = num_lights
        self._is_on = False

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on
