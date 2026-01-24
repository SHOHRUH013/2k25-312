namespace SmartCity.Core
{
    public interface IModule
    {
        string Name { get; }
        void Execute();
    }
}