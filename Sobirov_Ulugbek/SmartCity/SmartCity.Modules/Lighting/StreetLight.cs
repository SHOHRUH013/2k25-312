namespace SmartCity.Modules.Lighting;
public class StreetLight {
    public string Id { get; set; } = string.Empty;
    public int Brightness { get; set; }
    public bool IsOn { get; set; }
    public void TurnOn() {
        IsOn = true;
        Console.WriteLine($"💡 Chiroq [{Id}] yoqildi (Yorqinlik: {Brightness}%)");
    }
    public void TurnOff() {
        IsOn = false;
        Console.WriteLine($"💡 Chiroq [{Id}] o'chirildi");
    }
    public void SetBrightness(int level) {
        Brightness = level;
        Console.WriteLine($"💡 Chiroq [{Id}] yorqinligi: {Brightness}%");
    }
}
