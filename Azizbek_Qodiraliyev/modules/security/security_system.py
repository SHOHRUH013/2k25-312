"""
Security System Module
Manages city surveillance and security infrastructure
"""
import random


class SecuritySystem:
    def __init__(self):
        self.cameras_operational = 150
        self.total_cameras = 150
        self.alert_level = "normal"
        self.incidents_today = random.randint(0, 5)

    def monitor_cameras(self):
        """Monitor all security cameras"""
        if self.cameras_operational < self.total_cameras * 0.9:
            return f"⚠️ Warning: {self.total_cameras - self.cameras_operational} cameras offline"
        else:
            return "✅ All cameras monitoring normally"

    def emergency_alert(self):
        """Activate emergency security alert"""
        self.alert_level = "emergency"
        return "🚨 SECURITY EMERGENCY: All units alerted, enhanced surveillance activated"

    def get_status(self):
        """Get security system status"""
        camera_health = (self.cameras_operational / self.total_cameras) * 100
        return (f"Security: {self.alert_level.upper()} - "
                f"Cameras: {camera_health:.1f}% - "
                f"Incidents: {self.incidents_today}")