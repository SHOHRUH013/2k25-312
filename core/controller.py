class SmartCityController:
    # singleton: единственный экземпляр контроллера
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.subsystems = {}
            self._initialized = True

    def register_subsystem(self, name, subsystem):
        self.subsystems[name] = subsystem

    def get_subsystem(self, name):
        return self.subsystems.get(name)

    def list_subsystems(self):
        return list(self.subsystems.keys())

    def execute_command(self, subsystem_name, command, *args, **kwargs):
        subsystem = self.get_subsystem(subsystem_name)
        if subsystem:
            return subsystem.execute(command, *args, **kwargs)
        return None

    