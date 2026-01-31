namespace SmartCity.Modules.Security;
public class Camera {
    public string Id { get; set; } = string.Empty;
    public string Zone { get; set; } = string.Empty;
    public bool IsRecording { get; set; }
    public void StartRecording() {
        IsRecording = true;
        Console.WriteLine($"📹 Kamera [{Id}] yozib olishni boshladi (Zona: {Zone})");
    }
    public void StopRecording() {
        IsRecording = false;
        Console.WriteLine($"📹 Kamera [{Id}] yozib olishni to'xtatdi");
    }
}
