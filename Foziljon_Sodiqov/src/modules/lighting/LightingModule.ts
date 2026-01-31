// Lighting Module - shahar yoritish tizimi

import { DeviceStatus } from '../../core/types';
import { LightingSubsystem } from '../../core/factories/SubsystemFactory';
import { LightingDeviceFactory, LightSensor, LightController, Dimmer } from '../../core/factories/DeviceFactory';

interface LightingZone {
  id: string;
  name: string;
  lights: string[];
  schedule: { onTime: string; offTime: string; brightness: number };
}

export class LightingModule extends LightingSubsystem {
  private deviceFactory: LightingDeviceFactory;
  private lights: Map<string, LightController> = new Map();
  private sensors: Map<string, LightSensor> = new Map();
  private dimmers: Map<string, Dimmer> = new Map();
  private zones: Map<string, LightingZone> = new Map();

  constructor() {
    super();
    this.deviceFactory = new LightingDeviceFactory();
    this.name = 'Smart Street Lighting';
  }

  public initialize(): void {
    console.log('\n💡 Initializing Lighting Module...');
    this.createDefaultDevices();
    this.createDefaultZones();
    console.log('✅ Lighting Module initialized\n');
  }

  private createDefaultDevices(): void {
    this.addLight('light-main-1', 'Main Street Light 1', 'Main St Block 1');
    this.addLight('light-main-2', 'Main Street Light 2', 'Main St Block 2');
    this.addLight('light-main-3', 'Main Street Light 3', 'Main St Block 3');
    this.addLight('light-park-1', 'Central Park Light 1', 'Central Park North');
    this.addLight('light-park-2', 'Central Park Light 2', 'Central Park South');
    this.addLightSensor('sensor-main', 'Main Street Sensor', 'Main St Center');
    this.addLightSensor('sensor-park', 'Park Sensor', 'Central Park');
    this.addDimmer('dimmer-main', 'Main Street Dimmer', 'Main St Control Box');
    this.addDimmer('dimmer-park', 'Park Dimmer', 'Park Control Box');
  }

  private createDefaultZones(): void {
    this.createZone('zone-main', 'Main Street Zone', ['light-main-1', 'light-main-2', 'light-main-3'], 
      { onTime: '18:00', offTime: '06:00', brightness: 100 });
    this.createZone('zone-park', 'Park Zone', ['light-park-1', 'light-park-2'], 
      { onTime: '19:00', offTime: '23:00', brightness: 70 });
  }

  public addLight(id: string, name: string, location: string): LightController {
    const light = this.deviceFactory.createController(id, name, location) as LightController;
    this.lights.set(id, light);
    this.addDevice(light);
    return light;
  }

  public addLightSensor(id: string, name: string, location: string): LightSensor {
    const sensor = this.deviceFactory.createSensor(id, name, location) as LightSensor;
    this.sensors.set(id, sensor);
    this.addDevice(sensor);
    return sensor;
  }

  public addDimmer(id: string, name: string, location: string): Dimmer {
    const dimmer = this.deviceFactory.createActuator(id, name, location) as Dimmer;
    this.dimmers.set(id, dimmer);
    this.addDevice(dimmer);
    return dimmer;
  }

  public createZone(id: string, name: string, lightIds: string[], 
    schedule: { onTime: string; offTime: string; brightness: number }): void {
    this.zones.set(id, { id, name, lights: lightIds, schedule });
    console.log(`🗺️  Zone created: ${name}`);
  }

  public turnOnAllLights(): void {
    console.log('\n💡 Turning on all lights...');
    this.lights.forEach(light => { light.activate(); light.execute('on'); });
  }

  public turnOffAllLights(): void {
    console.log('\n🌑 Turning off all lights...');
    this.lights.forEach(light => { light.execute('off'); light.deactivate(); });
  }

  public activateZone(zoneId: string): void {
    const zone = this.zones.get(zoneId);
    if (!zone) { console.log(`❌ Zone not found: ${zoneId}`); return; }
    console.log(`\n🗺️  Activating zone: ${zone.name}`);
    zone.lights.forEach(lightId => {
      const light = this.lights.get(lightId);
      if (light) { light.activate(); light.execute('on'); }
    });
  }

  public deactivateZone(zoneId: string): void {
    const zone = this.zones.get(zoneId);
    if (!zone) { console.log(`❌ Zone not found: ${zoneId}`); return; }
    console.log(`\n🗺️  Deactivating zone: ${zone.name}`);
    zone.lights.forEach(lightId => {
      const light = this.lights.get(lightId);
      if (light) { light.execute('off'); light.deactivate(); }
    });
  }

  public setZoneBrightness(zoneId: string, brightness: number): void {
    const zone = this.zones.get(zoneId);
    if (!zone) { console.log(`❌ Zone not found: ${zoneId}`); return; }
    console.log(`\n💡 Setting brightness for ${zone.name}: ${brightness}%`);
    this.dimmers.forEach(dimmer => { dimmer.activate(); dimmer.setValue(brightness); });
  }

  public autoAdjustBrightness(): void {
    console.log('\n🔄 Auto-adjusting brightness...');
    let totalLux = 0, sensorCount = 0;
    this.sensors.forEach(sensor => { sensor.activate(); totalLux += sensor.readValue(); sensorCount++; });
    if (sensorCount === 0) { console.log('⚠️  No sensors available'); return; }

    const avgLux = totalLux / sensorCount;
    let targetBrightness = avgLux < 100 ? 100 : avgLux < 500 ? 70 : avgLux < 1000 ? 40 : 0;

    console.log(`📊 Average ambient light: ${avgLux.toFixed(0)} lux`);
    console.log(`💡 Target brightness: ${targetBrightness}%`);

    this.dimmers.forEach(dimmer => dimmer.setValue(targetBrightness));
    if (targetBrightness > 0) this.turnOnAllLights(); else this.turnOffAllLights();
  }

  public getModuleReport(): string {
    const activeLights = Array.from(this.lights.values()).filter(l => l.getStatus() === DeviceStatus.ACTIVE).length;
    const avgBrightness = Array.from(this.dimmers.values()).reduce((sum, d) => sum + d.getValue(), 0) / (this.dimmers.size || 1);
    return `
╔══════════════════════════════════════════╗
║         LIGHTING MODULE REPORT           ║
╠══════════════════════════════════════════╣
║ Total Lights: ${String(this.lights.size).padEnd(25)}║
║ Active Lights: ${String(activeLights).padEnd(24)}║
║ Light Sensors: ${String(this.sensors.size).padEnd(24)}║
║ Dimmers: ${String(this.dimmers.size).padEnd(30)}║
║ Zones: ${String(this.zones.size).padEnd(32)}║
║ Avg Brightness: ${String(avgBrightness.toFixed(0) + '%').padEnd(23)}║
║ Status: ${(this.isActive ? '🟢 Active' : '🔴 Inactive').padEnd(31)}║
╚══════════════════════════════════════════╝`;
  }

  public listZones(): void {
    console.log('\n🗺️  Lighting Zones:');
    console.log('─'.repeat(50));
    this.zones.forEach((zone, id) => {
      console.log(`  [${id}] ${zone.name}`);
      console.log(`      Lights: ${zone.lights.length}, Schedule: ${zone.schedule.onTime} - ${zone.schedule.offTime}`);
    });
    console.log('─'.repeat(50) + '\n');
  }
}
