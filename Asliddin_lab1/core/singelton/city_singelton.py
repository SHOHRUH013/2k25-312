class CitySingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.city_name = "SmartCity"
            cls._instance.version = "1.0"
        return cls._instance

    def info(self):
        return f"{self.city_name} Management System v{self.version}"
