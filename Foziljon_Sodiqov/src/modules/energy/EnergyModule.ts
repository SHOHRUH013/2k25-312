// Energy Module - shahar energiya boshqaruvi

import { DeviceStatus, AlertLevel } from '../../core/types';
import { EnergySubsystem } from '../../core/factories/SubsystemFactory';
import { EnergyDeviceFactory, PowerMeter, PowerController, PowerRegulator } from '../../core/factories/DeviceFactory';
import { CityController } from '../../core/singleton/CityController';

interface PowerZone {
  id: string;
  name: string;
  meters: string[];
  regulators: string[];
  maxCapacity: number;
  priority: 'high' | 'medium' | 'low';
}

interface EnergyRecord {
  timestamp: Date;
  totalConsumption: number;
  savingMode: boolean;
}

export class EnergyModule extends EnergySubsystem {
  private deviceFactory: EnergyDeviceFactory;
  private meters: Map<string, PowerMeter> = new Map();
  private controllers: Map<string, PowerController> = new Map();
  private regulators: Map<string, PowerRegulator> = new Map();
  private zones: Map<string, PowerZone> = new Map();
  private usageHistory: EnergyRecord[] = [];
  private maxCapacity: number = 50000;
  private alertThreshold: number = 0.8;
  private solarEnabled: boolean = false;
  private solarOutput: number = 0;

  constructor() {
    super();
    this.deviceFactory = new EnergyDeviceFactory();
    this.name = 'Smart Energy Management';
  }

  public initialize(): void {
    console.log('\n⚡ Initializing Energy Module...');
    this.createDefaultDevices();
    this.createDefaultZones();
    console.log('✅ Energy Module initialized\n');
  }

  private createDefaultDevices(): void {
    this.addMeter('meter-main', 'Main Grid Meter', 'Power Station');
    this.addMeter('meter-residential', 'Residential Meter', 'Residential District');
    this.addMeter('meter-commercial', 'Commercial Meter', 'Business District');
    this.addMeter('meter-industrial', 'Industrial Meter', 'Industrial Zone');
    this.addMeter('meter-public', 'Public Services Meter', 'City Services');
    this.addController('ctrl-main', 'Main Power Controller', 'Power Station');
    this.addController('ctrl-backup', 'Backup Controller', 'Backup Station');
    this.addRegulator('reg-residential', 'Residential Regulator', 'Residential District');
    this.addRegulator('reg-commercial', 'Commercial Regulator', 'Business District');
    this.addRegulator('reg-industrial', 'Industrial Regulator', 'Industrial Zone');
  }

  private createDefaultZones(): void {
    this.createZone('zone-residential', 'Residential', 
      { meters: ['meter-residential'], regulators: ['reg-residential'], maxCapacity: 15000, priority: 'high' });
    this.createZone('zone-commercial', 'Commercial', 
      { meters: ['meter-commercial'], regulators: ['reg-commercial'], maxCapacity: 20000, priority: 'medium' });
    this.createZone('zone-industrial', 'Industrial', 
      { meters: ['meter-industrial'], regulators: ['reg-industrial'], maxCapacity: 10000, priority: 'low' });
  }

  public addMeter(id: string, name: string, location: string): PowerMeter {
    const meter = this.deviceFactory.createSensor(id, name, location) as PowerMeter;
    this.meters.set(id, meter);
    this.addDevice(meter);
    return meter;
  }

  public addController(id: string, name: string, location: string): PowerController {
    const controller = this.deviceFactory.createController(id, name, location) as PowerController;
    this.controllers.set(id, controller);
    this.addDevice(controller);
    return controller;
  }

  public addRegulator(id: string, name: string, location: string): PowerRegulator {
    const regulator = this.deviceFactory.createActuator(id, name, location) as PowerRegulator;
    this.regulators.set(id, regulator);
    this.addDevice(regulator);
    return regulator;
  }

  public createZone(id: string, name: string, 
    config: { meters: string[]; regulators: string[]; maxCapacity: number; priority: 'high' | 'medium' | 'low' }): void {
    this.zones.set(id, { id, name, ...config });
    console.log(`🗺️  Power zone created: ${name}`);
  }

  public monitorConsumption(): Map<string, number> {
    console.log('\n📊 Monitoring power consumption...\n');
    const readings = new Map<string, number>();
    let totalConsumption = 0;

    this.meters.forEach((meter, id) => {
      meter.activate();
      const consumption = meter.readValue();
      readings.set(id, consumption);
      totalConsumption += consumption;
      console.log(`  ${meter.name}: ${consumption} ${meter.getUnit()}`);
    });

    console.log(`\n  Total: ${totalConsumption} kWh`);
    console.log(`  Capacity: ${((totalConsumption / this.maxCapacity) * 100).toFixed(1)}%`);

    if (totalConsumption > this.maxCapacity * this.alertThreshold) {
      const controller = CityController.getInstance();
      controller.createAlert('Energy Module', 
        `Power consumption at ${((totalConsumption / this.maxCapacity) * 100).toFixed(1)}%`, AlertLevel.HIGH);
    }

    this.usageHistory.push({ timestamp: new Date(), totalConsumption, savingMode: this.isSavingMode() });
    if (this.usageHistory.length > 100) this.usageHistory.shift();

    return readings;
  }

  public enableSolarPanels(): void {
    this.solarEnabled = true;
    this.solarOutput = Math.floor(Math.random() * 5000) + 2000;
    console.log(`☀️  Solar panels enabled. Output: ${this.solarOutput} kWh`);
  }

  public disableSolarPanels(): void {
    this.solarEnabled = false;
    this.solarOutput = 0;
    console.log('🌙 Solar panels disabled');
  }

  public balanceLoad(): void {
    console.log('\n⚖️  Balancing power load...');
    const totalConsumption = Array.from(this.meters.values()).reduce((sum, m) => sum + m.readValue(), 0);
    const availableCapacity = this.maxCapacity + (this.solarEnabled ? this.solarOutput : 0) - totalConsumption;
    
    if (availableCapacity < 0) {
      console.log('⚠️  Overload detected! Reducing power to low-priority zones');
      this.zones.forEach(zone => {
        if (zone.priority === 'low') {
          zone.regulators.forEach(regId => {
            const regulator = this.regulators.get(regId);
            if (regulator) regulator.setValue(50);
          });
        }
      });
    } else {
      console.log('✅ Power load is balanced');
      this.regulators.forEach(regulator => regulator.setValue(100));
    }
  }

  public activateEmergencyMode(): void {
    console.log('\n🆘 EMERGENCY MODE: Prioritizing critical systems');
    this.controllers.forEach(controller => { controller.activate(); controller.execute('emergency'); });
    this.zones.forEach(zone => {
      if (zone.priority !== 'high') {
        zone.regulators.forEach(regId => {
          const regulator = this.regulators.get(regId);
          if (regulator) regulator.setValue(30);
        });
      }
    });
  }

  public deactivateEmergencyMode(): void {
    console.log('\n✅ Returning to normal operation');
    this.controllers.forEach(controller => controller.execute('normal'));
    this.regulators.forEach(regulator => regulator.setValue(100));
  }

  public getUsageStatistics(): { average: number; peak: number; lowest: number; trend: string } {
    if (this.usageHistory.length === 0) return { average: 0, peak: 0, lowest: 0, trend: 'stable' };
    const consumptions = this.usageHistory.map(r => r.totalConsumption);
    const average = consumptions.reduce((a, b) => a + b, 0) / consumptions.length;
    const peak = Math.max(...consumptions);
    const lowest = Math.min(...consumptions);
    let trend = 'stable';
    if (consumptions.length >= 10) {
      const recent = consumptions.slice(-5).reduce((a, b) => a + b, 0) / 5;
      const older = consumptions.slice(-10, -5).reduce((a, b) => a + b, 0) / 5;
      if (recent > older * 1.1) trend = 'increasing';
      else if (recent < older * 0.9) trend = 'decreasing';
    }
    return { average, peak, lowest, trend };
  }

  public getModuleReport(): string {
    const stats = this.getUsageStatistics();
    const currentConsumption = Array.from(this.meters.values())
      .reduce((sum, m) => sum + (m.getStatus() === DeviceStatus.ACTIVE ? m.readValue() : 0), 0);
    return `
╔══════════════════════════════════════════╗
║          ENERGY MODULE REPORT            ║
╠══════════════════════════════════════════╣
║ Power Meters: ${String(this.meters.size).padEnd(25)}║
║ Controllers: ${String(this.controllers.size).padEnd(26)}║
║ Regulators: ${String(this.regulators.size).padEnd(27)}║
║ Zones: ${String(this.zones.size).padEnd(32)}║
║──────────────────────────────────────────║
║ Current Usage: ${String(currentConsumption + ' kWh').padEnd(24)}║
║ Max Capacity: ${String(this.maxCapacity + ' kWh').padEnd(25)}║
║ Solar: ${(this.solarEnabled ? `☀️  ${this.solarOutput} kWh` : '🌙 OFF').padEnd(32)}║
║ Saving Mode: ${(this.isSavingMode() ? '🌱 ON' : '⚡ OFF').padEnd(26)}║
║ Trend: ${String(stats.trend).padEnd(32)}║
║ Status: ${(this.isActive ? '🟢 Active' : '🔴 Inactive').padEnd(31)}║
╚══════════════════════════════════════════╝`;
  }

  public printUsageHistory(limit: number = 10): void {
    console.log('\n📈 Energy Usage History:');
    console.log('─'.repeat(50));
    const records = this.usageHistory.slice(-limit);
    records.forEach((record, index) => {
      const mode = record.savingMode ? '🌱' : '⚡';
      console.log(`${index + 1}. ${mode} ${record.timestamp.toISOString()} - ${record.totalConsumption} kWh`);
    });
    console.log('─'.repeat(50) + '\n');
  }
}
