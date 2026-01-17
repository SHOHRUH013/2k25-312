class RealSecuritySystem:
    def __init__(self):
        self.cameras = ["Cam-1", "Cam-2", "Cam-3"]
        self.armed = False

    def view_cameras(self):
        return f"Cameras: {', '.join(self.cameras)}"

    def activate(self):
        self.armed = True
        print("[Security] Tizim faol holatga keltirildi.")
        return "activated"

    def status(self):
        return f"armed={self.armed}, cameras={len(self.cameras)}"
