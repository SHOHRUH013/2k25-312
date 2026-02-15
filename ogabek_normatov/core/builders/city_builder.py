class CityBuilder:
    """
    Builder pattern
    Purpose: step-by-step construction of SmartCity system
    """
    def __init__(self):
        self.city = []

    def add_subsystem(self, subsystem):
        self.city.append(subsystem)
        return self

    def build(self):
        return self.city
