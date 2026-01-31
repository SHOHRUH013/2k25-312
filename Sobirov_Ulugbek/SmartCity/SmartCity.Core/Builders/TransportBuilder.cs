namespace SmartCity.Core.Builders;
public class TransportBuilder : ITransportBuilder
{
    private readonly Transport _transport = new();
    
    public ITransportBuilder SetType(string type)
    {
        _transport.Type = type;
        return this;
    }
    
    public ITransportBuilder SetCapacity(int capacity)
    {
        _transport.Capacity = capacity;
        return this;
    }
    
    public ITransportBuilder SetRoute(string route)
    {
        _transport.Route = route;
        return this;
    }
    
    public ITransportBuilder AddGPS()
    {
        _transport.HasGPS = true;
        return this;
    }
    
    public ITransportBuilder MakeElectric()
    {
        _transport.IsElectric = true;
        return this;
    }
    
    public Transport Build()
    {
        return _transport;
    }
}
