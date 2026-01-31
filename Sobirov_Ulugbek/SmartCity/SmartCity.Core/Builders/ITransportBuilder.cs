namespace SmartCity.Core.Builders;
public interface ITransportBuilder
{
    ITransportBuilder SetType(string type);
    ITransportBuilder SetCapacity(int capacity);
    ITransportBuilder SetRoute(string route);
    ITransportBuilder AddGPS();
    ITransportBuilder MakeElectric();
    Transport Build();
}
