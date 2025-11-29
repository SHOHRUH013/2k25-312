"""
SmartCity System - Main Entry Point
Utilizes multiple design patterns for intelligent city management
"""

from core.controller import SmartCityController
from modules.transport.transport_system import TrafficLight, PublicTransport
from modules.lighting.lighting_system import StreetLight
from modules.security.security_system import Camera
from modules.energy.energy_system import SolarPanel


def display_menu():
    """Display main menu options"""
    print("\n" + "=" * 50)
    print("🏙️  SMARTCITY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Manage Transportation")
    print("2. Manage Street Lighting")
    print("3. Manage Security System")
    print("4. Manage Energy System")
    print("5. View System Status")
    print("6. Generate System Report")
    print("0. Exit")
    print("=" * 50)


def transportation_menu(controller):
    """Transportation subsystem menu"""
    print("\n🚦 Transportation Management")
    print("1. Create Traffic Light")
    print("2. Create Public Transport")
    print("3. Control Traffic Light")
    print("4. View Transport Status")
    print("0. Back")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        location = input("Enter location: ").strip()
        device = controller.create_device("traffic_light", location)
        print(f"✅ Traffic light created at {location}")

    elif choice == "2":
        route = input("Enter route: ").strip()
        device = controller.create_device("public_transport", route)
        print(f"✅ Public transport created on route {route}")

    elif choice == "3":
        location = input("Enter traffic light location: ").strip()
        state = input("Enter state (red/yellow/green): ").strip()
        # Simple control demonstration
        print(f"🚦 Traffic light at {location} set to {state}")

    elif choice == "4":
        print("\n📊 Transportation Status:")
        controller.get_system_status()


def lighting_menu(controller):
    """Lighting subsystem menu"""
    print("\n💡 Street Lighting Management")
    print("1. Install Street Light")
    print("2. Control Street Light")
    print("3. View Lighting Status")
    print("0. Back")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        location = input("Enter location: ").strip()
        device = controller.create_device("street_light", location)
        print(f"✅ Street light installed at {location}")

    elif choice == "2":
        location = input("Enter location: ").strip()
        action = input("Turn on/off: ").strip()
        print(f"💡 Street light at {location} turned {action}")

    elif choice == "3":
        print("\n📊 Lighting Status:")
        controller.get_system_status()


def security_menu(controller):
    """Security subsystem menu"""
    print("\n🔒 Security System Management")
    print("1. Install Camera")
    print("2. Access Camera (via Proxy)")
    print("3. View Security Status")
    print("0. Back")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        location = input("Enter location: ").strip()
        device = controller.create_device("camera", location)
        print(f"✅ Security camera installed at {location}")

    elif choice == "2":
        location = input("Enter camera location: ").strip()
        print(f"🎥 Accessing camera at {location}...")
        print("📹 Live feed active (simulated)")

    elif choice == "3":
        print("\n📊 Security Status:")
        controller.get_system_status()


def energy_menu(controller):
    """Energy subsystem menu"""
    print("\n⚡ Energy Management")
    print("1. Install Solar Panel")
    print("2. Check Energy Production")
    print("3. View Energy Status")
    print("0. Back")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        location = input("Enter location: ").strip()
        device = controller.create_device("solar_panel", location)
        print(f"✅ Solar panel installed at {location}")

    elif choice == "2":
        print("\n⚡ Current Energy Production: 1250 kWh")
        print("☀️ Solar panels active: 12")
        print("📊 Efficiency: 87%")

    elif choice == "3":
        print("\n📊 Energy Status:")
        controller.get_system_status()


def main():
    """Main application loop"""
    # Singleton pattern: Only one controller instance
    controller = SmartCityController()

    print("\n🌟 Welcome to SmartCity Management System")
    print("Initializing subsystems...")

    # Initialize some default devices
    controller.create_device("traffic_light", "Central Square")
    controller.create_device("street_light", "Main Street")
    controller.create_device("camera", "City Hall")
    controller.create_device("solar_panel", "City Hall Roof")

    print("✅ System initialized successfully!")

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            transportation_menu(controller)

        elif choice == "2":
            lighting_menu(controller)

        elif choice == "3":
            security_menu(controller)

        elif choice == "4":
            energy_menu(controller)

        elif choice == "5":
            print("\n📊 SYSTEM STATUS")
            print("=" * 50)
            controller.get_system_status()

        elif choice == "6":
            print("\n📄 SYSTEM REPORT")
            print("=" * 50)
            controller.generate_report()

        elif choice == "0":
            print("\n👋 Shutting down SmartCity System...")
            print("Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()