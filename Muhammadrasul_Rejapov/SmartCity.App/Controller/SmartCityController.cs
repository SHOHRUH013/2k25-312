using SmartCity.Core;
using System;
using System.Collections.Generic;

namespace SmartCity.App.Controller
{
    // Singleton + Facade
    public class SmartCityController
    {
        private static readonly Lazy<SmartCityController> _instance =
            new Lazy<SmartCityController>(() => new SmartCityController());

        public static SmartCityController Instance => _instance.Value;

        private readonly List<IModule> _modules = new List<IModule>();

        private SmartCityController() { }

        public void RegisterModule(IModule module)
        {
            _modules.Add(module);
        }

        public void ExecuteAll()
        {
            Console.WriteLine("=== SmartCity System ===");
            foreach (var module in _modules)
            {
                module.Execute();
            }
            Console.WriteLine("=== End of Simulation ===");
        }
    }
}