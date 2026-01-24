using SmartCity.Core;
using System;

namespace SmartCity.Modules.Energy
{
    public class EnergyModule : IModule
    {
        public string Name => "Energy";

        public void Execute()
        {
            Console.WriteLine("⚡ Energy consumption optimized.");
        }
    }
}
