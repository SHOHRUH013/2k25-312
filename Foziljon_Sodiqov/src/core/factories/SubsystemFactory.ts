// SubsystemFactory - Factory Method pattern
// Subsystemlar yaratish uchun

import { ISubsystem, SubsystemType, IDevice, DeviceStatus, DeviceType } from '../types';

// Base class for subsystems
export abstract class BaseSubsystem implements ISubsystem {
  public name: string;
  public type: SubsystemType;
  public isActive: boolean = false;
  protected devices: IDevice[] = [];

  constructor(name: string, type: SubsystemType) {
    this.name = name;
    this.type = type;
  }

  public start(): void {
    this.isActive = true;
    console.log(`🟢 ${this.name} subsystem started`);
  }

  public stop(): void {
    this.isActive = false;
    console.log(`🔴 ${this.name} subsystem stopped`);
  }

  public getStatus(): string {
    return this.isActive ? 'Active' : 'Inactive';
  }

  public getDevices(): IDevice[] {
    return [...this.devices];
  }

  public addDevice(device: IDevice): void {
    this.devices.push(device);
    console.log(`📱 Device "${device.name}" added to ${this.name}`);
  }

  public removeDevice(deviceId: string): void {
    const index = this.devices.findIndex(d => d.id === deviceId);
    if (index !== -1) {
      const removed = this.devices.splice(index, 1)[0];
      console.log(`📱 Device "${removed.name}" removed from ${this.name}`);
    }
  }

  abstract performMainFunction(): void;
}

// Transport subsystem
export class TransportSubsystem extends BaseSubsystem {
  private trafficLevel: number = 0;

  constructor() {
    super('Transport Management', SubsystemType.TRANSPORT);
  }

  public performMainFunction(): void {
    console.log('🚗 Managing city traffic...');
    this.updateTrafficLevel();
  }

  public updateTrafficLevel(): void {
    this.trafficLevel = Math.floor(Math.random() * 100);
    console.log(`🚦 Current traffic level: ${this.trafficLevel}%`);
  }

  public getTrafficLevel(): number {
    return this.trafficLevel;
  }

  public optimizeTrafficLights(): void {
    console.log('🚦 Optimizing traffic light timings...');
  }
}

// Lighting subsystem
export class LightingSubsystem extends BaseSubsystem {
  private brightnessLevel: number = 100;
  private autoMode: boolean = true;

  constructor() {
    super('Street Lighting', SubsystemType.LIGHTING);
  }

  public performMainFunction(): void {
    console.log('💡 Managing street lighting...');
    if (this.autoMode) {
      this.adjustBrightness();
    }
  }

  public setBrightness(level: number): void {
    this.brightnessLevel = Math.max(0, Math.min(100, level));
    console.log(`💡 Brightness set to: ${this.brightnessLevel}%`);
  }

  public getBrightness(): number {
    return this.brightnessLevel;
  }

  public setAutoMode(enabled: boolean): void {
    this.autoMode = enabled;
    console.log(`🔄 Auto mode: ${enabled ? 'ON' : 'OFF'}`);
  }

  private adjustBrightness(): void {
    const hour = new Date().getHours();
    if (hour >= 6 && hour < 18) {
      this.brightnessLevel = 30;
    } else if (hour >= 18 && hour < 22) {
      this.brightnessLevel = 100;
    } else {
      this.brightnessLevel = 50;
    }
    console.log(`💡 Auto-adjusted brightness: ${this.brightnessLevel}%`);
  }
}

// Security subsystem
export class SecuritySubsystem extends BaseSubsystem {
  private alertMode: boolean = false;
  private camerasActive: number = 0;

  constructor() {
    super('City Security', SubsystemType.SECURITY);
  }

  public performMainFunction(): void {
    console.log('🔒 Monitoring city security...');
    this.scanForThreats();
  }

  public activateAlertMode(): void {
    this.alertMode = true;
    console.log('🚨 ALERT MODE ACTIVATED');
  }

  public deactivateAlertMode(): void {
    this.alertMode = false;
    console.log('✅ Alert mode deactivated');
  }

  public isAlertMode(): boolean {
    return this.alertMode;
  }

  public getActiveCameras(): number {
    return this.camerasActive;
  }

  private scanForThreats(): void {
    this.camerasActive = this.devices.filter(
      d => d.status === DeviceStatus.ACTIVE && d.type === DeviceType.SENSOR
    ).length;
    console.log(`📹 Active security cameras: ${this.camerasActive}`);
  }
}

// Energy subsystem
export class EnergySubsystem extends BaseSubsystem {
  private currentConsumption: number = 0;
  private savingMode: boolean = false;

  constructor() {
    super('Energy Management', SubsystemType.ENERGY);
  }

  public performMainFunction(): void {
    console.log('⚡ Managing energy consumption...');
    this.monitorConsumption();
  }

  public enableSavingMode(): void {
    this.savingMode = true;
    console.log('🌱 Energy saving mode: ON');
  }

  public disableSavingMode(): void {
    this.savingMode = false;
    console.log('⚡ Energy saving mode: OFF');
  }

  public isSavingMode(): boolean {
    return this.savingMode;
  }

  public getCurrentConsumption(): number {
    return this.currentConsumption;
  }

  public monitorConsumption(): void {
    this.currentConsumption = Math.floor(Math.random() * 1000) + 500;
    console.log(`⚡ Current consumption: ${this.currentConsumption} kWh`);
  }

  public getEnergyReport(): string {
    return `
    ⚡ Energy Report
    ─────────────────
    Current: ${this.currentConsumption} kWh
    Saving Mode: ${this.savingMode ? 'ON' : 'OFF'}
    Devices: ${this.devices.length}
    `;
  }
}

// Factory class
export class SubsystemFactory {
  public createSubsystem(type: SubsystemType): ISubsystem {
    switch (type) {
      case SubsystemType.TRANSPORT:
        console.log('🏭 Factory: Creating Transport Subsystem');
        return new TransportSubsystem();
      
      case SubsystemType.LIGHTING:
        console.log('🏭 Factory: Creating Lighting Subsystem');
        return new LightingSubsystem();
      
      case SubsystemType.SECURITY:
        console.log('🏭 Factory: Creating Security Subsystem');
        return new SecuritySubsystem();
      
      case SubsystemType.ENERGY:
        console.log('🏭 Factory: Creating Energy Subsystem');
        return new EnergySubsystem();
      
      default:
        throw new Error(`Unknown subsystem type: ${type}`);
    }
  }

  public createAllSubsystems(): Map<SubsystemType, ISubsystem> {
    const subsystems = new Map<SubsystemType, ISubsystem>();
    Object.values(SubsystemType).forEach(type => {
      subsystems.set(type, this.createSubsystem(type));
    });
    return subsystems;
  }
}
