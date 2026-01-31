"""
Builder Pattern Implementation
Purpose: Separate the construction of complex alert objects from their representation.
This allows step-by-step construction and different representations of alerts.
"""
from datetime import datetime
from abc import ABC, abstractmethod


class Alert:
    def __init__(self):
        self.type = None
        self.severity = None
        self.message = None
        self.location = None
        self.timestamp = None
        self.department = None
        self.action_required = None

    def __str__(self):
        return (f"Alert [{self.timestamp}]:\n"
                f"  Type: {self.type}\n"
                f"  Severity: {self.severity}\n"
                f"  Location: {self.location}\n"
                f"  Message: {self.message}\n"
                f"  Department: {self.department}\n"
                f"  Action Required: {self.action_required}")


# Builder Interface
class AlertBuilder(ABC):
    @abstractmethod
    def set_type(self, alert_type):
        pass

    @abstractmethod
    def set_severity(self, severity):
        pass

    @abstractmethod
    def set_message(self, message):
        pass

    @abstractmethod
    def set_location(self, location):
        pass

    @abstractmethod
    def set_department(self, department):
        pass

    @abstractmethod
    def set_action_required(self, action):
        pass

    @abstractmethod
    def build(self):
        pass


# Concrete Builder
class CityAlertBuilder(AlertBuilder):
    def __init__(self):
        self.alert = Alert()

    def set_type(self, alert_type):
        self.alert.type = alert_type
        return self

    def set_severity(self, severity):
        self.alert.severity = severity
        return self

    def set_message(self, message):
        self.alert.message = message
        return self

    def set_location(self, location):
        self.alert.location = location
        return self

    def set_department(self, department):
        self.alert.department = department
        return self

    def set_action_required(self, action):
        self.alert.action_required = action
        return self

    def build(self):
        self.alert.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.alert


# Director
class AlertDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_traffic_alert(self, location, severity="Medium"):
        return (self.builder
                .set_type("Traffic")
                .set_severity(severity)
                .set_location(location)
                .set_message(f"Heavy traffic detected at {location}")
                .set_department("Transport Department")
                .set_action_required("Adjust traffic signals and notify public transport")
                .build())

    def construct_security_alert(self, location, severity="High"):
        return (self.builder
                .set_type("Security")
                .set_severity(severity)
                .set_location(location)
                .set_message(f"Security breach detected at {location}")
                .set_department("Security Department")
                .set_action_required("Dispatch security team and notify police")
                .build())

    def construct_energy_alert(self, location, severity="Low"):
        return (self.builder
                .set_type("Energy")
                .set_severity(severity)
                .set_location(location)
                .set_message(f"Abnormal energy consumption at {location}")
                .set_department("Energy Department")
                .set_action_required("Check equipment and optimize consumption")
                .build())