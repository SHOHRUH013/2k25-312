class Device:
    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        return f"{self.__class__.__name__} at {self.location} ({self.status})"


class TrafficLight(Device):
    def __init__(self, location):
        super().__init__(location)
        self.current_state = "red"
        self.cycle_time = 60

    def change_state(self, new_state):
        valid_states = ['red', 'yellow', 'green']
        if new_state in valid_states:
            self.current_state = new_state
            return True
        return False

    def get_info(self):
        return f"🚦 Traffic Light at {self.location} - State: {self.current_state}"


class PublicTransport(Device):
    def __init__(self, route):
        super().__init__(route)
        self.route = route
        self.capacity = 50
        self.current_passengers = 0

    def get_info(self):
        return f"🚌 Public Transport on {self.route} - Passengers: {self.current_passengers}/{self.capacity}"