class Device:
    def __init__(self, location):
        self.location = location
        self.status = "active"

    def get_info(self):
        return f"{self.__class__.__name__} at {self.location}"


class Camera(Device):
    def __init__(self, location):
        super().__init__(location)
        self.is_recording = True
        self.resolution = "1080p"

    def start_recording(self):
        self.is_recording = True
        return f"Camera at {self.location} started recording"

    def stop_recording(self):
        self.is_recording = False
        return f"Camera at {self.location} stopped recording"

    def get_live_feed(self):
        if self.is_recording:
            return f"📹 Live feed from {self.location} [{self.resolution}]"
        return "Camera not recording"

    def get_info(self):
        status = "Recording" if self.is_recording else "Standby"
        return f"📷 Camera at {self.location} - {status} ({self.resolution})"


class CameraProxy:
    def __init__(self, camera, access_level="guest"):
        self._camera = camera
        self._access_level = access_level
        self._access_log = []

    def _check_permission(self, required_level):
        levels = {"guest": 1, "operator": 2, "admin": 3}
        user_level = levels.get(self._access_level, 0)
        required = levels.get(required_level, 0)
        return user_level >= required

    def _log_access(self, action, granted):
        status = "GRANTED" if granted else "DENIED"
        log_entry = f"{action} - {status} (Level: {self._access_level})"
        self._access_log.append(log_entry)
        return log_entry

    def get_live_feed(self):
        if self._check_permission("operator"):
            self._log_access("Live Feed Access", True)
            return self._camera.get_live_feed()
        else:
            log = self._log_access("Live Feed Access", False)
            return f"❌ Access Denied: {log}"

    def start_recording(self):
        if self._check_permission("operator"):
            self._log_access("Start Recording", True)
            return self._camera.start_recording()
        else:
            log = self._log_access("Start Recording", False)
            return f"❌ Access Denied: {log}"

    def stop_recording(self):
        if self._check_permission("admin"):
            self._log_access("Stop Recording", True)
            return self._camera.stop_recording()
        else:
            log = self._log_access("Stop Recording", False)
            return f"❌ Access Denied: {log}"

    def get_info(self):
        self._log_access("Info Request", True)
        return self._camera.get_info()

    def get_access_log(self):
        if self._check_permission("admin"):
            return self._access_log
        return ["❌ Access Denied: Admin access required"]


# Example usage demonstrating proxy pattern
def demo_proxy():
    camera = Camera("City Hall Entrance")

    # Guest user (limited access)
    guest_proxy = CameraProxy(camera, "guest")
    print("Guest Access:")
    print(guest_proxy.get_info())  # Allowed
    print(guest_proxy.get_live_feed())  # Denied

    print("\n" + "=" * 50 + "\n")

    # Operator user (normal access)
    operator_proxy = CameraProxy(camera, "operator")
    print("Operator Access:")
    print(operator_proxy.get_live_feed())  # Allowed
    print(operator_proxy.stop_recording())  # Denied (needs admin)

    print("\n" + "=" * 50 + "\n")

    # Admin user (full access)
    admin_proxy = CameraProxy(camera, "admin")
    print("Admin Access:")
    print(admin_proxy.stop_recording())  # Allowed
    print("\nAccess Log:")
    for log in admin_proxy.get_access_log():
        print(f"  • {log}")