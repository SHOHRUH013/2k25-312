"""Lighting subsystem — использует Prototype (клонирование сценариев) и простую бизнес-логику."""

import copy

class LightingScenario:
    """Prototype: шаблон сценария освещения, который можно клонировать."""
    def __init__(self, name, brightness=100, auto=False):
        self.name = name
        self.brightness = brightness
        self.auto = auto

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"<Scenario {self.name} brightness={self.brightness} auto={self.auto}>"

class LightingSubsystem:
    def __init__(self):
        self.scenarios = {
            "day": LightingScenario("day", brightness=100, auto=True),
            "night": LightingScenario("night", brightness=30, auto=True)
        }
        self.current = self.scenarios["day"]

    def status(self):
        return f"Lighting active scenario: {self.current}"

    def show_menu(self, proxy):
        while True:
            print("\nLighting Menu: 1)set scenario 2)clone scenario 3)back")
            ch = input(">> ").strip()
            if ch == "1":
                name = input("scenario name: ").strip()
                if name in self.scenarios:
                    try:
                        proxy.perform("configure", name)
                    except Exception as e:
                        print("Error:", e)
                else:
                    print("No such scenario.")
            elif ch == "2":
                base = input("Base scenario to clone: ").strip()
                if base in self.scenarios:
                    new = self.scenarios[base].clone()
                    new.name = input("New scenario name: ").strip()
                    self.scenarios[new.name] = new
                    print("Cloned:", new)
                else:
                    print("No such base scenario.")
            else:
                break

    def configure(self, name):
        if name in self.scenarios:
            self.current = self.scenarios[name]
            print("Scenario set to", self.current)
        else:
            print("Scenario not found.")
