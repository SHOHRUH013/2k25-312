// PATTERN: Abstract Factory + Factory Method (Concrete Factory)

package com.example.factory;

public class LightingFactory implements DeviceFactory {

    @Override
    public Device createDevice() {
        return () -> "Smart chiroq: YOQILGAN – 90%";
    }
}
