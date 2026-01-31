// PATTERN: Decorator (Concrete Decorator)

package com.example.decorator;

public class LoggingLightingDecorator implements LightingSystem {

    private final LightingSystem lightingSystem;

    public LoggingLightingDecorator(LightingSystem lightingSystem) {
        this.lightingSystem = lightingSystem;
    }

    @Override
    public void turnOnAll() {
        System.out.println("[LOG] turnOnAll ishga tushdi");
        lightingSystem.turnOnAll();
    }
}
