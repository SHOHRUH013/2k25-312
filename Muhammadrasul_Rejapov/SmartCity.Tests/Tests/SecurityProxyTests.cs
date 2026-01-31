using Xunit;
using SmartCity.App.Proxy;

namespace SmartCity.Tests
{
    public class SecurityProxyTests
    {
        [Fact]
        public void AccessAllowed_ReturnsTrue()
        {
            var proxy = new SecurityProxy("admin123");
            Assert.True(proxy.CanAccess());
        }

        [Fact]
        public void AccessDenied_ReturnsFalse()
        {
            var proxy = new SecurityProxy("guest");
            Assert.False(proxy.CanAccess());
        }
    }
}