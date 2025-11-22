"""Builder pattern: пошаговая сборка конфигурации сложного объекта (ModuleConfig)."""

class ModuleConfig:
    def __init__(self):
        self.params = {}

    def __repr__(self):
        return f"ModuleConfig({self.params})"

class ModuleConfigBuilder:
    def __init__(self):
        self._config = ModuleConfig()

    def set_mode(self, mode: str):
        self._config.params['mode'] = mode
        return self

    def set_threshold(self, key: str, value):
        self._config.params[key] = value
        return self

    def build(self):
        return self._config
