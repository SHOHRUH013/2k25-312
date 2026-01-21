package com.example.proxy;

public class RealEnergySystem implements EnergySystem {

    private String mode = "normal";

    @Override
    public String getReport() {
        return "Energiya rejimi: " + mode + " | Sarf: 312 kVt/soat";
    }

    @Override
    public void setMode(String mode) {
        this.mode = mode;
        System.out.println("Energiya rejimi " + mode + " ga o‘zgartirildi");
    }
}
