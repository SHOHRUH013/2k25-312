using SmartCity.Modules.Lighting;
using SmartCity.Modules.Security;

namespace SmartCity.Core.Factories;

public class SecurityFactory : IDeviceFactory
{
    public StreetLight CreateLight(string id)
    {
        return new StreetLight 
        { 
            Id = id, 
            Brightness = 50,
            IsOn = true
        };
    }
    
    public Camera CreateCamera(string id, string zone)
    {
        return new Camera 
        { 
            Id = id, 
            Zone = zone,
            IsRecording = true
        };
    }
}
