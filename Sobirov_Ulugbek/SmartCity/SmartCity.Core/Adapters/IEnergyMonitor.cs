using SmartCity.Modules.Energy;
namespace SmartCity.Core.Adapters;
public interface IEnergyMonitor
{
    EnergyData GetCurrentEnergyData();
}
