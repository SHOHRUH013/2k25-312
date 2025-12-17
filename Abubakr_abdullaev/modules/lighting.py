from core.composite import Light, LightGroup
from core.builders import SmartLightBuilder

class LightingSystem:
    """Подсистема освещения с использованием Composite и Builder"""
    
    def __init__(self):
        self.main_street = LightGroup("Главная улица")
        self.park = LightGroup("Центральный парк")
        
        # Создаём фонари через Builder
        light1 = SmartLightBuilder() \
            .set_name("Фонарь №1") \
            .set_brightness(100) \
            .with_motion_sensor() \
            .build()
            
        light2 = SmartLightBuilder() \
            .set_name("Фонарь №2") \
            .set_brightness(80) \
            .set_color_temperature("warm") \
            .build()
        
        # Простые фонари через Composite
        self.main_street.add(Light("Обычный фонарь A", 60))
        self.main_street.add(Light("Обычный фонарь B", 60))
        self.park.add(Light("Парковый фонарь", 40))
        
        self.all_groups = [self.main_street, self.park]
    
    def active_count(self):
        return sum(len(group.children) for group in self.all_groups)
    
    def menu(self):
        while True:
            print("\nОсвещение")
            print("1. Включить всё освещение")
            print("2. Выключить всё")
            print("3. Ночное энергосбережение (50%)")
            print("0. Назад")
            
            ch = input("→ ").strip()
            if ch == "1":
                for group in self.all_groups:
                    group.turn_on()
                print("Всё освещение включено")
            elif ch == "2":
                for group in self.all_groups:
                    group.turn_off()
                print("Всё освещение выключено")
            elif ch == "3":
                print("Переход в ночной режим...")
                for group in self.all_groups:
                    for child in group.children:
                        child.power = child.power // 2 if hasattr(child, 'power') else child.power
            elif ch == "0":
                break