from core.singelton.city_singelton import CitySingleton
from core.factories.device_factory import DeviceFactory
from core.builders.lighting_builder import LightingBuilder
from core.builders.transport_builder import TransportRouteBuilder
from core.adapters.weather_adaptor import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy
from modules.lighting.lighting import LightingSystem
from modules.transport.transport import TransportSystem
from modules.security.security import RealSecuritySystem
from modules.energy.energy import EnergySystem

def seed_system():
    weather = WeatherAdapter()
    lighting = LightingSystem(weather_adapter=weather)
    transport = TransportSystem()
    energy = EnergySystem()
    real_security = RealSecuritySystem()
    security = SecurityProxy(real_security)

    return {
        "lighting": lighting,
        "transport": transport,
        "energy": energy,
        "security": security,
        "weather": weather
    }

def show_menu():
    print("\n=== SmartCity Console ===")
    print("1. Lighting konfiguratsiyasini Builder bilan qo'llash")
    print("2. Transport marshrutini Builder bilan yaratish")
    print("3. Barcha chiroqlarni yoqish")
    print("4. Transportni ishga tushirish va optimallashtirish")
    print("5. Xavfsizlik: kameralarni ko'rish (admin kerak)")
    print("6. Energiya tejamkor rejimini yoqish")
    print("7. Shahar holatini ko'rish")
    print("0. Chiqish")

def main():
    cfg = CitySingleton()
    print("Xizmat:", cfg.info())

    subs = seed_system()
    lighting = subs["lighting"]
    transport = subs["transport"]
    energy = subs["energy"]
    security = subs["security"]
    weather = subs["weather"]

    factory = DeviceFactory()

    admin = {"name": "Admin", "role": "admin"}
    user = {"name": "User", "role": "user"}

    while True:
        show_menu()
        choice = input("Tanlov: ").strip()

        if choice == "1":
            lb = LightingBuilder()
            cfg_l = lb.set_brightness(70).set_mode("eco").set_auto_off(10).build()
            lighting.apply_configuration(cfg_l)

        elif choice == "2":
            tb = TransportRouteBuilder()
            route = tb.set_number(7).add_stop("Station A").add_stop("Center").set_speed_limit(45).build()
            transport.set_route(route)

        elif choice == "3":
            lighting.turn_on()

        elif choice == "4":
            transport.start()
            transport.optimize()

        elif choice == "5":
            try:
                cams = security.view_cameras(admin)
                print(cams)
            except PermissionError as e:
                print("Ruxsat yo'q:", e)

        elif choice == "6":
            energy.optimize()

        elif choice == "7":
            print("Lighting:", lighting.status())
            print("Transport:", transport.status())
            print("Security:", security._real.status() if hasattr(security, "_real") else "proxy")
            print("Energy:", energy.status())
            print("Weather:", weather.get_temperature_celsius(), "C")

        elif choice == "0":
            print("Tizimdan chiqish...")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
