// SmartCity.Core/Controller/CityController.cs
using SmartCity.Core.Adapters;
using SmartCity.Core.Builders;
using SmartCity.Core.Factories;
using SmartCity.Core.Proxy;
using SmartCity.Modules.Lighting;
using SmartCity.Modules.Security;
using SmartCity.Modules.Transport;

namespace SmartCity.Core.Controller;

/// <summary>
/// DESIGN PATTERN: Singleton + Facade
/// Singleton: Faqat bitta CityController mavjud
/// Facade: Barcha subsistemalar uchun sodda interfeys
/// </summary>
public sealed class CityController
{
    private static CityController? _instance;
    private static readonly object _lock = new();
    
    private readonly List<StreetLight> _lights = new();
    private readonly List<Camera> _cameras = new();
    private readonly List<Transport> _transports = new();
    private readonly List<TrafficLight> _trafficLights = new();
    
    private readonly IEnergyMonitor _energyMonitor;
    private readonly ISecurityAccess _securityProxy;
    
    // Private constructor - Singleton pattern
    // private CityController()
    // {
    //     // Adapter pattern - Eski energiya tizimini yangi tizimga ulash
    //     var legacySystem = new LegacyEnergySystem();
    //     _energyMonitor = new EnergyAdapter(legacySystem);
        
    //     // Proxy pattern - Xavfsizlik tizimiga kirish nazorati
    //     _securityProxy = new SecurityProxy();
        
    //     Console.WriteLine("🏙️ SmartCity Controller yaratildi (Singleton)");
    // }
    
    // Singleton instance olish
    public static CityController Instance
    {
        get
        {
            if (_instance == null)
            {
                lock (_lock)
                {
                    _instance ??= new CityController();
                }
            }
            return _instance;
        }
    }
    
    // Facade metodlari - Murakkab operatsiyalarni sodda qilish
    
    public void InitializeCity()
    {
        Console.WriteLine("\n🏙️ Shahar tizimini ishga tushirish...\n");
        
        // Factory Method va Abstract Factory
        var lightingFactory = DeviceFactoryProvider.GetFactory("lighting");
        var securityFactory = DeviceFactoryProvider.GetFactory("security");
        
        // Chiroqlar yaratish
        _lights.Add(lightingFactory.CreateLight("LIGHT-001"));
        _lights.Add(lightingFactory.CreateLight("LIGHT-002"));
        
        // Kameralar yaratish
        _cameras.Add(securityFactory.CreateCamera("CAM-001", "Park"));
        _cameras.Add(securityFactory.CreateCamera("CAM-002", "Markaz"));
        
        // Svetoforlar
        _trafficLights.Add(new TrafficLight { Location = "Main Street" });
        _trafficLights.Add(new TrafficLight { Location = "Central Square" });
        
        // Builder pattern - Transport yaratish
        var builder = new TransportBuilder();
        
        var bus = builder
            .SetType("Avtobus")
            .SetCapacity(50)
            .SetRoute("Markaz - Bog'")
            .AddGPS()
            .MakeElectric()
            .Build();
        _transports.Add(bus);
        
        var taxi = new TransportBuilder()
            .SetType("Taksi")
            .SetCapacity(4)
            .SetRoute("Shahar bo'ylab")
            .AddGPS()
            .Build();
        _transports.Add(taxi);
        
        Console.WriteLine("✅ Shahar tizimi tayyor!\n");
    }
    
    public void ControlLighting(bool turnOn)
    {
        Console.WriteLine($"\n💡 Yoritishni {(turnOn ? "yoqish" : "o'chirish")}:");
        foreach (var light in _lights)
        {
            if (turnOn)
                light.TurnOn();
            else
                light.TurnOff();
        }
    }
    
    public void ManageTraffic()
    {
        Console.WriteLine("\n🚦 Svetoforlarni boshqarish:");
        foreach (var light in _trafficLights)
        {
            light.ChangeState("Green");
            Thread.Sleep(1000);
            light.ChangeState("Yellow");
            Thread.Sleep(500);
            light.ChangeState("Red");
        }
    }
    
    public void StartTransport()
    {
        Console.WriteLine("\n🚌 Transportni ishga tushirish:");
        foreach (var transport in _transports)
        {
            transport.Start();
        }
    }
    
    public void MonitorEnergy()
    {
        Console.WriteLine("\n⚡ Energiya monitoringi:");
        var data = _energyMonitor.GetCurrentEnergyData();
        Console.WriteLine(data);
    }
    
    public void AccessSecurity(string userName)
    {
        Console.WriteLine($"\n🔐 Xavfsizlik tizimiga kirish (Foydalanuvchi: {userName}):");
        _securityProxy.AccessSecuritySystem(userName);
        _securityProxy.ViewCameraFeed("CAM-001", userName);
        _securityProxy.ControlAlarm("yoqish", userName);
    }
    
    public void DisplayStatus()
    {
        Console.WriteLine("\n📊 SHAHAR HOLATI:");
        Console.WriteLine($"   💡 Chiroqlar: {_lights.Count}");
        Console.WriteLine($"   📹 Kameralar: {_cameras.Count}");
        Console.WriteLine($"   🚦 Svetoforlar: {_trafficLights.Count}");
        Console.WriteLine($"   🚌 Transport: {_transports.Count}");
    }
}