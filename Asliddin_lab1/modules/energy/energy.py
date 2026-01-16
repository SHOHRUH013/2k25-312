class EnergySystem:
    def __init__(self):
        self.mode = "normal"

    def enable_saving(self):
        self.mode = "saving"
        print("[Energy] Tejamkor rejim yoqildi.")

    def optimize(self):
        self.enable_saving()
        print("[Energy] Energiya optimallashtirildi.")

    def status(self):
        return f"mode={self.mode}"

