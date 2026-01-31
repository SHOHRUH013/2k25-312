"""
Factory Method Pattern: Creates different types of sensors
without specifying the exact class to create
"""
from abc import ABC, abstractmethod


class Sensor(ABC):
    """Product interface"""

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class TrafficSensor(Sensor):
    """Concrete Product: Traffic Sensor"""

    def read_data(self):
        return "Reading vehicle count and speed data"

    def get_type(self):
        return "Traffic Sensor"


class LightingSensor(Sensor):
    """Concrete Product: Lighting Sensor"""

    def read_data(self):
        return "Reading ambient light levels"

    def get_type(self):
        return "Lighting Sensor"


class SecuritySensor(Sensor):
    """Concrete Product: Security Sensor"""

    def read_data(self):
        return "Reading motion and surveillance data"

    def get_type(self):
        return "Security Sensor"


class EnergySensor(Sensor):
    """Concrete Product: Energy Sensor"""

    def read_data(self):
        return "Reading power consumption data"

    def get_type(self):
        return "Energy Sensor"


class SensorFactory(ABC):
    """Creator abstract class"""

    @abstractmethod
    def create_sensor(self) -> Sensor:
        pass

    def deploy_sensor(self):
        """Template method for sensor deployment"""
        sensor = self.create_sensor()
        return f"Deploying {sensor.get_type()}: {sensor.read_data()}"


class TrafficSensorFactory(SensorFactory):
    """Concrete Creator: Traffic Sensor Factory"""

    def create_sensor(self) -> Sensor:
        return TrafficSensor()


class LightingSensorFactory(SensorFactory):
    """Concrete Creator: Lighting Sensor Factory"""

    def create_sensor(self) -> Sensor:
        return LightingSensor()


class SecuritySensorFactory(SensorFactory):
    """Concrete Creator: Security Sensor Factory"""

    def create_sensor(self) -> Sensor:
        return SecuritySensor()


class EnergySensorFactory(SensorFactory):
    """Concrete Creator: Energy Sensor Factory"""

    def create_sensor(self) -> Sensor:
        return EnergySensor()


# Sensor Manager using Factory Method
class SensorManager:
    def __init__(self):
        self.factories = {
            'traffic': TrafficSensorFactory(),
            'lighting': LightingSensorFactory(),
            'security': SecuritySensorFactory(),
            'energy': EnergySensorFactory()
        }

    def deploy_sensor_network(self):
        """Deploy complete sensor network using factory method"""
        deployments = []
        for sensor_type, factory in self.factories.items():
            deployments.append(factory.deploy_sensor())
        return deployments