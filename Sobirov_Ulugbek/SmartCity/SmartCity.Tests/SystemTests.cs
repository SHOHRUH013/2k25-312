// SmartCity.Tests/SystemTests.cs
using Xunit;
using SmartCity.Core.Controller;
using SmartCity.Core.Builders;
using SmartCity.Core.Factories;
using SmartCity.Core.Adapters;
using SmartCity.Core.Proxy;

namespace SmartCity.Tests;

/// <summary>
/// SmartCity tizimi uchun Unit testlar
/// </summary>
public class SystemTests
{
    [Fact]
    public void Singleton_ShouldReturnSameInstance()
    {
        // Arrange & Act
        var controller1 = CityController.Instance;
        var controller2 = CityController.Instance;
        
        // Assert
        Assert.Same(controller1, controller2);
    }
    
    [Fact]
    public void Builder_ShouldCreateTransportWithAllProperties()
    {
        // Arrange
        var builder = new TransportBuilder();
        
        // Act
        var transport = builder
            .SetType("Avtobus")
            .SetCapacity(50)
            .SetRoute("A-B")
            .AddGPS()
            .MakeElectric()
            .Build();
        
        // Assert
        Assert.Equal("Avtobus", transport.Type);
        Assert.Equal(50, transport.Capacity);
        Assert.Equal("A-B", transport.Route);
        Assert.True(transport.HasGPS);
        Assert.True(transport.IsElectric);
    }
    
    [Fact]
    public void FactoryMethod_ShouldReturnCorrectFactory()
    {
        // Act
        var lightingFactory = DeviceFactoryProvider.GetFactory("lighting");
        var securityFactory = DeviceFactoryProvider.GetFactory("security");
        
        // Assert
        Assert.IsType<LightingFactory>(lightingFactory);
        Assert.IsType<SecurityFactory>(securityFactory);
    }
    
    [Fact]
    public void AbstractFactory_ShouldCreateLightWithCorrectProperties()
    {
        // Arrange
        var factory = new LightingFactory();
        
        // Act
        var light = factory.CreateLight("TEST-001");
        
        // Assert
        Assert.Equal("TEST-001", light.Id);
        Assert.Equal(100, light.Brightness);
        Assert.False(light.IsOn);
    }
    
    [Fact]
    public void AbstractFactory_ShouldCreateCameraWithCorrectProperties()
    {
        // Arrange
        var factory = new SecurityFactory();
        
        // Act
        var camera = factory.CreateCamera("CAM-001", "Park");
        
        // Assert
        Assert.Equal("CAM-001", camera.Id);
        Assert.Equal("Park", camera.Zone);
        Assert.True(camera.IsRecording); // Security cameras always record
    }
    
    [Fact]
    public void Adapter_ShouldConvertLegacyDataToNewFormat()
    {
        // Arrange
        var legacySystem = new LegacyEnergySystem();
        var adapter = new EnergyAdapter(legacySystem);
        
        // Act
        var data = adapter.GetCurrentEnergyData();
        
        // Assert
        Assert.NotNull(data);
        Assert.True(data.Consumption > 0);
        Assert.True(data.Production > 0);
        Assert.NotEqual(default(DateTime), data.Timestamp);
    }
    
    [Fact]
    public void Proxy_ShouldAllowAuthorizedUser()
    {
        // Arrange
        var proxy = new SecurityProxy();
        
        // Act & Assert - Should not throw exception
        proxy.AccessSecuritySystem("admin");
        proxy.ViewCameraFeed("CAM-001", "admin");
        proxy.ControlAlarm("activate", "security");
    }
    
    [Fact]
    public void Transport_ShouldChangeStateWhenStarted()
    {
        // Arrange
        var transport = new TransportBuilder()
            .SetType("Bus")
            .SetCapacity(30)
            .SetRoute("Route-1")
            .Build();
        
        // Act
        transport.Start();
        
        // Assert
        Assert.Equal("Running", transport.Status);
    }
    
    [Fact]
    public void StreetLight_ShouldTurnOnCorrectly()
    {
        // Arrange
        var factory = new LightingFactory();
        var light = factory.CreateLight("LIGHT-001");
        
        // Act
        light.TurnOn();
        
        // Assert
        Assert.True(light.IsOn);
    }
    
    [Fact]
    public void StreetLight_ShouldChangeBrightness()
    {
        // Arrange
        var factory = new LightingFactory();
        var light = factory.CreateLight("LIGHT-001");
        
        // Act
        light.SetBrightness(75);
        
        // Assert
        Assert.Equal(75, light.Brightness);
    }
    
    [Fact]
    public void Camera_ShouldStartRecording()
    {
        // Arrange
        var factory = new LightingFactory();
        var camera = factory.CreateCamera("CAM-001", "Zone-A");
        
        // Act
        camera.StartRecording();
        
        // Assert
        Assert.True(camera.IsRecording);
    }
    
    [Fact]
    public void FactoryMethod_ShouldThrowExceptionForInvalidType()
    {
        // Act & Assert
        Assert.Throws<ArgumentException>(() => 
            DeviceFactoryProvider.GetFactory("invalid"));
    }
}