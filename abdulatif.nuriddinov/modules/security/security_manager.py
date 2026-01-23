"""
Security Management Subsystem
"""
from datetime import datetime
from random import random


class SecurityManager:
    def __init__(self):
        self._cameras = {}
        self._alerts = []
        self._emergency_protocols = {
            'fire': ['Notify fire department', 'Activate sprinklers', 'Evacuate building'],
            'intruder': ['Lockdown affected area', 'Notify police', 'Alert security team'],
            'medical': ['Dispatch ambulance', 'Notify hospital', 'Clear emergency route']
        }

    def monitor_area(self, camera_id):
        """Simulate camera monitoring"""
        status = {
            'camera_id': camera_id,
            'status': 'ACTIVE',
            'last_detection': datetime.now().strftime("%H:%M:%S"),
            'detected_objects': ['person', 'vehicle'] if random() > 0.3 else []

        }
        self._cameras[camera_id] = status

        if len(status['detected_objects']) > 5:
            self._create_alert(camera_id, "High activity detected")

        return status

    def _create_alert(self, location, message):
        alert = {
            'location': location,
            'message': message,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'resolved': False
        }
        self._alerts.append(alert)
        return alert

    def get_security_status(self):
        """Get overall security status"""
        active_cameras = sum(1 for cam in self._cameras.values() if cam['status'] == 'ACTIVE')
        unresolved_alerts = sum(1 for alert in self._alerts if not alert['resolved'])

        return {
            'total_cameras': len(self._cameras),
            'active_cameras': active_cameras,
            'unresolved_alerts': unresolved_alerts,
            'system_status': 'SECURE' if unresolved_alerts == 0 else 'ALERT',
            'last_updated': datetime.now().strftime("%H:%M:%S")
        }

    def activate_emergency_protocol(self, protocol_type):
        """Activate emergency protocol"""
        if protocol_type in self._emergency_protocols:
            actions = self._emergency_protocols[protocol_type]
            print(f"🚨 Emergency protocol '{protocol_type}' activated!")
            for action in actions:
                print(f"  → {action}")
            return True
        return False