namespace SmartCity.Core.Adapters;
public class LegacyEnergySystem
{
    public string GetPowerData()
    {
        var consumption = new Random().Next(100, 200) + new Random().NextDouble();
        var production = new Random().Next(50, 100) + new Random().NextDouble();
        var date = DateTime.Now.ToString("yyyy-MM-dd");
        return $"{consumption:F2}|{production:F2}|{date}";
    }
}
