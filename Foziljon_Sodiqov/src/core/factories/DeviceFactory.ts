// DeviceFactory - Abstract Factory pattern
// Qurilmalar yaratish uchun

import { 
  IDevice, 
  ISensor, 
  IController, 
  IActuator,
  DeviceType, 
  DeviceStatus,
  SubsystemType 
} from '../types';

// Abstract Factory interface
export interface IDeviceFactory {
  createSensor(id: string, name: string, location: string): ISensor;
  createController(id: string, name: string, location: string): IController;
  createActuator(id: string, name: string, location: string): IActuator;
}

// Base device class
abstract class BaseDevice implements IDevice {
  id: string;
  name: string;
  type: DeviceType;
  status: DeviceStatus;
  location: string;

  constructor(id: string, name: string, type: DeviceType, location: string) {
    this.id = id;
    this.name = name;
    this.type = type;
    this.status = DeviceStatus.INACTIVE;
    this.location = location;
  }

  activate(): void {
    this.status = DeviceStatus.ACTIVE;
    console.log(`✅ ${this.name} activated`);
  }

  deactivate(): void {
    this.status = DeviceStatus.INACTIVE;
    console.log(`⏹️ ${this.name} deactivated`);
  }

  getStatus(): DeviceStatus {
    return this.status;
  }

  getInfo(): string {
    return `[${this.type}] ${this.name} (${this.id}) - ${this.status} @ ${this.location}`;
  }
}

// Transport devices
export class TrafficSensor extends BaseDevice implements ISensor {
  private vehicleCount: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.SENSOR, location);
  }

  readValue(): number {
    this.vehicleCount = Math.floor(Math.random() * 100);
    return this.vehicleCount;
  }

  getUnit(): string {
    return 'vehicles/min';
  }

  calibrate(): void {
    console.log(`🔧 Calibrating traffic sensor: ${this.name}`);
    this.vehicleCount = 0;
  }
}

export class TrafficLightController extends BaseDevice implements IController {
  private currentPhase: string = 'red';

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.CONTROLLER, location);
  }

  execute(command: string): void {
    switch (command.toLowerCase()) {
      case 'green':
        this.currentPhase = 'green';
        console.log(`🟢 Traffic light ${this.name}: GREEN`);
        break;
      case 'yellow':
        this.currentPhase = 'yellow';
        console.log(`🟡 Traffic light ${this.name}: YELLOW`);
        break;
      case 'red':
        this.currentPhase = 'red';
        console.log(`🔴 Traffic light ${this.name}: RED`);
        break;
      default:
        console.log(`Unknown command: ${command}`);
    }
  }

  getCommands(): string[] {
    return ['green', 'yellow', 'red'];
  }

  getCurrentPhase(): string {
    return this.currentPhase;
  }
}

export class TrafficBarrier extends BaseDevice implements IActuator {
  private position: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.ACTUATOR, location);
  }

  setValue(value: number): void {
    this.position = Math.max(0, Math.min(100, value));
    console.log(`🚧 Barrier ${this.name}: ${this.position}% open`);
  }

  getValue(): number {
    return this.position;
  }

  getRange(): { min: number; max: number } {
    return { min: 0, max: 100 };
  }
}

// Lighting devices
export class LightSensor extends BaseDevice implements ISensor {
  private luxLevel: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.SENSOR, location);
  }

  readValue(): number {
    this.luxLevel = Math.floor(Math.random() * 10000);
    return this.luxLevel;
  }

  getUnit(): string {
    return 'lux';
  }

  calibrate(): void {
    console.log(`🔧 Calibrating light sensor: ${this.name}`);
  }
}

export class LightController extends BaseDevice implements IController {
  private isOn: boolean = false;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.CONTROLLER, location);
  }

  execute(command: string): void {
    switch (command.toLowerCase()) {
      case 'on':
        this.isOn = true;
        console.log(`💡 Light ${this.name}: ON`);
        break;
      case 'off':
        this.isOn = false;
        console.log(`🌑 Light ${this.name}: OFF`);
        break;
      case 'toggle':
        this.isOn = !this.isOn;
        console.log(`💡 Light ${this.name}: ${this.isOn ? 'ON' : 'OFF'}`);
        break;
      default:
        console.log(`Unknown command: ${command}`);
    }
  }

  getCommands(): string[] {
    return ['on', 'off', 'toggle'];
  }
}

export class Dimmer extends BaseDevice implements IActuator {
  private brightness: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.ACTUATOR, location);
  }

  setValue(value: number): void {
    this.brightness = Math.max(0, Math.min(100, value));
    console.log(`💡 Dimmer ${this.name}: ${this.brightness}%`);
  }

  getValue(): number {
    return this.brightness;
  }

  getRange(): { min: number; max: number } {
    return { min: 0, max: 100 };
  }
}

// Security devices
export class SecurityCamera extends BaseDevice implements ISensor {
  private motionDetected: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.SENSOR, location);
  }

  readValue(): number {
    this.motionDetected = Math.random() > 0.7 ? 1 : 0;
    return this.motionDetected;
  }

  getUnit(): string {
    return 'motion (0/1)';
  }

  calibrate(): void {
    console.log(`🔧 Calibrating security camera: ${this.name}`);
  }
}

export class AlarmController extends BaseDevice implements IController {
  private isArmed: boolean = false;
  private isTriggered: boolean = false;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.CONTROLLER, location);
  }

  execute(command: string): void {
    switch (command.toLowerCase()) {
      case 'arm':
        this.isArmed = true;
        console.log(`🔒 Alarm ${this.name}: ARMED`);
        break;
      case 'disarm':
        this.isArmed = false;
        this.isTriggered = false;
        console.log(`🔓 Alarm ${this.name}: DISARMED`);
        break;
      case 'trigger':
        if (this.isArmed) {
          this.isTriggered = true;
          console.log(`🚨 Alarm ${this.name}: TRIGGERED!`);
        }
        break;
      case 'reset':
        this.isTriggered = false;
        console.log(`✅ Alarm ${this.name}: RESET`);
        break;
      default:
        console.log(`Unknown command: ${command}`);
    }
  }

  getCommands(): string[] {
    return ['arm', 'disarm', 'trigger', 'reset'];
  }
}

export class SecurityGate extends BaseDevice implements IActuator {
  private openPercentage: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.ACTUATOR, location);
  }

  setValue(value: number): void {
    this.openPercentage = Math.max(0, Math.min(100, value));
    console.log(`🚪 Gate ${this.name}: ${this.openPercentage}% open`);
  }

  getValue(): number {
    return this.openPercentage;
  }

  getRange(): { min: number; max: number } {
    return { min: 0, max: 100 };
  }
}

// Energy devices
export class PowerMeter extends BaseDevice implements ISensor {
  private consumption: number = 0;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.SENSOR, location);
  }

  readValue(): number {
    this.consumption = Math.floor(Math.random() * 500) + 100;
    return this.consumption;
  }

  getUnit(): string {
    return 'kWh';
  }

  calibrate(): void {
    console.log(`🔧 Calibrating power meter: ${this.name}`);
  }
}

export class PowerController extends BaseDevice implements IController {
  private powerState: 'normal' | 'saving' | 'emergency' = 'normal';

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.CONTROLLER, location);
  }

  execute(command: string): void {
    switch (command.toLowerCase()) {
      case 'normal':
        this.powerState = 'normal';
        console.log(`⚡ Power ${this.name}: NORMAL mode`);
        break;
      case 'saving':
        this.powerState = 'saving';
        console.log(`🌱 Power ${this.name}: SAVING mode`);
        break;
      case 'emergency':
        this.powerState = 'emergency';
        console.log(`🆘 Power ${this.name}: EMERGENCY mode`);
        break;
      default:
        console.log(`Unknown command: ${command}`);
    }
  }

  getCommands(): string[] {
    return ['normal', 'saving', 'emergency'];
  }
}

export class PowerRegulator extends BaseDevice implements IActuator {
  private outputLevel: number = 100;

  constructor(id: string, name: string, location: string) {
    super(id, name, DeviceType.ACTUATOR, location);
  }

  setValue(value: number): void {
    this.outputLevel = Math.max(0, Math.min(100, value));
    console.log(`⚡ Regulator ${this.name}: ${this.outputLevel}% output`);
  }

  getValue(): number {
    return this.outputLevel;
  }

  getRange(): { min: number; max: number } {
    return { min: 0, max: 100 };
  }
}

// Concrete factories
export class TransportDeviceFactory implements IDeviceFactory {
  createSensor(id: string, name: string, location: string): ISensor {
    console.log(`🏭 Creating Traffic Sensor: ${name}`);
    return new TrafficSensor(id, name, location);
  }

  createController(id: string, name: string, location: string): IController {
    console.log(`🏭 Creating Traffic Light Controller: ${name}`);
    return new TrafficLightController(id, name, location);
  }

  createActuator(id: string, name: string, location: string): IActuator {
    console.log(`🏭 Creating Traffic Barrier: ${name}`);
    return new TrafficBarrier(id, name, location);
  }
}

export class LightingDeviceFactory implements IDeviceFactory {
  createSensor(id: string, name: string, location: string): ISensor {
    console.log(`🏭 Creating Light Sensor: ${name}`);
    return new LightSensor(id, name, location);
  }

  createController(id: string, name: string, location: string): IController {
    console.log(`🏭 Creating Light Controller: ${name}`);
    return new LightController(id, name, location);
  }

  createActuator(id: string, name: string, location: string): IActuator {
    console.log(`🏭 Creating Dimmer: ${name}`);
    return new Dimmer(id, name, location);
  }
}

export class SecurityDeviceFactory implements IDeviceFactory {
  createSensor(id: string, name: string, location: string): ISensor {
    console.log(`🏭 Creating Security Camera: ${name}`);
    return new SecurityCamera(id, name, location);
  }

  createController(id: string, name: string, location: string): IController {
    console.log(`🏭 Creating Alarm Controller: ${name}`);
    return new AlarmController(id, name, location);
  }

  createActuator(id: string, name: string, location: string): IActuator {
    console.log(`🏭 Creating Security Gate: ${name}`);
    return new SecurityGate(id, name, location);
  }
}

export class EnergyDeviceFactory implements IDeviceFactory {
  createSensor(id: string, name: string, location: string): ISensor {
    console.log(`🏭 Creating Power Meter: ${name}`);
    return new PowerMeter(id, name, location);
  }

  createController(id: string, name: string, location: string): IController {
    console.log(`🏭 Creating Power Controller: ${name}`);
    return new PowerController(id, name, location);
  }

  createActuator(id: string, name: string, location: string): IActuator {
    console.log(`🏭 Creating Power Regulator: ${name}`);
    return new PowerRegulator(id, name, location);
  }
}

// Factory provider
export class DeviceFactoryProvider {
  static getFactory(subsystemType: SubsystemType): IDeviceFactory {
    switch (subsystemType) {
      case SubsystemType.TRANSPORT:
        return new TransportDeviceFactory();
      case SubsystemType.LIGHTING:
        return new LightingDeviceFactory();
      case SubsystemType.SECURITY:
        return new SecurityDeviceFactory();
      case SubsystemType.ENERGY:
        return new EnergyDeviceFactory();
      default:
        throw new Error(`Unknown subsystem type: ${subsystemType}`);
    }
  }
}
