using Xunit;
using SmartCity.App.Factories;
using SmartCity.Core;
using SmartCity.Modules.Lighting;
using SmartCity.Modules.Transport;
using SmartCity.Modules.Security;
using SmartCity.Modules.Energy;

namespace SmartCity.Tests
{
    public class ModuleFactoryTests
    {
        [Fact]
        public void LightingModule_CreatedSuccessfully()
        {
            var module = ModuleFactory.Create("Lighting");
            Assert.NotNull(module);
            Assert.IsAssignableFrom<IModule>(module);
        }

        [Fact]
        public void TransportModule_CreatedSuccessfully()
        {
            var module = ModuleFactory.Create("Transport");
            Assert.NotNull(module);
            Assert.IsAssignableFrom<IModule>(module);
        }

        [Fact]
        public void SecurityModule_CreatedSuccessfully()
        {
            var module = ModuleFactory.Create("Security");
            Assert.NotNull(module);
            Assert.IsAssignableFrom<IModule>(module);
        }

        [Fact]
        public void EnergyModule_CreatedSuccessfully()
        {
            var module = ModuleFactory.Create("Energy");
            Assert.NotNull(module);
            Assert.IsAssignableFrom<IModule>(module);
        }
    }
}
