"""Transport subsystem — пример применения Decorator (логирование вызовов) и простого управления."""

def log_decorator(func):
    """Decorator pattern: добавляет логирование к методам подсистемы."""
    def wrapper(*args, **kwargs):
        print(f"[TransportLog] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class TransportSubsystem:
    def __init__(self):
        self.traffic_light = "normal"

    def status(self):
        return f"Traffic lights: {self.traffic_light}"

    def show_menu(self, proxy):
        while True:
            print("\nTransport Menu: 1)set traffic 2)back")
            ch = input(">> ").strip()
            if ch == "1":
                val = input("Enter state (normal/alert): ").strip()
                try:
                    proxy.perform("set_traffic", val)
                except Exception as e:
                    print("Error:", e)
            else:
                break

    @log_decorator
    def set_traffic(self, state):
        self.traffic_light = state
        print("Traffic state set to", state)
