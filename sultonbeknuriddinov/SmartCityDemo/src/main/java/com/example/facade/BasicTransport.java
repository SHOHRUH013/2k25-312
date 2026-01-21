// PATTERN: Facade (Subsystem implementation)

package com.example.facade;

public class BasicTransport implements TransportSystem {

    @Override
    public void emergencyStop() {
        System.out.println("BARCHA TRANSPORT TO‘XTATILDI!");
    }
}
