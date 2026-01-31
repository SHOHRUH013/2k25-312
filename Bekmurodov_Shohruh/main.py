from Bekmurodov_Shohruh.core.controller import SmartCityController
from core.logging_config import configure_logging

configure_logging()


def main():
    city = SmartCityController()

    while True:
        print("\n=== SmartCity Console ===")
        print("1. Configure lighting")
        print("2. Send transport")
        print("3. Arm security")
        print("4. Disarm security")
        print("5. Eco mode")
        print("6. Exit")

        cmd = input("Select option: ").strip()

        if cmd == "1":
            city.configure_lighting(
                input("Area: "),
                int(input("Brightness: ")),
                input("Schedule: "),
            )

        elif cmd == "2":
            city.send_transport(
                input("Route: "),
                input("Type (bus/tram): ")
            )

        elif cmd == "3":
            city.arm_security()

        elif cmd == "4":
            city.disarm_security()

        elif cmd == "5":
            city.eco_mode()

        elif cmd == "6":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
