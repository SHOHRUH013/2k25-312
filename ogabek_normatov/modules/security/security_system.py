"""
Security System - City surveillance and protection

Design Pattern: PROXY
Controls access to security cameras and provides lazy loading.
"""

from abc import ABC, abstractmethod
import time

class SecurityCamera(ABC):
    """
    Pattern: PROXY
    Abstract interface for security cameras.
    """
    
    @abstractmethod
    def get_feed(self):
        pass
    
    @abstractmethod
    def record(self):
        pass

class RealSecurityCamera(SecurityCamera):
    """
    Real security camera that requires resources to initialize.
    This is the 'real subject' in Proxy pattern.
    """
    
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.is_recording = False
        
        # Simulate expensive initialization
        print(f"🎥 Initializing camera {camera_id} at {location}...")
        time.sleep(0.1)  # Simulate loading delay
    
    def get_feed(self):
        return f"[LIVE FEED] Camera {self.camera_id} - {self.location}"
    
    def record(self):
        self.is_recording = True
        return f"📹 Recording from camera {self.camera_id}"

class SecurityCameraProxy(SecurityCamera):
    """
    Pattern: PROXY
    Provides controlled access to security cameras.
    Implements lazy initialization and access control.
    """
    
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self._real_camera = None
        self.access_log = []
    
    def _get_real_camera(self):
        """Lazy initialization of the real camera."""
        if self._real_camera is None:
            self._real_camera = RealSecurityCamera(self.camera_id, self.location)
        return self._real_camera
    
    def get_feed(self):
        """Get camera feed with access logging."""
        self._log_access("feed_requested")
        
        # Check access permissions (simplified)
        if self._check_permissions():
            camera = self._get_real_camera()
            return camera.get_feed()
        else:
            return f"❌ Access denied to camera {self.camera_id}"
    
    def record(self):
        """Start recording with access logging."""
        self._log_access("recording_started")
        camera = self._get_real_camera()
        return camera.record()
    
    def _check_permissions(self):
        """Simulate permission check."""
        return True  # Simplified - always allow
    
    def _log_access(self, action):
        """Log access attempts."""
        timestamp = time.strftime("%H:%M:%S")
        self.access_log.append(f"{timestamp} - {action}")

class SecuritySystem:
    """Main security system managing cameras and alarms."""
    
    def __init__(self):
        # Use Proxy pattern for cameras - they won't be initialized until accessed
        self.cameras = [
            SecurityCameraProxy("CAM-001", "Main Square"),
            SecurityCameraProxy("CAM-002", "Park Entrance"),
            SecurityCameraProxy("CAM-003", "Shopping District"),
            SecurityCameraProxy("CAM-004", "Residential North"),
            SecurityCameraProxy("CAM-005", "Industrial Gate")
        ]
        
        self.alarms_active = []
        self.security_level = "Normal"
    
    def perform_check(self):
        """Perform security system check."""
        print("\n🔒 SECURITY SYSTEM CHECK")
        print(f"Security Level: {self.security_level}")
        print(f"Total Cameras: {len(self.cameras)}")
        print(f"Active Alarms: {len(self.alarms_active)}")
        
        if self.alarms_active:
            print("\n⚠️  ACTIVE ALARMS:")
            for alarm in self.alarms_active:
                print(f"  • {alarm}")
        else:
            print("✅ No active alarms")
    
    def view_cameras(self):
        """
        View camera feeds.
        Cameras are only initialized when accessed (Proxy pattern in action).
        """
        print("\n📹 CAMERA FEEDS:")
        print("-" * 40)
        
        # Access only first 3 cameras to demonstrate lazy loading
        for camera in self.cameras[:3]:
            print(camera.get_feed())
        
        print("\n💡 Note: Other cameras remain in standby (not initialized)")
    
    def trigger_alarm(self, location):
        """Trigger security alarm at specific location."""
        alarm = f"🚨 ALARM at {location} - {time.strftime('%H:%M:%S')}"
        self.alarms_active.append(alarm)
        self.security_level = "Alert"
        
        print(f"\n{alarm}")
        print("📹 Starting recording on nearby cameras...")
        
        # Start recording on relevant cameras
        for camera in self.cameras:
            if location.lower() in camera.location.lower():
                print(camera.record())
    
    def emergency_mode(self):
        """Activate emergency security protocols."""
        self.security_level = "Emergency"
        print("🚨 Emergency security mode: All cameras active, alarms armed")
        
        # Initialize all cameras in emergency
        for camera in self.cameras:
            camera.record()
    
    def get_status(self):
        """Get security system status."""
        return f"Level: {self.security_level}, Alarms: {len(self.alarms_active)}"
    
    def generate_report(self):
        """Generate security report."""
        print("\n🔒 SECURITY SYSTEM REPORT")
        print("-" * 40)
        print(f"Security Level: {self.security_level}")
        print(f"Cameras Deployed: {len(self.cameras)}")
        print(f"Active Alarms: {len(self.alarms_active)}")
        
        # Show which cameras have been initialized (Proxy pattern benefit)
        initialized = sum(1 for cam in self.cameras if cam._real_camera is not None)
        print(f"Cameras Currently Active: {initialized}/{len(self.cameras)}")
        print("(Others remain in standby - Proxy pattern optimization)")
    
    def shutdown(self):
        """Shutdown security system."""
        self.alarms_active.clear()
        self.security_level = "Offline"
        print("🔒 Security system shutdown")