// Transport Module - shahar transporti boshqaruvi

import { SubsystemType, DeviceStatus } from '../../core/types';
import { TransportSubsystem } from '../../core/factories/SubsystemFactory';
import { TransportDeviceFactory, TrafficSensor, TrafficLightController, TrafficBarrier } from '../../core/factories/DeviceFactory';

export class TransportModule extends TransportSubsystem {
  private deviceFactory: TransportDeviceFactory;
  private trafficLights: Map<string, TrafficLightController> = new Map();
  private sensors: Map<string, TrafficSensor> = new Map();
  private barriers: Map<string, TrafficBarrier> = new Map();

  constructor() {
    super();
    this.deviceFactory = new TransportDeviceFactory();
    this.name = 'Advanced Transport Management';
  }

  public initialize(): void {
    console.log('\n🚗 Initializing Transport Module...');
    this.createDefaultDevices();
    console.log('✅ Transport Module initialized\n');
  }

  private createDefaultDevices(): void {
    this.addTrafficLight('main-intersection', 'Main Street Traffic Light', 'Main St & 1st Ave');
    this.addTrafficLight('north-entry', 'North Entry Light', 'North Gate');
    this.addTrafficLight('south-entry', 'South Entry Light', 'South Gate');
    this.addTrafficSensor('sensor-highway', 'Highway Sensor', 'Highway Entry');
    this.addTrafficSensor('sensor-downtown', 'Downtown Sensor', 'City Center');
    this.addBarrier('barrier-parking', 'Parking Barrier', 'Central Parking');
    this.addBarrier('barrier-restricted', 'Restricted Zone Barrier', 'Government Area');
  }

  public addTrafficLight(id: string, name: string, location: string): TrafficLightController {
    const light = this.deviceFactory.createController(id, name, location) as TrafficLightController;
    this.trafficLights.set(id, light);
    this.addDevice(light);
    return light;
  }

  public addTrafficSensor(id: string, name: string, location: string): TrafficSensor {
    const sensor = this.deviceFactory.createSensor(id, name, location) as TrafficSensor;
    this.sensors.set(id, sensor);
    this.addDevice(sensor);
    return sensor;
  }

  public addBarrier(id: string, name: string, location: string): TrafficBarrier {
    const barrier = this.deviceFactory.createActuator(id, name, location) as TrafficBarrier;
    this.barriers.set(id, barrier);
    this.addDevice(barrier);
    return barrier;
  }

  public setEmergencyMode(enable: boolean): void {
    if (enable) {
      console.log('\n🚨 EMERGENCY MODE: All traffic lights turning GREEN');
      this.trafficLights.forEach(light => { light.activate(); light.execute('green'); });
    } else {
      console.log('\n✅ Emergency mode disabled');
      this.trafficLights.forEach(light => light.execute('red'));
    }
  }

  public monitorTraffic(): Map<string, { vehicleCount: number; unit: string }> {
    const readings = new Map<string, { vehicleCount: number; unit: string }>();
    console.log('\n📊 Traffic Monitoring Report:');
    console.log('─'.repeat(40));
    this.sensors.forEach((sensor, id) => {
      sensor.activate();
      const count = sensor.readValue();
      const unit = sensor.getUnit();
      readings.set(id, { vehicleCount: count, unit });
      console.log(`  ${sensor.name}: ${count} ${unit}`);
    });
    console.log('─'.repeat(40) + '\n');
    return readings;
  }

  public controlTrafficLight(id: string, phase: 'green' | 'yellow' | 'red'): boolean {
    const light = this.trafficLights.get(id);
    if (light) { light.execute(phase); return true; }
    console.log(`❌ Traffic light not found: ${id}`);
    return false;
  }

  public controlBarrier(id: string, openPercentage: number): boolean {
    const barrier = this.barriers.get(id);
    if (barrier) { barrier.activate(); barrier.setValue(openPercentage); return true; }
    console.log(`❌ Barrier not found: ${id}`);
    return false;
  }

  public listTrafficLights(): void {
    console.log('\n🚦 Traffic Lights:');
    console.log('─'.repeat(50));
    this.trafficLights.forEach((light, id) => {
      console.log(`  [${id}] ${light.name} @ ${light.location}`);
      console.log(`      Status: ${light.getStatus()}, Phase: ${light.getCurrentPhase()}`);
    });
    console.log('─'.repeat(50) + '\n');
  }

  public getModuleReport(): string {
    const totalTraffic = Array.from(this.sensors.values())
      .reduce((sum, s) => sum + (s.getStatus() === DeviceStatus.ACTIVE ? s.readValue() : 0), 0);
    return `
╔══════════════════════════════════════════╗
║        TRANSPORT MODULE REPORT           ║
╠══════════════════════════════════════════╣
║ Traffic Lights: ${String(this.trafficLights.size).padEnd(23)}║
║ Sensors: ${String(this.sensors.size).padEnd(30)}║
║ Barriers: ${String(this.barriers.size).padEnd(29)}║
║ Total Vehicles Detected: ${String(totalTraffic).padEnd(14)}║
║ Status: ${(this.isActive ? '🟢 Active' : '🔴 Inactive').padEnd(31)}║
╚══════════════════════════════════════════╝`;
  }
}
