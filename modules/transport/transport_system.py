"""
Transportation System Module
Manages traffic lights, public transport, and traffic flow
"""


class Device:
    """Base class for all smart city devices"""

    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        """Return device information"""
        return f"{self.__class__.__name__} at {self.location} ({self.status})"


class TrafficLight(Device):
    """
    Traffic Light Device
    Controls intersection traffic flow
    """

    def __init__(self, location):
        super().__init__(location)
        self.current_state = "red"
        self.cycle_time = 60

    def change_state(self, new_state):
        """Change traffic light state"""
        valid_states = ['red', 'yellow', 'green']
        if new_state in valid_states:
            self.current_state = new_state
            return True
        return False

    def get_info(self):
        """Return traffic light status"""
        return f"🚦 Traffic Light at {self.location} - State: {self.current_state}"


class PublicTransport(Device):
    """
    Public Transport Vehicle
    Represents buses, trams, etc.
    """

    def __init__(self, route):
        super().__init__(route)
        self.route = route
        self.capacity = 50
        self.current_passengers = 0

    def get_info(self):
        """Return transport status"""
        return f"🚌 Public Transport on {self.route} - Passengers: {self.current_passengers}/{self.capacity}"