"""Console entry point for SmartCity System."""
from core.controller import SmartCityController

def main():
    controller = SmartCityController.get_instance()
    print("=== SmartCity System ===")
    while True:
        print("\nГлавное меню:")
        print("1) Lighting")
        print("2) Transport")
        print("3) Security")
        print("4) Energy")
        print("5) Show status")
        print("0) Exit")
        choice = input("Выберите опцию: ").strip()
        if choice == "0":
            print("Выход...")
            break
        elif choice == "1":
            controller.run_module("lighting")
        elif choice == "2":
            controller.run_module("transport")
        elif choice == "3":
            controller.run_module("security")
        elif choice == "4":
            controller.run_module("energy")
        elif choice == "5":
            controller.show_status()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
