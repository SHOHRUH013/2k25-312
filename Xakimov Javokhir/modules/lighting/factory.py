from modules.lighting.light import Light, StreetLight, IndoorLight, EmergencyLight


class LightFactory:
    # factory method: создание различных типов светильников
    @staticmethod
    def create_light(light_type, location):
        if light_type == "street":
            return StreetLight(location)
        elif light_type == "indoor":
            return IndoorLight(location)
        elif light_type == "emergency":
            return EmergencyLight(location)
        else:
            raise ValueError(f"неизвестный тип светильника: {light_type}")

