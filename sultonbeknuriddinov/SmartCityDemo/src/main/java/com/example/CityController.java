
package com.example;

import com.example.decorator.LightingSystem;
import com.example.facade.TransportSystem;
import com.example.proxy.EnergySystem;

import java.util.HashMap;
import java.util.Map;

public class CityController {

    private static CityController instance;
    private final Map<String, Object> systems = new HashMap<>();

    private CityController() {}

    public static CityController getInstance() {
        if (instance == null) {
            instance = new CityController();
        }
        return instance;
    }

    public void register(String name, Object system) {
        systems.put(name, system);
    }

    public void turnOnAllLights() {
        ((LightingSystem) systems.get("lighting")).turnOnAll();
    }

    public void emergencyStopTraffic() {
        ((TransportSystem) systems.get("transport")).emergencyStop();
    }

    public String getEnergyReport() {
        return ((EnergySystem) systems.get("energy")).getReport();
    }

    public void setEnergyMode(String mode) {
        ((EnergySystem) systems.get("energy")).setMode(mode);
    }
}
