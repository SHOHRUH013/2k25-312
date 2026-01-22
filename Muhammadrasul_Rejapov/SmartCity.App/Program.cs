using SmartCity.App.Factories;
using SmartCity.App.Controller;

class Program
{
    static void Main()
    {
        var controller = SmartCityController.Instance;

        controller.RegisterModule(ModuleFactory.Create("lighting"));
        controller.RegisterModule(ModuleFactory.Create("transport"));
        controller.RegisterModule(ModuleFactory.Create("energy"));
        controller.RegisterModule(ModuleFactory.Create("security"));

        controller.ExecuteAll();
    }
}