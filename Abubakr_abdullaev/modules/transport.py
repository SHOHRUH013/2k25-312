class TransportSystem:
    """Подсистема управления транспортом"""
    
    def __init__(self):
        self.traffic_lights = 24
        self.current_mode = "Нормальный"
    
    def traffic_lights_count(self):
        return self.traffic_lights
    
    def menu(self):
        while True:
            print("\nУправление транспортом")
            print("1. Нормальный режим")
            print("2. Режим ЧС (все красные)")
            print("3. Зелёная волна (утро)")
            print("0. Назад")
            
            ch = input("→ ").strip()
            if ch == "1":
                self.current_mode = "Нормальный"
            elif ch == "2":
                self.current_mode = "Чрезвычайная ситуация"
                print("Все светофоры на КРАСНЫЙ!")
            elif ch == "3":
                self.current_mode = "Зелёная волна"
                print("Запущена утренняя зелёная волна")
            elif ch == "0":
                break
            print(f"Текущий режим: {self.current_mode}")