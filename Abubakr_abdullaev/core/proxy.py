from datetime import datetime

class Camera:
    def __init__(self, id):
        self.id = id
        self.is_recording = False
    
    def start_recording(self):
        print(f"Камера {self.id}: запись начата")
        self.is_recording = True
    
    def stop_recording(self):
        print(f"Камера {self.id}: запись остановлена")
        self.is_recording = False

class SecurityProxy:
    """Proxy pattern: контролирует доступ к камерам по времени"""
    def __init__(self):
        self.cameras = [Camera(i) for i in range(1, 9)]
        self.camera_count = len(self.cameras)
    
    def request_access(self):
        hour = datetime.now().hour
        if 20 <= hour or hour <= 6:
            print("Ночное время — полный доступ к камерам разрешён")
            return True
        else:
            print("Дневное время — доступ к записи ограничен (только просмотр)")
            return False
    
    def access_control_menu(self):
        print("\nСИСТЕМА БЕЗОПАСНОСТИ")
        if self.request_access():
            print("Запуск записи на всех камерах...")
            for cam in self.cameras:
                cam.start_recording()
        else:
            print("Запись запрещена через Proxy. Доступ только на чтение.")