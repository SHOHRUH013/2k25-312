"""
SmartCity System - Main Entry Point
Demonstrates the use of multiple design patterns in a cohesive smart city management system.
"""

from core.controller import SmartCityController

def print_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🏙️  SMARTCITY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. View City Status")
    print("2. Control Lighting System")
    print("3. Manage Transportation")
    print("4. Security Operations")
    print("5. Energy Management")
    print("6. Add New District")
    print("7. Generate System Report")
    print("8. Emergency Mode")
    print("0. Exit")
    print("="*50)

def main():
    """Main application loop."""
    # Pattern: Singleton - Only one controller instance exists
    controller = SmartCityController.get_instance()
    
    print("\n🌟 Initializing SmartCity System...")
    controller.initialize_city()
    print("✅ System initialized successfully!\n")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            controller.display_city_status()
            
        elif choice == "2":
            print("\n💡 Lighting System Control")
            print("1. Turn on all lights")
            print("2. Turn off all lights")
            print("3. Set brightness level")
            sub_choice = input("Choose action: ").strip()
            
            if sub_choice == "1":
                controller.control_lighting("on")
            elif sub_choice == "2":
                controller.control_lighting("off")
            elif sub_choice == "3":
                level = input("Enter brightness (0-100): ")
                try:
                    controller.control_lighting("dim", int(level))
                except ValueError:
                    print("❌ Invalid brightness level")
                    
        elif choice == "3":
            print("\n🚗 Transportation Management")
            print("1. Optimize traffic flow")
            print("2. Add new vehicle")
            print("3. View traffic report")
            sub_choice = input("Choose action: ").strip()
            
            if sub_choice == "1":
                controller.manage_traffic("optimize")
            elif sub_choice == "2":
                v_type = input("Vehicle type (bus/car/tram): ")
                v_id = input("Vehicle ID: ")
                controller.add_vehicle(v_type, v_id)
            elif sub_choice == "3":
                controller.manage_traffic("report")
                
        elif choice == "4":
            print("\n🔒 Security Operations")
            print("1. Check security status")
            print("2. Trigger alarm")
            print("3. View camera feeds")
            sub_choice = input("Choose action: ").strip()
            
            if sub_choice == "1":
                controller.security_check()
            elif sub_choice == "2":
                location = input("Alarm location: ")
                controller.trigger_alarm(location)
            elif sub_choice == "3":
                controller.view_cameras()
                
        elif choice == "5":
            print("\n⚡ Energy Management")
            print("1. View energy consumption")
            print("2. Optimize energy usage")
            print("3. Switch to renewable sources")
            sub_choice = input("Choose action: ").strip()
            
            if sub_choice == "1":
                controller.check_energy()
            elif sub_choice == "2":
                controller.optimize_energy()
            elif sub_choice == "3":
                controller.switch_energy_source("renewable")
                
        elif choice == "6":
            district_name = input("\nEnter new district name: ")
            controller.add_district(district_name)
            
        elif choice == "7":
            controller.generate_report()
            
        elif choice == "8":
            print("\n🚨 EMERGENCY MODE ACTIVATED")
            controller.emergency_mode()
            
        elif choice == "0":
            print("\n👋 Shutting down SmartCity System...")
            controller.shutdown()
            print("✅ System shutdown complete. Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()