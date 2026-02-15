class TransportSystem:
    def __init__(self, transport_type="bus"):
        self.type = transport_type
        self._route = None
        self._optimized = False

    def set_route(self, route):
        self._route = route
        print(f"[Transport] Yangi marshrut o'rnatildi: {route}")

    def optimize(self):
        self._optimized = True
        print("[Transport] Marshrutlar optimallashtirildi.")

    def start(self):
        print(f"[Transport] {self.type.capitalize()}lar harakatga tushdi.")

    def status(self):
        route = repr(self._route) if self._route else "no route"
        return f"type={self.type}, route={route}, optimized={self._optimized}"
