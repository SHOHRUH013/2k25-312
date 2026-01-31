"""
Singleton Pattern Implementation
Purpose: Ensure only one instance of configuration manager exists throughout the application.
This centralizes configuration management and prevents multiple instances from causing conflicts.
"""
import json
import os


class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize configuration with default values"""
        self.config = {
            'city_name': 'SmartCity',
            'log_level': 'INFO',
            'max_energy_consumption': 10000,
            'emergency_contact': 'city_control@smartcity.com',
            'traffic_threshold': 80,  # percentage
            'lighting_schedule': {
                'on_time': '18:00',
                'off_time': '06:00'
            }
        }
        self.load_config()

    def load_config(self):
        """Load configuration from file if exists"""
        config_file = 'config.json'
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
            except Exception as e:
                print(f"Error loading config: {e}")

    def save_config(self):
        """Save configuration to file"""
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, key):
        """Get configuration value"""
        return self.config.get(key)

    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()

    def display_config(self):
        """Display current configuration"""
        print("\n=== Current Configuration ===")
        for key, value in self.config.items():
            print(f"{key}: {value}")
        print("============================\n")