namespace SmartCity.Core.Builders;
public class Transport
{
    public string Type { get; set; } = string.Empty;
    public int Capacity { get; set; }
    public string Route { get; set; } = string.Empty;
    public string Status { get; set; } = "Idle";
    public bool HasGPS { get; set; }
    public bool IsElectric { get; set; }
    
    public void DisplayInfo()
    {
        Console.WriteLine($"\n🚌 Transport ma'lumotlari:");
        Console.WriteLine($"   Tur: {Type}");
        Console.WriteLine($"   Sig'im: {Capacity} kishi");
        Console.WriteLine($"   Marshrut: {Route}");
        Console.WriteLine($"   Holat: {Status}");
        Console.WriteLine($"   GPS: {(HasGPS ? "✅" : "❌")}");
        Console.WriteLine($"   Elektr: {(IsElectric ? "✅" : "❌")}");
    }
    
    public void Start()
    {
        Status = "Running";
        Console.WriteLine($"🚌 {Type} harakatni boshladi ({Route})");
    }
    
    public void Stop()
    {
        Status = "Stopped";
        Console.WriteLine($"🚌 {Type} to'xtadi");
    }
}
