from modules.lighting.factory import LightFactory


class LightingSubsystem:
    def __init__(self):
        self.lights = {}

    def add_light(self, light_type, location):
        light = LightFactory.create_light(light_type, location)
        self.lights[location] = light
        return f"светильник добавлен: {light_type} на {location}"

    def remove_light(self, location):
        if location in self.lights:
            del self.lights[location]
            return f"светильник на {location} удален"
        return f"светильник на {location} не найден"

    def turn_on_light(self, location):
        if location in self.lights:
            return self.lights[location].turn_on()
        return f"светильник на {location} не найден"

    def turn_off_light(self, location):
        if location in self.lights:
            return self.lights[location].turn_off()
        return f"светильник на {location} не найден"

    def set_brightness(self, location, level):
        if location in self.lights:
            return self.lights[location].set_brightness(level)
        return f"светильник на {location} не найден"

    def get_status(self, location=None):
        if location:
            if location in self.lights:
                return self.lights[location].get_status()
            return None
        return {loc: light.get_status() for loc, light in self.lights.items()}

    def execute(self, command, *args, **kwargs):
        if command == "add":
            return self.add_light(*args, **kwargs)
        elif command == "remove":
            return self.remove_light(*args, **kwargs)
        elif command == "on":
            return self.turn_on_light(*args, **kwargs)
        elif command == "off":
            return self.turn_off_light(*args, **kwargs)
        elif command == "brightness":
            return self.set_brightness(*args, **kwargs)
        elif command == "status":
            return self.get_status(*args, **kwargs)
        return "неизвестная команда"

