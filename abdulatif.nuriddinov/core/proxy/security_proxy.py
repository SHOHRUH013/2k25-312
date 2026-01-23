from datetime import datetime

class SecurityProxy:
    def __init__(self, security_system):
        self._security_system = security_system

    def _log_access(self, user, action):
        log_entry = f"{datetime.now()}: User '{user}' performed '{action}'"
        print(f"[SECURITY LOG] {log_entry}")

    def get_security_status(self, user):
        self._log_access(user, "get_security_status")
        return self._security_system.get_security_status()

    def monitor_area(self, user, camera_id):
        self._log_access(user, f"monitor_area({camera_id})")
        return self._security_system.monitor_area(camera_id)
