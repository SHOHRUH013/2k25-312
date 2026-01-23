"""
Main application entry point
SmartCity System Console Application
"""
import sys
from datetime import datetime
from core.controller import SmartCityController


def display_menu():
    print("\n" + "=" * 50)
    print("🏙️  SMART CITY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Monitor City Status")
    print("2. Create Traffic Alert")
    print("3. Create Security Alert")
    print("4. Check Weather")
    print("5. Control Lighting")
    print("6. Manage Traffic")
    print("7. Security Monitoring")
    print("8. Energy Management")
    print("9. View Configuration")
    print("10. Change City Mode")
    print("11. Emergency Shutdown")
    print("0. Exit")
    print("=" * 50)
    return input("Select option (0-11): ")


def main():
    # Singleton: Get the controller instance
    controller = SmartCityController()

    while True:
        choice = display_menu()

        if choice == '1':
            controller.monitor_city()

        elif choice == '2':
            location = input("Enter location: ")
            severity = input("Enter severity (Low/Medium/High): ") or "Medium"
            controller.create_alert("Traffic", location, severity)

        elif choice == '3':
            location = input("Enter location: ")
            severity = input("Enter severity (Low/Medium/High): ") or "High"
            controller.create_alert("Security", location, severity)

        elif choice == '4':
            weather = controller.weather_service.get_weather(controller.city_name)
            print(f"\n🌤️  Weather in {controller.city_name}:")
            print(f"  Temperature: {weather['temperature']}°C")
            print(f"  Condition: {weather['condition']}")
            print(f"  Humidity: {weather['humidity']}%")
            print(f"  Wind Speed: {weather['wind_speed']} km/h")
            if weather['recommendations']:
                print("  Recommendations:")
                for rec in weather['recommendations']:
                    print(f"    • {rec}")

        elif choice == '5':
            street = input("Enter street name: ")
            dark = input("Is it dark? (y/n): ").lower() == 'y'
            traffic = int(input("Enter traffic density (0-100): ") or "50")
            conditions = {'dark': dark, 'traffic_density': traffic, 'weather': 'Clear'}
            result = controller.lighting.control_lighting(street, conditions)
            print(f"\n💡 {result}")

        elif choice == '6':
            area = input("Enter area to monitor: ")
            density = int(input("Enter traffic density (0-100): ") or "50")
            speed = int(input("Enter average speed (km/h): ") or "40")
            traffic_data = controller.transport.update_traffic(area, density, speed)
            optimization = controller.transport.optimize_traffic_lights(area)
            print(f"\n🚦 Traffic in {area}:")
            print(f"  Density: {traffic_data['density']}%")
            print(f"  Average Speed: {traffic_data['avg_speed']} km/h")
            print(f"  Congestion: {'Yes' if traffic_data['congestion'] else 'No'}")
            print(f"  Action: {optimization}")

        elif choice == '7':
            user = input("Enter your username: ")
            camera_id = input("Enter camera ID to monitor: ")
            status = controller.security_proxy.monitor_area(user, camera_id)
            if status:
                print(f"\n📹 Camera {camera_id} Status:")
                print(f"  Status: {status['status']}")
                print(
                    f"  Objects detected: {', '.join(status['detected_objects']) if status['detected_objects'] else 'None'}")

        elif choice == '8':
            sector = input("Enter sector (Residential/Commercial/Industrial): ")
            consumption = int(input("Enter consumption in kWh: ") or "1000")
            data = controller.energy.monitor_consumption(sector, consumption)
            report = controller.energy.get_energy_report()
            print(f"\n⚡ Energy Report:")
            print(f"  {sector} consumption: {data['consumption_kwh']} kWh")
            print(f"  Total consumption: {report['total_consumption_kwh']} kWh")
            print(f"  Recommendation: {report['recommendation']}")

        elif choice == '9':
            controller.config.display_config()

        elif choice == '10':
            mode = input("Enter mode (standard/eco): ")
            controller.change_city_mode(mode)

        elif choice == '11':
            confirm = input("Are you sure? This will shutdown all systems! (y/n): ")
            if confirm.lower() == 'y':
                controller.emergency_shutdown()
                print("Goodbye!")
                break

        elif choice == '0':
            print("Exiting SmartCity System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()