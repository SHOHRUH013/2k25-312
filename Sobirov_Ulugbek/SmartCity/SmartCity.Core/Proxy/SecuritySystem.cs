namespace SmartCity.Core.Proxy;
public class SecuritySystem : ISecurityAccess
{
    public void AccessSecuritySystem(string user)
    {
        Console.WriteLine($"✅ [{user}] xavfsizlik tizimiga kirdi");
    }
    
    public void ViewCameraFeed(string cameraId, string user)
    {
        Console.WriteLine($"📹 [{user}] {cameraId} kamerasini ko'rmoqda");
    }
    
    public void ControlAlarm(string action, string user)
    {
        Console.WriteLine($"🚨 [{user}] signalizatsiyani {action}");
    }
}
