"""Facade + Singleton: центральный контроллер системы (Facade предоставляет упрощённый API).
Используем SingletonMeta, чтобы был единственный контроллер в системе.
"""
from core.singleton import SingletonMeta
from core.factories import ModuleFactory
from core.builders import ModuleConfigBuilder
from core.adapters import LoggerAdapter, ExternalLogger
from core.proxy import ModuleProxy

class SmartCityController(metaclass=SingletonMeta):
    def __init__(self):
        self.factory = ModuleFactory()
        self.modules = {}
        self.logger = LoggerAdapter(ExternalLogger())
        # преднастройка: создаём модули и прокси
        for name in ["lighting", "transport", "security", "energy"]:
            module = self.factory.create(name)
            proxy = ModuleProxy(module, user_role="admin")  # в демо admin
            self.modules[name] = {"module": module, "proxy": proxy}
        self.logger.log("SmartCityController initialized", "info")

    @classmethod
    def get_instance(cls):
        return cls()

    def run_module(self, name: str):
        name = name.lower()
        if name not in self.modules:
            print("Module not found.")
            return
        proxy = self.modules[name]["proxy"]
        module = self.modules[name]["module"]
        print(f"--- Вход в подсистему: {name} ---")
        module.show_menu(proxy)
    
    def show_status(self):
        print("=== Status of modules ===")
        for name, entry in self.modules.items():
            module = entry["module"]
            print(f"{name}: {module.status()}")
