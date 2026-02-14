
from core.controller import SmartCityController
from core.factories.city_factory import BasicCityFactory, AdvancedCityFactory
from core.builders.city_builder import CityConfigBuilder

def choose_factory():
    print("\nChoose city type:")
    print("1) Basic City")
    print("2) Advanced City")
    choice = input("Select (1-2): ").strip()
    if choice == "2":
        return AdvancedCityFactory()
    return BasicCityFactory()

def build_config():
    builder = CityConfigBuilder()
    name = input("City name (default SmartCity): ").strip() or "SmartCity"
    lights = input("Number of street lights (default 10): ").strip()
    buses = input("Number of buses (default 5): ").strip()
    strict = input("Strict security mode? (y/n, default n): ").strip().lower() == "y"

    builder.set_city_name(name)
    builder.set_num_lights(int(lights) if lights.isdigit() else 10)
    builder.set_num_buses(int(buses) if buses.isdigit() else 5)
    builder.set_strict_security(strict)
    return builder.build()

def main():
    print("=== SmartCity System (Console) ===")
    factory = choose_factory()
    config = build_config()
    controller = SmartCityController(factory=factory, config=config)

    while True:
        print("\n1) Status\n2) Lighting ON\n3) Lighting OFF\n4) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            print(controller.get_status())
        elif choice == "2":
            controller.lighting_on()
            print("Lights ON")
        elif choice == "3":
            controller.lighting_off()
            print("Lights OFF")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
