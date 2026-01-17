from modules.security.proxy import CameraProxy


class SecuritySubsystem:
    def __init__(self):
        self.cameras = {}
        self.next_id = 1

    def add_camera(self, location, access_level="public"):
        camera_id = f"CAM{self.next_id}"
        proxy = CameraProxy(camera_id, location, access_level)
        self.cameras[camera_id] = proxy
        self.next_id += 1
        return f"камера {camera_id} добавлена на {location}"

    def remove_camera(self, camera_id):
        if camera_id in self.cameras:
            del self.cameras[camera_id]
            return f"камера {camera_id} удалена"
        return f"камера {camera_id} не найдена"

    def activate_camera(self, camera_id, user_level="public"):
        if camera_id in self.cameras:
            return self.cameras[camera_id].activate(user_level)
        return f"камера {camera_id} не найдена"

    def deactivate_camera(self, camera_id, user_level="public"):
        if camera_id in self.cameras:
            return self.cameras[camera_id].deactivate(user_level)
        return f"камера {camera_id} не найдена"

    def start_recording(self, camera_id, user_level="public"):
        if camera_id in self.cameras:
            return self.cameras[camera_id].start_recording(user_level)
        return f"камера {camera_id} не найдена"

    def stop_recording(self, camera_id, user_level="public"):
        if camera_id in self.cameras:
            return self.cameras[camera_id].stop_recording(user_level)
        return f"камера {camera_id} не найдена"

    def get_status(self, camera_id=None, user_level="public"):
        if camera_id:
            if camera_id in self.cameras:
                return self.cameras[camera_id].get_status(user_level)
            return None
        result = {}
        for cam_id, proxy in self.cameras.items():
            status = proxy.get_status(user_level)
            if status:
                result[cam_id] = status
        return result

    def get_access_log(self, camera_id, user_level="admin"):
        if camera_id in self.cameras:
            return self.cameras[camera_id].get_access_log(user_level)
        return f"камера {camera_id} не найдена"

    def execute(self, command, *args, **kwargs):
        if command == "add":
            return self.add_camera(*args, **kwargs)
        elif command == "remove":
            return self.remove_camera(*args, **kwargs)
        elif command == "activate":
            return self.activate_camera(*args, **kwargs)
        elif command == "deactivate":
            return self.deactivate_camera(*args, **kwargs)
        elif command == "start_recording":
            return self.start_recording(*args, **kwargs)
        elif command == "stop_recording":
            return self.stop_recording(*args, **kwargs)
        elif command == "status":
            return self.get_status(*args, **kwargs)
        elif command == "log":
            return self.get_access_log(*args, **kwargs)
        return "неизвестная команда"

