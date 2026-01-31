namespace SmartCity.Modules.Energy;
public class EnergyData {
    public double Consumption { get; set; }
    public double Production { get; set; }
    public DateTime Timestamp { get; set; }
    public override string ToString() {
        return $"⚡ Iste'mol: {Consumption:F2} kWh | Ishlab chiqarish: {Production:F2} kWh | Vaqt: {Timestamp:HH:mm:ss}";
    }
}
