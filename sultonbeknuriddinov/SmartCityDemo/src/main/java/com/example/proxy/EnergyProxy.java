
package com.example.proxy;

public class EnergyProxy implements EnergySystem {

    private final RealEnergySystem realEnergySystem;
    private final String role;

    public EnergyProxy(String role) {
        this.role = role;
        this.realEnergySystem = new RealEnergySystem();
    }

    @Override
    public String getReport() {
        return realEnergySystem.getReport();
    }

    @Override
    public void setMode(String mode) {
        if (!"admin".equals(role)) {
            System.out.println("XATO: Faqat ADMIN o‘zgartira oladi!");
            return;
        }
        realEnergySystem.setMode(mode);
    }
}
