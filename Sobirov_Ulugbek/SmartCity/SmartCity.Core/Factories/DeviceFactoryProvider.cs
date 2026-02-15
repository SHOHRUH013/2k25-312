namespace SmartCity.Core.Factories;

public class DeviceFactoryProvider
{
    public static IDeviceFactory GetFactory(string type)
    {
        return type.ToLower() switch
        {
            "lighting" => new LightingFactory(),
            "security" => new SecurityFactory(),
            _ => throw new ArgumentException($"Noma'lum factory turi: {type}")
        };
    }
}
