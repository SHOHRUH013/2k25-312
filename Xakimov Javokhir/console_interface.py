from core.controller import SmartCityController
from modules.lighting.lighting_subsystem import LightingSubsystem
from modules.transport.transport_subsystem import TransportSubsystem
from modules.security.security_subsystem import SecuritySubsystem
from modules.energy.energy_subsystem import EnergySubsystem


class ConsoleInterface:
    def __init__(self):
        self.controller = SmartCityController()
        self._init_subsystems()

    def _init_subsystems(self):
        lighting = LightingSubsystem()
        self.controller.register_subsystem("lighting", lighting)
        
        transport = TransportSubsystem()
        self.controller.register_subsystem("transport", transport)
        
        security = SecuritySubsystem()
        self.controller.register_subsystem("security", security)
        
        energy = EnergySubsystem(self.controller)
        self.controller.register_subsystem("energy", energy)

    def _print_menu(self):
        print("\n" + "="*50)
        print("SmartCity System - Главное меню")
        print("="*50)
        print("1. Управление освещением")
        print("2. Управление транспортом")
        print("3. Управление безопасностью")
        print("4. Управление энергопотреблением")
        print("5. Показать статус всех подсистем")
        print("0. Выход")
        print("="*50)

    def _lighting_menu(self):
        while True:
            print("\n--- Управление освещением ---")
            print("1. Добавить светильник")
            print("2. Включить светильник")
            print("3. Выключить светильник")
            print("4. Установить яркость")
            print("5. Показать статус")
            print("0. Назад")
            
            choice = input("Выберите действие: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                print("Типы: street, indoor, emergency")
                light_type = input("Тип светильника: ").strip()
                location = input("Местоположение: ").strip()
                result = self.controller.execute_command("lighting", "add", light_type, location)
                print(result)
            elif choice == "2":
                location = input("Местоположение: ").strip()
                result = self.controller.execute_command("lighting", "on", location)
                print(result)
            elif choice == "3":
                location = input("Местоположение: ").strip()
                result = self.controller.execute_command("lighting", "off", location)
                print(result)
            elif choice == "4":
                location = input("Местоположение: ").strip()
                try:
                    level = int(input("Уровень яркости (0-100): ").strip())
                    result = self.controller.execute_command("lighting", "brightness", location, level)
                    print(result)
                except ValueError:
                    print("неверный формат числа")
            elif choice == "5":
                status = self.controller.execute_command("lighting", "status")
                for loc, data in status.items():
                    print(f"{loc}: включен={data['is_on']}, яркость={data['brightness']}%")
            else:
                print("неверный выбор")

    def _transport_menu(self):
        while True:
            print("\n--- Управление транспортом ---")
            print("1. Добавить транспорт")
            print("2. Начать маршрут")
            print("3. Завершить маршрут")
            print("4. Показать статус")
            print("0. Назад")
            
            choice = input("Выберите действие: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                vehicle_type = input("Тип транспорта: ").strip()
                route = input("Маршрут: ").strip()
                capacity = input("Вместимость (опционально): ").strip()
                fuel_type = input("Тип топлива (опционально): ").strip()
                capacity = int(capacity) if capacity else None
                fuel_type = fuel_type if fuel_type else None
                result = self.controller.execute_command("transport", "add", vehicle_type, route, capacity, fuel_type)
                print(result)
            elif choice == "2":
                vehicle_id = input("ID транспорта: ").strip()
                result = self.controller.execute_command("transport", "start", vehicle_id)
                print(result)
            elif choice == "3":
                vehicle_id = input("ID транспорта: ").strip()
                result = self.controller.execute_command("transport", "stop", vehicle_id)
                print(result)
            elif choice == "4":
                status = self.controller.execute_command("transport", "status")
                for vid, data in status.items():
                    print(f"{vid}: {data['type']} | маршрут: {data['route']} | статус: {data['status']}")
            else:
                print("неверный выбор")

    def _security_menu(self):
        while True:
            print("\n--- Управление безопасностью ---")
            print("1. Добавить камеру")
            print("2. Активировать камеру")
            print("3. Деактивировать камеру")
            print("4. Начать запись")
            print("5. Остановить запись")
            print("6. Показать статус")
            print("0. Назад")
            
            choice = input("Выберите действие: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                location = input("Местоположение: ").strip()
                print("Уровни доступа: public, operator, admin")
                access_level = input("Уровень доступа: ").strip()
                result = self.controller.execute_command("security", "add", location, access_level)
                print(result)
            elif choice == "2":
                camera_id = input("ID камеры: ").strip()
                user_level = input("Уровень пользователя (public/operator/admin): ").strip()
                result = self.controller.execute_command("security", "activate", camera_id, user_level)
                print(result)
            elif choice == "3":
                camera_id = input("ID камеры: ").strip()
                user_level = input("Уровень пользователя (public/operator/admin): ").strip()
                result = self.controller.execute_command("security", "deactivate", camera_id, user_level)
                print(result)
            elif choice == "4":
                camera_id = input("ID камеры: ").strip()
                user_level = input("Уровень пользователя (public/operator/admin): ").strip()
                result = self.controller.execute_command("security", "start_recording", camera_id, user_level)
                print(result)
            elif choice == "5":
                camera_id = input("ID камеры: ").strip()
                user_level = input("Уровень пользователя (public/operator/admin): ").strip()
                result = self.controller.execute_command("security", "stop_recording", camera_id, user_level)
                print(result)
            elif choice == "6":
                user_level = input("Уровень пользователя (public/operator/admin): ").strip()
                status = self.controller.execute_command("security", "status", None, user_level)
                for cam_id, data in status.items():
                    print(f"{cam_id}: {data['location']} | активна={data['is_active']} | запись={data['recording']}")
            else:
                print("неверный выбор")

    def _energy_menu(self):
        while True:
            print("\n--- Управление энергопотреблением ---")
            print("1. Зарегистрировать энергопотребление освещения")
            print("2. Зарегистрировать энергопотребление транспорта")
            print("3. Оптимизировать энергопотребление")
            print("4. Показать отчет")
            print("0. Назад")
            
            choice = input("Выберите действие: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                location = input("Местоположение освещения: ").strip()
                try:
                    consumption = float(input("Энергопотребление (кВт·ч): ").strip())
                    result = self.controller.execute_command("energy", "register_lighting", location, consumption)
                    print(result)
                except ValueError:
                    print("неверный формат числа")
            elif choice == "2":
                vehicle_id = input("ID транспорта: ").strip()
                try:
                    consumption = float(input("Энергопотребление (кВт·ч): ").strip())
                    result = self.controller.execute_command("energy", "register_transport", vehicle_id, consumption)
                    print(result)
                except ValueError:
                    print("неверный формат числа")
            elif choice == "3":
                results = self.controller.execute_command("energy", "optimize")
                if results:
                    print("Результаты оптимизации:")
                    for result in results:
                        print(f"  - {result}")
                else:
                    print("оптимизация не требуется")
            elif choice == "4":
                report = self.controller.execute_command("energy", "report")
                print(f"\nОбщее энергопотребление: {report['total_consumption']} {report['units']}")
                print("\nПо источникам:")
                for source, data in report['consumption_by_source'].items():
                    print(f"  {source}: {data['current']} {report['units']} (активно: {data['active']})")
            else:
                print("неверный выбор")

    def _show_all_status(self):
        print("\n=== Статус всех подсистем ===\n")
        
        print("--- Освещение ---")
        lighting_status = self.controller.execute_command("lighting", "status")
        if lighting_status:
            for loc, data in lighting_status.items():
                print(f"  {loc}: включен={data['is_on']}, яркость={data['brightness']}%")
        else:
            print("  нет светильников")
        
        print("\n--- Транспорт ---")
        transport_status = self.controller.execute_command("transport", "status")
        if transport_status:
            for vid, data in transport_status.items():
                print(f"  {vid}: {data['type']} | маршрут: {data['route']} | статус: {data['status']}")
        else:
            print("  нет транспорта")
        
        print("\n--- Безопасность ---")
        security_status = self.controller.execute_command("security", "status", None, "public")
        if security_status:
            for cam_id, data in security_status.items():
                print(f"  {cam_id}: {data['location']} | активна={data['is_active']} | запись={data['recording']}")
        else:
            print("  нет камер")
        
        print("\n--- Энергопотребление ---")
        energy_report = self.controller.execute_command("energy", "report")
        if energy_report:
            print(f"  Общее: {energy_report['total_consumption']} {energy_report['units']}")
        else:
            print("  данные не зарегистрированы")

    def run(self):
        print("SmartCity System запущена")
        print(f"Зарегистрированные подсистемы: {', '.join(self.controller.list_subsystems())}")
        
        while True:
            self._print_menu()
            choice = input("Выберите пункт меню: ").strip()
            
            if choice == "0":
                print("выход из системы")
                break
            elif choice == "1":
                self._lighting_menu()
            elif choice == "2":
                self._transport_menu()
            elif choice == "3":
                self._security_menu()
            elif choice == "4":
                self._energy_menu()
            elif choice == "5":
                self._show_all_status()
            else:
                print("неверный выбор, попробуйте снова")

