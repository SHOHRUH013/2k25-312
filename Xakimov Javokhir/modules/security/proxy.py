from modules.security.camera import SecurityCamera


class CameraProxy:
    # proxy: контроль доступа к камерам безопасности
    def __init__(self, camera_id, location, access_level="public"):
        self._camera = SecurityCamera(camera_id, location)
        self.access_level = access_level
        self.access_log = []

    def _check_access(self, required_level):
        levels = {"public": 0, "operator": 1, "admin": 2}
        return levels.get(self.access_level, 0) >= levels.get(required_level, 0)

    def _log_access(self, action, success):
        self.access_log.append({
            "action": action,
            "success": success,
            "access_level": self.access_level
        })

    def activate(self, user_level="public"):
        if not self._check_access("operator"):
            self._log_access("activate", False)
            return f"доступ запрещен: требуется уровень operator"
        result = self._camera.activate()
        self._log_access("activate", True)
        return result

    def deactivate(self, user_level="public"):
        if not self._check_access("operator"):
            self._log_access("deactivate", False)
            return f"доступ запрещен: требуется уровень operator"
        result = self._camera.deactivate()
        self._log_access("deactivate", True)
        return result

    def start_recording(self, user_level="public"):
        if not self._check_access("operator"):
            self._log_access("start_recording", False)
            return f"доступ запрещен: требуется уровень operator"
        result = self._camera.start_recording()
        self._log_access("start_recording", True)
        return result

    def stop_recording(self, user_level="public"):
        if not self._check_access("operator"):
            self._log_access("stop_recording", False)
            return f"доступ запрещен: требуется уровень operator"
        result = self._camera.stop_recording()
        self._log_access("stop_recording", True)
        return result

    def get_status(self, user_level="public"):
        if not self._check_access("public"):
            return None
        return self._camera.get_status()

    def get_access_log(self, user_level="public"):
        if not self._check_access("admin"):
            return "доступ запрещен: требуется уровень admin"
        return self.access_log

