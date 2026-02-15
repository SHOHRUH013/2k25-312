"""
Facade Pattern Implementation
Purpose: Provide a simplified interface to the complex SmartCity system.
Singleton Pattern Implementation
Purpose: Ensure only one instance of the controller exists.
"""
from core.singleton.config_manager import ConfigManager
from core.factories.subsystem_factory import StandardCityFactory
from core.builders.alert_builder import CityAlertBuilder, AlertDirector
from core.adapters.weather_adapter import WeatherServiceAdapter, ExternalWeatherService
from core.proxy.security_proxy import SecurityProxy


class SmartCityController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize all subsystems"""
        # Singleton: Config Manager
        self.config = ConfigManager()

        # Abstract Factory: Create subsystems
        self.factory = StandardCityFactory()

        # Create subsystems using factory
        self.transport = self.factory.create_transport_system()
        self.lighting = self.factory.create_lighting_system()
        self.security = self.factory.create_security_system()
        self.energy = self.factory.create_energy_system()

        # Proxy: Security with access control
        self.security_proxy = SecurityProxy(self.security)

        # Builder: Alert system
        self.alert_builder = CityAlertBuilder()
        self.alert_director = AlertDirector(self.alert_builder)

        # Adapter: External weather service
        external_weather = ExternalWeatherService()
        self.weather_service = WeatherServiceAdapter(external_weather)

        # System status
        self.system_online = True
        self.city_name = self.config.get('city_name')

        print(f"🚀 SmartCity System '{self.city_name}' initialized!")

    def get_city_status(self):
        """Get overall city status - Facade method"""
        status = {
            'city': self.city_name,
            'system_status': 'ONLINE' if self.system_online else 'OFFLINE',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'subsystems': {
                'transport': self.transport.__class__.__name__,
                'lighting': self.lighting.__class__.__name__,
                'security': self.security_proxy.__class__.__name__,
                'energy': self.energy.__class__.__name__
            }
        }
        return status

    def monitor_city(self):
        """Monitor all city systems - Facade method"""
        print("\n" + "=" * 50)
        print(f"🏙️  SMART CITY MONITORING: {self.city_name}")
        print("=" * 50)

        # Get weather information
        weather = self.weather_service.get_weather(self.city_name)
        print(f"\n🌤️  WEATHER: {weather['condition']}, {weather['temperature']}°C")

        # Monitor subsystems
        self._monitor_transport()
        self._monitor_security()
        self._monitor_energy()
        self._monitor_lighting()

        # Display recommendations
        if weather['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in weather['recommendations']:
                print(f"  • {rec}")

    def _monitor_transport(self):
        """Monitor transport system"""
        traffic_data = self.transport.update_traffic("Downtown", 65, 45)
        optimization = self.transport.optimize_traffic_lights("Downtown")
        print(f"\n🚦 TRANSPORT:")
        print(f"  • Downtown traffic: {traffic_data['density']}% density")
        print(f"  • Average speed: {traffic_data['avg_speed']} km/h")
        print(f"  • Action: {optimization}")

    def _monitor_security(self):
        """Monitor security system"""
        status = self.security_proxy.get_security_status('admin')
        camera_status = self.security_proxy.monitor_area('operator', 'CAM-001')
        print(f"\n🔒 SECURITY:")
        print(f"  • System status: {status['system_status']}")
        print(f"  • Active cameras: {status['active_cameras']}/{status['total_cameras']}")
        print(f"  • Camera CAM-001: {'Active' if camera_status else 'Inactive'}")

    def _monitor_energy(self):
        """Monitor energy system"""
        self.energy.monitor_consumption("Residential", 1200)
        self.energy.monitor_consumption("Commercial", 1800)
        report = self.energy.get_energy_report()
        print(f"\n⚡ ENERGY:")
        print(f"  • Total consumption: {report['total_consumption_kwh']} kWh")
        print(f"  • Grid dependency: {report['grid_dependency_percent']:.1f}%")
        print(f"  • Recommendation: {report['recommendation']}")

    def _monitor_lighting(self):
        """Monitor lighting system"""
        conditions = {'dark': True, 'traffic_density': 65, 'weather': 'Clear'}
        lighting_status = self.lighting.control_lighting("Main Street", conditions)
        energy_usage = self.lighting.get_energy_usage()
        print(f"\n💡 LIGHTING:")
        print(f"  • {lighting_status}")
        print(f"  • Total energy usage: {energy_usage} kWh")

    def create_alert(self, alert_type, location, severity="Medium"):
        """Create alert using Builder pattern"""
        if alert_type == "Traffic":
            alert = self.alert_director.construct_traffic_alert(location, severity)
        elif alert_type == "Security":
            alert = self.alert_director.construct_security_alert(location, severity)
        elif alert_type == "Energy":
            alert = self.alert_director.construct_energy_alert(location, severity)
        else:
            alert = self.alert_builder.set_type(alert_type).set_location(location).build()

        print(f"\n🚨 NEW ALERT CREATED:")
        print(alert)
        return alert

    def emergency_shutdown(self):
        """Emergency shutdown procedure"""
        print("\n⚠️  INITIATING EMERGENCY SHUTDOWN...")
        self.system_online = False
        print("System shutdown complete.")

    def change_city_mode(self, mode):
        """Change city operating mode"""
        if mode == "eco":
            from core.factories.subsystem_factory import EcoCityFactory
            self.factory = EcoCityFactory()
            print("🌿 Switched to ECO mode")
        elif mode == "standard":
            from core.factories.subsystem_factory import StandardCityFactory
            self.factory = StandardCityFactory()
            print("🏙️ Switched to STANDARD mode")