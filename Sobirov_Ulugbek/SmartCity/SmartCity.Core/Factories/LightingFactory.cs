using SmartCity.Modules.Lighting;
using SmartCity.Modules.Security;

namespace SmartCity.Core.Factories;

public class LightingFactory : IDeviceFactory
{
    public StreetLight CreateLight(string id)
    {
        return new StreetLight 
        { 
            Id = id, 
            Brightness = 100,
            IsOn = false
        };
    }
    
    public Camera CreateCamera(string id, string zone)
    {
        return new Camera 
        { 
            Id = id, 
            Zone = zone,
            IsRecording = false
        };
    }
}
