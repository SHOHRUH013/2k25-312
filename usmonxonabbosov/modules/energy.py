"""Energy subsystem — минимальный мониторинг; можно расширять с Flyweight для сенсоров."""

class EnergySubsystem:
    def __init__(self):
        self.consumption = 1200  # kWh
        self.saving_mode = False

    def status(self):
        return f"Consumption={self.consumption}kWh saving_mode={self.saving_mode}"

    def show_menu(self, proxy):
        while True:
            print("\nEnergy Menu: 1)toggle saving 2)set consumption 3)back")
            ch = input(">> ").strip()
            if ch == "1":
                try:
                    proxy.perform("toggle_saving")
                except Exception as e:
                    print("Error:", e)
            elif ch == "2":
                val = input("New consumption (int): ").strip()
                try:
                    proxy.perform("set_consumption", int(val))
                except Exception as e:
                    print("Error:", e)
            else:
                break

    def toggle_saving(self):
        self.saving_mode = not self.saving_mode
        print("Saving mode:", self.saving_mode)

    def set_consumption(self, val: int):
        self.consumption = val
        print("Consumption set to", self.consumption)
