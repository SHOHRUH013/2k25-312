"""
Singleton Pattern: Configuration Manager
Ensures only one configuration instance exists throughout the application
"""
import json
import os


class ConfigManager:
    _instance = None
    _config_file = "city_config.json"

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.config_data = self._load_config()
            ConfigManager._instance = self

    @classmethod
    def get_instance(cls):
        """Singleton: Get the single instance of ConfigManager"""
        if cls._instance is None:
            cls._instance = ConfigManager()
        return cls._instance

    def _load_config(self):
        """Load configuration from file or create default"""
        default_config = {
            "city_name": "SmartCity",
            "max_energy_consumption": 10000,
            "emergency_contact": "911",
            "traffic_optimization_interval": 30,
            "lighting_schedule": "18:00-06:00",
            "security_level": "high"
        }

        if os.path.exists(self._config_file):
            try:
                with open(self._config_file, 'r') as f:
                    return json.load(f)
            except:
                return default_config
        return default_config

    def get(self, key):
        """Get configuration value"""
        return self.config_data.get(key)

    def set(self, key, value):
        """Set configuration value"""
        self.config_data[key] = value
        self._save_config()

    def _save_config(self):
        """Save configuration to file"""
        with open(self._config_file, 'w') as f:
            json.dump(self.config_data, f, indent=2)

    def get_all_config(self):
        """Get all configuration data"""
        return self.config_data.copy()