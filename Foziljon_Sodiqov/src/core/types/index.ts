// SmartCity System - Core Types

export enum SubsystemType {
  TRANSPORT = 'transport',
  LIGHTING = 'lighting',
  SECURITY = 'security',
  ENERGY = 'energy'
}

export enum DeviceType {
  SENSOR = 'sensor',
  CONTROLLER = 'controller',
  ACTUATOR = 'actuator'
}

export enum DeviceStatus {
  ACTIVE = 'active',
  INACTIVE = 'inactive',
  MAINTENANCE = 'maintenance',
  ERROR = 'error'
}

export enum AlertLevel {
  LOW = 'low',
  MEDIUM = 'medium',
  HIGH = 'high',
  CRITICAL = 'critical'
}

// Device interface
export interface IDevice {
  id: string;
  name: string;
  type: DeviceType;
  status: DeviceStatus;
  location: string;
  activate(): void;
  deactivate(): void;
  getStatus(): DeviceStatus;
  getInfo(): string;
}

// Subsystem interface
export interface ISubsystem {
  name: string;
  type: SubsystemType;
  isActive: boolean;
  start(): void;
  stop(): void;
  getStatus(): string;
  getDevices(): IDevice[];
  addDevice(device: IDevice): void;
  removeDevice(deviceId: string): void;
}

// Sensor interface
export interface ISensor extends IDevice {
  readValue(): number;
  getUnit(): string;
  calibrate(): void;
}

// Controller interface
export interface IController extends IDevice {
  execute(command: string): void;
  getCommands(): string[];
}

// Actuator interface
export interface IActuator extends IDevice {
  setValue(value: number): void;
  getValue(): number;
  getRange(): { min: number; max: number };
}

// Event types
export interface IEvent {
  id: string;
  timestamp: Date;
  source: string;
  type: string;
  data: Record<string, unknown>;
}

export interface IAlert extends IEvent {
  level: AlertLevel;
  message: string;
  acknowledged: boolean;
}

export interface IEventHandler {
  handle(event: IEvent): void;
}

// Configuration types
export interface ISystemConfig {
  cityName: string;
  timezone: string;
  subsystems: SubsystemConfig[];
  energySavingMode: boolean;
  alertThresholds: AlertThresholds;
}

export interface SubsystemConfig {
  type: SubsystemType;
  enabled: boolean;
  settings: Record<string, unknown>;
}

export interface AlertThresholds {
  temperature: { min: number; max: number };
  energy: { max: number };
  traffic: { max: number };
}

// External service types
export interface IExternalService {
  connect(): Promise<boolean>;
  disconnect(): Promise<void>;
  isConnected(): boolean;
}

export interface IWeatherService extends IExternalService {
  getTemperature(): Promise<number>;
  getHumidity(): Promise<number>;
  getForecast(): Promise<WeatherForecast>;
}

export interface WeatherForecast {
  date: Date;
  temperature: number;
  humidity: number;
  condition: string;
}

// Access control
export enum UserRole {
  ADMIN = 'admin',
  OPERATOR = 'operator',
  VIEWER = 'viewer'
}

export interface IUser {
  id: string;
  username: string;
  role: UserRole;
}

export interface IAccessControl {
  authenticate(username: string, password: string): IUser | null;
  authorize(user: IUser, action: string): boolean;
  hasPermission(user: IUser, resource: string): boolean;
}
