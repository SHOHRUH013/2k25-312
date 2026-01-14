using SmartCity.Modules.Lighting;
using SmartCity.Modules.Security;

namespace SmartCity.Core.Factories;

public interface IDeviceFactory
{
    StreetLight CreateLight(string id);
    Camera CreateCamera(string id, string zone);
}
