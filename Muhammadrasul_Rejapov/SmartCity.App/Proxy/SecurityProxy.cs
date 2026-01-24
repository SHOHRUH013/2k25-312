using SmartCity.Core;
using SmartCity.Modules.Security;
using System;

namespace SmartCity.App.Proxy
{
    public class SecurityProxy : IModule
    {
        private readonly SecurityModule _security;
        private readonly string _password;

        public SecurityProxy(string password)
        {
            _password = password;
            _security = new SecurityModule();
        }

        public string Name => "Security Proxy";

        public void Execute()
        {
            if (!CanAccess())
            {
                Console.WriteLine("❌ Access Denied!");
                return;
            }

            _security.Execute();
        }

        // Qo‘shimcha metod testlar uchun
        public bool CanAccess() => _password == "admin123";
    }
}