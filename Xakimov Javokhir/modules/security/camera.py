class SecurityCamera:
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.is_active = False
        self.recording = False

    def activate(self):
        self.is_active = True
        return f"камера {self.camera_id} на {self.location} активирована"

    def deactivate(self):
        self.is_active = False
        self.recording = False
        return f"камера {self.camera_id} на {self.location} деактивирована"

    def start_recording(self):
        if not self.is_active:
            return f"камера {self.camera_id} не активна"
        self.recording = True
        return f"камера {self.camera_id} начала запись"

    def stop_recording(self):
        self.recording = False
        return f"камера {self.camera_id} остановила запись"

    def get_status(self):
        return {
            "camera_id": self.camera_id,
            "location": self.location,
            "is_active": self.is_active,
            "recording": self.recording
        }

