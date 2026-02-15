using SmartCity.Modules.Energy;
namespace SmartCity.Core.Adapters;
public class EnergyAdapter : IEnergyMonitor
{
    private readonly LegacyEnergySystem _legacySystem;
    
    public EnergyAdapter(LegacyEnergySystem legacySystem)
    {
        _legacySystem = legacySystem;
    }
    
    public EnergyData GetCurrentEnergyData()
    {
        string rawData = _legacySystem.GetPowerData();
        var parts = rawData.Split('|');
        
        return new EnergyData
        {
            Consumption = double.Parse(parts[0]),
            Production = double.Parse(parts[1]),
            Timestamp = DateTime.Parse(parts[2])
        };
    }
}
