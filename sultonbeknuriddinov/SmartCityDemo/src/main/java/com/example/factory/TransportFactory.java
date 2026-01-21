// PATTERN: Abstract Factory + Factory Method (Concrete Factory)

package com.example.factory;

public class TransportFactory implements DeviceFactory {

    @Override
    public Device createDevice() {
        return () -> "Smart svetofor: YASHIL";
    }
}
