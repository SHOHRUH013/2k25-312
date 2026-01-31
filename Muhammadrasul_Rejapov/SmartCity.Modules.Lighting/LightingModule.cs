using SmartCity.Core;
using System;

namespace SmartCity.Modules.Lighting
{
    public class LightingModule : IModule
    {
        public string Name => "Lighting";

        public void Execute()
        {
            Console.WriteLine("💡 City lighting adjusted based on time and weather.");
        }
    }
}
