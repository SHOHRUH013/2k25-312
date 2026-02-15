using SmartCity.Core;
using System;

namespace SmartCity.Modules.Security
{
    public class SecurityModule : IModule
    {
        public string Name => "Security";

        public void Execute()
        {
            Console.WriteLine("🔒 Security system armed and monitoring.");
        }
    }
}
