// PATTERN: Client (uses all patterns together)

package com.example;

import com.example.builder.SmartStreet;
import com.example.decorator.BasicLighting;
import com.example.decorator.LightingSystem;
import com.example.decorator.LoggingLightingDecorator;
import com.example.facade.BasicTransport;
import com.example.facade.TransportSystem;
import com.example.proxy.EnergyProxy;
import com.example.proxy.EnergySystem;

import java.util.Scanner;

public class SmartCityApp {

    public static void main(String[] args) {

        CityController controller = CityController.getInstance();


        LightingSystem lighting =
                new LoggingLightingDecorator(new BasicLighting());

        TransportSystem transport = new BasicTransport();

        EnergySystem energy = new EnergyProxy("guest");

        controller.register("lighting", lighting);
        controller.register("transport", transport);
        controller.register("energy", energy);

        SmartStreet street = new SmartStreet.Builder()
                .addLamps(35)
                .addCameras(12)
                .addSolarPanels(20)
                .build();

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("""
                    
                    1. Chiroqlarni yoqish
                    2. Transportni to‘xtatish
                    3. Energiya hisoboti
                    4. Admin rejim
                    5. Smart ko‘cha ma'lumoti
                    6. Energiya rejimini o‘zgartirish
                    0. Chiqish
                    """);

            System.out.print("Tanlov: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1" -> controller.turnOnAllLights();
                case "2" -> controller.emergencyStopTraffic();
                case "3" -> System.out.println(controller.getEnergyReport());
                case "4" -> {
                    controller.register("energy", new EnergyProxy("admin"));
                    System.out.println("ADMIN rejimi yoqildi!");
                }
                case "5" -> street.info();
                case "6" -> {
                    System.out.print("Rejim (eco/max): ");
                    controller.setEnergyMode(scanner.nextLine());
                }
                case "0" -> {
                    System.out.println("SmartCity o‘chirildi!");
                    return;
                }
            }
        }
    }
}
