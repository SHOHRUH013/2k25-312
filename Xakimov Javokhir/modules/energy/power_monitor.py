class PowerMonitor:
    def __init__(self):
        self.consumption = {}
        self.total_consumption = 0

    def register_consumer(self, consumer_id, base_consumption):
        self.consumption[consumer_id] = {
            "base": base_consumption,
            "current": base_consumption,
            "active": True
        }
        self._update_total()

    def update_consumption(self, consumer_id, consumption):
        if consumer_id in self.consumption:
            self.consumption[consumer_id]["current"] = consumption
            self._update_total()

    def set_active(self, consumer_id, active):
        if consumer_id in self.consumption:
            self.consumption[consumer_id]["active"] = active
            if not active:
                self.consumption[consumer_id]["current"] = 0
            else:
                self.consumption[consumer_id]["current"] = self.consumption[consumer_id]["base"]
            self._update_total()

    def _update_total(self):
        self.total_consumption = sum(
            cons["current"] for cons in self.consumption.values() if cons["active"]
        )

    def get_consumption(self, consumer_id=None):
        if consumer_id:
            return self.consumption.get(consumer_id)
        return self.consumption

    def get_total(self):
        return self.total_consumption

