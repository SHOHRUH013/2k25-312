namespace SmartCity.Core.Proxy;
public interface ISecurityAccess
{
    void AccessSecuritySystem(string user);
    void ViewCameraFeed(string cameraId, string user);
    void ControlAlarm(string action, string user);
}
