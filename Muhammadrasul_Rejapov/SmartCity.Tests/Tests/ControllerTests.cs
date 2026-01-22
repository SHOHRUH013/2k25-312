using Xunit;
using SmartCity.App.Controller;

namespace SmartCity.Tests
{
    public class ControllerTests
    {
        [Fact]
        public void Singleton_InstanceIsSame()
        {
            var instance1 = SmartCityController.Instance;
            var instance2 = SmartCityController.Instance;
            Assert.Same(instance1, instance2);
        }
    }
}