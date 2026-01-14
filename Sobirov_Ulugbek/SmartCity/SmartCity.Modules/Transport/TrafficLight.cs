namespace SmartCity.Modules.Transport;
public class TrafficLight {
    public string Location { get; set; } = string.Empty;
    public string CurrentState { get; set; } = "Red";
    public void ChangeState(string newState) {
        CurrentState = newState;
        Console.WriteLine($"🚦 Svetofor [{Location}] holati: {CurrentState}");
    }
}
