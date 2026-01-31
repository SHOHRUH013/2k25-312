using SmartCity.Core;
using System;

namespace SmartCity.Modules.Transport
{
    public class TransportModule : IModule
    {
        public string Name => "Transport";

        public void Execute()
        {
            Console.WriteLine("🚌 Transport system updated for traffic flow.");
        }
    }
}
