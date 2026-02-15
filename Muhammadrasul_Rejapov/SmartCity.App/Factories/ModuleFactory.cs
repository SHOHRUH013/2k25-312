using SmartCity.Core;
using SmartCity.Modules.Lighting;
using SmartCity.Modules.Transport;
using SmartCity.Modules.Energy;
using SmartCity.App.Proxy;

namespace SmartCity.App.Factories
{
    public static class ModuleFactory
    {
        public static IModule Create(string type)
        {
            return type.ToLower() switch
            {
                "lighting" => new LightingModule(),
                "transport" => new TransportModule(),
                "energy" => new EnergyModule(),
                "security" => new SecurityProxy("admin123"),
                _ => throw new ArgumentException("Unknown module type")
            };
        }
    }
}