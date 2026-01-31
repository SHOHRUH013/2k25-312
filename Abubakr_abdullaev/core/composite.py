from abc import ABC, abstractmethod

class LightingComponent(ABC):
    @abstractmethod
    def turn_on(self): pass
    @abstractmethod
    def turn_off(self): pass
    @abstractmethod
    def get_power(self): pass

class Light(LightingComponent):
    def __init__(self, name, power=60):
        self.name = name
        self.power = power
        self.is_on = False
    
    def turn_on(self): self.is_on = True
    def turn_off(self): self.is_on = False
    def get_power(self): return self.power if self.is_on else 0
    def __str__(self): return f"{self.name} ({'ВКЛ' if self.is_on else 'ВЫКЛ'})"

class LightGroup(LightingComponent):
   
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def turn_on(self):
        for child in self.children:
            child.turn_on()
    
    def turn_off(self):
        for child in self.children:
            child.turn_off()
    
    def get_power(self):
        return sum(child.get_power() for child in self.children)
    
    def __str__(self):
        return f"Группа: {self.name} [{len(self.children)} элементов]"