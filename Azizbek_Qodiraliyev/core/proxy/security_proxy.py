"""
Proxy Pattern: Controls access to security system
Adds authentication and logging for security operations
"""
from abc import ABC, abstractmethod


class SecuritySystemInterface(ABC):
    """Subject interface"""

    @abstractmethod
    def monitor_cameras(self):
        pass

    @abstractmethod
    def emergency_alert(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class RealSecuritySystem(SecuritySystemInterface):
    """Real subject - the actual security system"""

    def monitor_cameras(self):
        return "Monitoring all security cameras in real-time"

    def emergency_alert(self):
        return "🚨 EMERGENCY ALERT ACTIVATED - All units notified"

    def get_status(self):
        return "Security System: ACTIVE - All cameras operational"


class SecurityProxy(SecuritySystemInterface):
    """Proxy that controls access to the real security system"""

    def __init__(self, real_security_system: SecuritySystemInterface):
        self._real_system = real_security_system
        self._access_levels = {
            'admin': ['monitor', 'alert', 'status'],
            'operator': ['status', 'monitor'],
            'viewer': ['status']
        }
        self._current_user = None
        self._access_log = []

    def authenticate(self, username, password):
        """Authenticate user (simplified for demo)"""
        users = {
            'admin': 'admin123',
            'operator': 'op123',
            'viewer': 'view123'
        }

        if username in users and users[username] == password:
            self._current_user = username
            self._log_access(f"User {username} authenticated")
            return True
        return False

    def _check_permission(self, operation):
        """Check if current user has permission for operation"""
        if not self._current_user:
            raise PermissionError("User not authenticated")

        if operation in self._access_levels[self._current_user]:
            return True

        raise PermissionError(
            f"User {self._current_user} not authorized for {operation}"
        )

    def _log_access(self, message):
        """Log security system access"""
        self._access_log.append(message)
        print(f"🔒 SECURITY LOG: {message}")

    def monitor_cameras(self):
        """Proxy method with access control"""
        self._check_permission('monitor')
        self._log_access(f"User {self._current_user} accessed camera monitoring")
        return self._real_system.monitor_cameras()

    def emergency_alert(self):
        """Proxy method with access control"""
        self._check_permission('alert')
        self._log_access(f"User {self._current_user} activated emergency alert")
        return self._real_system.emergency_alert()

    def get_status(self):
        """Proxy method with access control"""
        self._check_permission('status')
        return self._real_system.get_status()

    def get_access_log(self):
        """Get security access log (admin only)"""
        if self._current_user != 'admin':
            raise PermissionError("Admin access required for logs")
        return self._access_log

    def logout(self):
        """Logout current user"""
        if self._current_user:
            self._log_access(f"User {self._current_user} logged out")
            self._current_user = None