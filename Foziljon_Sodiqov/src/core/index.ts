// SmartCity Core exports

export * from './types';
export { CityController } from './singleton/CityController';

export { 
  SubsystemFactory,
  BaseSubsystem,
  TransportSubsystem,
  LightingSubsystem,
  SecuritySubsystem,
  EnergySubsystem
} from './factories/SubsystemFactory';

export {
  IDeviceFactory,
  DeviceFactoryProvider,
  TransportDeviceFactory,
  LightingDeviceFactory,
  SecurityDeviceFactory,
  EnergyDeviceFactory,
  TrafficSensor,
  TrafficLightController,
  TrafficBarrier,
  LightSensor,
  LightController,
  Dimmer,
  SecurityCamera,
  AlarmController,
  SecurityGate,
  PowerMeter,
  PowerController,
  PowerRegulator
} from './factories/DeviceFactory';

export {
  ISystemConfigBuilder,
  SystemConfigBuilder,
  ConfigDirector
} from './builders/SystemConfigBuilder';

export {
  LegacyWeatherAPI,
  ModernWeatherREST,
  LegacyWeatherAdapter,
  ModernWeatherAdapter,
  ExternalTrafficAPI,
  ITrafficService,
  TrafficDataAdapter,
  LegacyEmergencySystem,
  IEmergencyService,
  EmergencyServiceAdapter
} from './adapters/ExternalServiceAdapter';

export {
  SimpleAccessControl,
  SubsystemProtectionProxy,
  SubsystemLoggingProxy,
  SubsystemCachingProxy,
  createSecureSubsystem
} from './proxy/SecurityProxy';
