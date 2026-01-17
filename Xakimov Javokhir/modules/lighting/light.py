from abc import ABC, abstractmethod


class Light(ABC):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.brightness = 0

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_brightness(self, level):
        pass

    def get_status(self):
        return {
            "location": self.location,
            "is_on": self.is_on,
            "brightness": self.brightness
        }


class StreetLight(Light):
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        return f"уличный фонарь на {self.location} включен"

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        return f"уличный фонарь на {self.location} выключен"

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            self.is_on = level > 0
            return f"яркость уличного фонаря на {self.location} установлена: {level}%"
        return "неверный уровень яркости (0-100)"


class IndoorLight(Light):
    def turn_on(self):
        self.is_on = True
        self.brightness = 50
        return f"внутреннее освещение на {self.location} включено"

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        return f"внутреннее освещение на {self.location} выключено"

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            self.is_on = level > 0
            return f"яркость внутреннего освещения на {self.location} установлена: {level}%"
        return "неверный уровень яркости (0-100)"


class EmergencyLight(Light):
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        return f"аварийное освещение на {self.location} активировано"

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        return f"аварийное освещение на {self.location} деактивировано"

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            self.is_on = level > 0
            return f"яркость аварийного освещения на {self.location} установлена: {level}%"
        return "неверный уровень яркости (0-100)"

