// PATTERN: Decorator (Concrete Component)

package com.example.decorator;

public class BasicLighting implements LightingSystem {

    @Override
    public void turnOnAll() {
        System.out.println("Barcha chiroqlar YOQILDI");
    }
}
