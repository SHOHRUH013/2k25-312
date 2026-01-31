// PATTERN: Builder

package com.example.builder;

public class SmartStreet {

    private final int lamps;
    private final int cameras;
    private final int solarPanels;

    private SmartStreet(Builder builder) {
        this.lamps = builder.lamps;
        this.cameras = builder.cameras;
        this.solarPanels = builder.solarPanels;
    }

    public void info() {
        System.out.println(
                "Chiroq: " + lamps +
                " | Kamera: " + cameras +
                " | Quyosh paneli: " + solarPanels
        );
    }

    public static class Builder {
        private int lamps;
        private int cameras;
        private int solarPanels;

        public Builder addLamps(int lamps) {
            this.lamps = lamps;
            return this;
        }

        public Builder addCameras(int cameras) {
            this.cameras = cameras;
            return this;
        }

        public Builder addSolarPanels(int solarPanels) {
            this.solarPanels = solarPanels;
            return this;
        }

        public SmartStreet build() {
            return new SmartStreet(this);
        }
    }
}
