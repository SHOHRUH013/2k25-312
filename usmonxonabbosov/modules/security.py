"""Security subsystem — простая логика оповещений и мониторинга."""

class SecuritySubsystem:
    def __init__(self):
        self.alarm = False
        self.last_event = None

    def status(self):
        return f"Alarm={'ON' if self.alarm else 'OFF'} last_event={self.last_event}"

    def show_menu(self, proxy):
        while True:
            print("\nSecurity Menu: 1)toggle alarm 2)simulate event 3)back")
            ch = input(">> ").strip()
            if ch == "1":
                try:
                    proxy.perform("toggle_alarm")
                except Exception as e:
                    print("Error:", e)
            elif ch == "2":
                event = input("Event description: ").strip()
                self.simulate_event(event)
            else:
                break

    def toggle_alarm(self):
        self.alarm = not self.alarm
        print("Alarm toggled:", self.alarm)

    def simulate_event(self, description):
        self.last_event = description
        print("Event recorded:", description)
