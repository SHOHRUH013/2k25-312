"""
Main entry point for SmartCity System
Uses: Facade Pattern, Singleton Pattern
"""
from core.controller import SmartCityController
from core.builders.system_builder import SmartCitySystemBuilder

def main():
    print("🏙️  Welcome to SmartCity System!")
    print("=" * 50)

    # Get controller instance (Singleton)
    controller = SmartCityController.get_instance()

    # Build the system using Builder Pattern
    builder = SmartCitySystemBuilder()
    smart_city = (builder
                 .add_transport_system()
                 .add_lighting_system()
                 .add_security_system()
                 .add_energy_system()
                 .build())

    while True:
        print("\n🔧 SmartCity Management Console:")
        print("1. Manage Transportation")
        print("2. Manage Lighting")
        print("3. Manage Security")
        print("4. Manage Energy")
        print("5. System Status")
        print("6. Emergency Protocol")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            transport_menu(controller)
        elif choice == '2':
            lighting_menu(controller)
        elif choice == '3':
            security_menu(controller)
        elif choice == '4':
            energy_menu(controller)
        elif choice == '5':
            controller.get_system_status()
        elif choice == '6':
            controller.activate_emergency_protocol()
        elif choice == '7':
            print("👋 Thank you for using SmartCity System!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def transport_menu(controller):
    """Transport subsystem management menu"""
    print("\n🚗 Transportation Management:")
    print("1. Optimize Traffic")
    print("2. Get Traffic Status")
    print("3. Manage Public Transport")

    choice = input("Enter choice (1-3): ").strip()
    if choice == '1':
        controller.optimize_traffic()
    elif choice == '2':
        print(controller.get_traffic_status())
    elif choice == '3':
        controller.manage_public_transport()
    else:
        print("❌ Invalid choice")

def lighting_menu(controller):
    """Lighting subsystem management menu"""
    print("\n💡 Lighting Management:")
    print("1. Adjust Street Lighting")
    print("2. Get Lighting Status")
    print("3. Toggle Emergency Lighting")

    choice = input("Enter choice (1-3): ").strip()
    if choice == '1':
        try:
            intensity = input("Enter lighting intensity (0-100): ").strip()
            controller.adjust_street_lighting(int(intensity))
        except ValueError:
            print("❌ Please enter a valid number")
    elif choice == '2':
        print(controller.get_lighting_status())
    elif choice == '3':
        controller.toggle_emergency_lighting()
    else:
        print("❌ Invalid choice")

def security_menu(controller):
    """Security subsystem management menu with authentication"""
    print("\n🚨 Security Management:")
    print("1. Monitor Surveillance")
    print("2. Activate Emergency Alert")
    print("3. Get Security Status")
    print("4. Login to Security System")
    print("5. Logout from Security System")

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        try:
            result = controller.monitor_surveillance()
            print(result)
        except PermissionError as e:
            print(f"❌ Access Denied: {e}")
            print("🔐 Please login first using option 4")
    elif choice == '2':
        try:
            result = controller.activate_emergency_alert()
            print(result)
        except PermissionError as e:
            print(f"❌ Access Denied: {e}")
            print("🔐 Please login as admin first using option 4")
    elif choice == '3':
        try:
            result = controller.get_security_status()
            print(result)
        except PermissionError as e:
            print(f"❌ Access Denied: {e}")
    elif choice == '4':
        security_login(controller)
    elif choice == '5':
        controller.security_system.logout()
        print("✅ Logged out from security system")
    else:
        print("❌ Invalid choice")

def security_login(controller):
    """Handle security system authentication"""
    print("\n🔐 Security System Login")
    print("Available accounts:")
    print("admin / admin123 (Full access)")
    print("operator / op123 (Monitoring access)")
    print("viewer / view123 (View-only access)")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if controller.security_system.authenticate(username, password):
        print(f"✅ Successfully logged in as {username}")
    else:
        print("❌ Login failed. Invalid credentials.")

def energy_menu(controller):
    """Energy subsystem management menu"""
    print("\n⚡ Energy Management:")
    print("1. Optimize Energy Distribution")
    print("2. Get Energy Consumption")
    print("3. Toggle Renewable Sources")

    choice = input("Enter choice (1-3): ").strip()
    if choice == '1':
        controller.optimize_energy_distribution()
    elif choice == '2':
        print(controller.get_energy_consumption())
    elif choice == '3':
        controller.toggle_renewable_sources()
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()