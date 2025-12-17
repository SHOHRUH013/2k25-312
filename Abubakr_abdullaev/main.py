from core.controller import CityController

def main():
    print("🌆 Добро пожаловать в SmartCity System v2.0")
    print("Инициализация города...\n")
    
    city = CityController.get_instance()
    
    while True:
        print("═" * 50)
        print("ГЛАВНОЕ МЕНЮ")
        print("1. Управление освещением")
        print("2. Управление транспортом")
        print("3. Система безопасности")
        print("4. Энергосбережение")
        print("5. Общий статус города")
        print("0. Выход")
        print("═" * 50)
        
        choice = input("Выберите пункт: ").strip()
        
        if choice == "1":
            city.manage_lighting()
        elif choice == "2":
            city.manage_transport()
        elif choice == "3":
            city.manage_security()
        elif choice == "4":
            city.manage_energy()
        elif choice == "5":
            city.show_status()
        elif choice == "0":
            print("До свидания! Город переходит в автономный режим... 🌙")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()