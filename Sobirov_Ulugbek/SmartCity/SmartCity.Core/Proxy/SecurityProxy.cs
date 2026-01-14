namespace SmartCity.Core.Proxy;
public class SecurityProxy : ISecurityAccess
{
    private readonly SecuritySystem _realSystem;
    private readonly List<string> _authorizedUsers = new() { "admin", "security" };
    
    public SecurityProxy()
    {
        _realSystem = new SecuritySystem();
    }
    
    private bool CheckAccess(string user)
    {
        if (_authorizedUsers.Contains(user.ToLower()))
        {
            return true;
        }
        
        Console.WriteLine($"❌ RUXSAT RAD ETILDI: [{user}] xavfsizlik tizimiga kira olmaydi!");
        return false;
    }
    
    public void AccessSecuritySystem(string user)
    {
        Console.WriteLine($"🔐 Proxy: [{user}] uchun ruxsat tekshirilmoqda...");
        if (CheckAccess(user))
        {
            _realSystem.AccessSecuritySystem(user);
        }
    }
    
    public void ViewCameraFeed(string cameraId, string user)
    {
        Console.WriteLine($"🔐 Proxy: [{user}] uchun kamera ruxsati tekshirilmoqda...");
        if (CheckAccess(user))
        {
            _realSystem.ViewCameraFeed(cameraId, user);
        }
    }
    
    public void ControlAlarm(string action, string user)
    {
        Console.WriteLine($"🔐 Proxy: [{user}] uchun signalizatsiya ruxsati tekshirilmoqda...");
        if (CheckAccess(user))
        {
            _realSystem.ControlAlarm(action, user);
        }
    }
}
