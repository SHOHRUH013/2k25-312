// SystemConfigBuilder - Builder pattern
// Tizim konfiguratsiyasini yaratish

import { 
  ISystemConfig, 
  SubsystemType, 
  SubsystemConfig, 
  AlertThresholds 
} from '../types';

// Builder interface
export interface ISystemConfigBuilder {
  setCityName(name: string): ISystemConfigBuilder;
  setTimezone(timezone: string): ISystemConfigBuilder;
  enableSubsystem(type: SubsystemType, settings?: Record<string, unknown>): ISystemConfigBuilder;
  disableSubsystem(type: SubsystemType): ISystemConfigBuilder;
  enableAllSubsystems(): ISystemConfigBuilder;
  setEnergySavingMode(enabled: boolean): ISystemConfigBuilder;
  setAlertThresholds(thresholds: Partial<AlertThresholds>): ISystemConfigBuilder;
  setTemperatureThresholds(min: number, max: number): ISystemConfigBuilder;
  setMaxEnergyConsumption(max: number): ISystemConfigBuilder;
  setMaxTrafficLevel(max: number): ISystemConfigBuilder;
  setSubsystemSettings(type: SubsystemType, settings: Record<string, unknown>): ISystemConfigBuilder;
  build(): ISystemConfig;
  reset(): ISystemConfigBuilder;
  preview(): void;
}

// Builder implementation
export class SystemConfigBuilder implements ISystemConfigBuilder {
  private cityName: string = 'SmartCity';
  private timezone: string = 'UTC';
  private subsystems: Map<SubsystemType, SubsystemConfig> = new Map();
  private energySavingMode: boolean = false;
  private alertThresholds: AlertThresholds = {
    temperature: { min: -20, max: 45 },
    energy: { max: 10000 },
    traffic: { max: 90 }
  };

  constructor() {
    Object.values(SubsystemType).forEach(type => {
      this.subsystems.set(type, { type, enabled: false, settings: {} });
    });
  }

  public setCityName(name: string): ISystemConfigBuilder {
    this.cityName = name;
    console.log(`🏙️  Builder: City name set to "${name}"`);
    return this;
  }

  public setTimezone(timezone: string): ISystemConfigBuilder {
    this.timezone = timezone;
    console.log(`🕐 Builder: Timezone set to "${timezone}"`);
    return this;
  }

  public enableSubsystem(type: SubsystemType, settings: Record<string, unknown> = {}): ISystemConfigBuilder {
    this.subsystems.set(type, { type, enabled: true, settings });
    console.log(`✅ Builder: ${type} subsystem enabled`);
    return this;
  }

  public disableSubsystem(type: SubsystemType): ISystemConfigBuilder {
    const config = this.subsystems.get(type);
    if (config) {
      config.enabled = false;
      this.subsystems.set(type, config);
    }
    console.log(`⏹️  Builder: ${type} subsystem disabled`);
    return this;
  }

  public enableAllSubsystems(): ISystemConfigBuilder {
    Object.values(SubsystemType).forEach(type => {
      this.enableSubsystem(type);
    });
    console.log(`✅ Builder: All subsystems enabled`);
    return this;
  }

  public setEnergySavingMode(enabled: boolean): ISystemConfigBuilder {
    this.energySavingMode = enabled;
    console.log(`🌱 Builder: Energy saving mode ${enabled ? 'enabled' : 'disabled'}`);
    return this;
  }

  public setAlertThresholds(thresholds: Partial<AlertThresholds>): ISystemConfigBuilder {
    if (thresholds.temperature) {
      this.alertThresholds.temperature = { ...this.alertThresholds.temperature, ...thresholds.temperature };
    }
    if (thresholds.energy) {
      this.alertThresholds.energy = { ...this.alertThresholds.energy, ...thresholds.energy };
    }
    if (thresholds.traffic) {
      this.alertThresholds.traffic = { ...this.alertThresholds.traffic, ...thresholds.traffic };
    }
    console.log(`⚙️  Builder: Alert thresholds updated`);
    return this;
  }

  public setTemperatureThresholds(min: number, max: number): ISystemConfigBuilder {
    this.alertThresholds.temperature = { min, max };
    console.log(`🌡️  Builder: Temperature thresholds set (${min}°C - ${max}°C)`);
    return this;
  }

  public setMaxEnergyConsumption(max: number): ISystemConfigBuilder {
    this.alertThresholds.energy = { max };
    console.log(`⚡ Builder: Max energy consumption set to ${max} kWh`);
    return this;
  }

  public setMaxTrafficLevel(max: number): ISystemConfigBuilder {
    this.alertThresholds.traffic = { max };
    console.log(`🚗 Builder: Max traffic level set to ${max}%`);
    return this;
  }

  public setSubsystemSettings(type: SubsystemType, settings: Record<string, unknown>): ISystemConfigBuilder {
    const config = this.subsystems.get(type);
    if (config) {
      config.settings = { ...config.settings, ...settings };
      this.subsystems.set(type, config);
    }
    console.log(`⚙️  Builder: ${type} settings updated`);
    return this;
  }

  public build(): ISystemConfig {
    console.log(`\n🏗️  Building configuration for "${this.cityName}"...`);
    
    const config: ISystemConfig = {
      cityName: this.cityName,
      timezone: this.timezone,
      subsystems: Array.from(this.subsystems.values()),
      energySavingMode: this.energySavingMode,
      alertThresholds: { ...this.alertThresholds }
    };

    console.log(`✅ Configuration built successfully!\n`);
    return config;
  }

  public reset(): ISystemConfigBuilder {
    this.cityName = 'SmartCity';
    this.timezone = 'UTC';
    this.energySavingMode = false;
    this.alertThresholds = {
      temperature: { min: -20, max: 45 },
      energy: { max: 10000 },
      traffic: { max: 90 }
    };
    
    Object.values(SubsystemType).forEach(type => {
      this.subsystems.set(type, { type, enabled: false, settings: {} });
    });

    console.log(`🔄 Builder: Reset to defaults`);
    return this;
  }

  public preview(): void {
    console.log('\n📋 Configuration Preview:');
    console.log('─'.repeat(40));
    console.log(`City: ${this.cityName}`);
    console.log(`Timezone: ${this.timezone}`);
    console.log(`Energy Saving: ${this.energySavingMode ? 'ON' : 'OFF'}`);
    console.log('\nSubsystems:');
    this.subsystems.forEach((config, type) => {
      console.log(`  ${type}: ${config.enabled ? '✅ Enabled' : '❌ Disabled'}`);
    });
    console.log('─'.repeat(40) + '\n');
  }
}

// Director - oldindan tayyor konfiguratsiyalar
export class ConfigDirector {
  private builder: SystemConfigBuilder;

  constructor(builder: SystemConfigBuilder) {
    this.builder = builder;
  }

  public buildMinimalConfig(cityName: string): ISystemConfig {
    return this.builder
      .reset()
      .setCityName(cityName)
      .enableSubsystem(SubsystemType.TRANSPORT)
      .enableSubsystem(SubsystemType.LIGHTING)
      .setEnergySavingMode(true)
      .build();
  }

  public buildFullConfig(cityName: string): ISystemConfig {
    return this.builder
      .reset()
      .setCityName(cityName)
      .setTimezone('Asia/Tashkent')
      .enableAllSubsystems()
      .setEnergySavingMode(false)
      .setTemperatureThresholds(-10, 40)
      .setMaxEnergyConsumption(15000)
      .setMaxTrafficLevel(85)
      .build();
  }

  public buildEcoConfig(cityName: string): ISystemConfig {
    return this.builder
      .reset()
      .setCityName(cityName)
      .enableAllSubsystems()
      .setEnergySavingMode(true)
      .setMaxEnergyConsumption(5000)
      .setSubsystemSettings(SubsystemType.LIGHTING, { autoDimming: true, maxBrightness: 70 })
      .setSubsystemSettings(SubsystemType.ENERGY, { solarPanelsEnabled: true })
      .build();
  }

  public buildSecurityConfig(cityName: string): ISystemConfig {
    return this.builder
      .reset()
      .setCityName(cityName)
      .enableSubsystem(SubsystemType.SECURITY, { alertLevel: 'high', autoLock: true, recordingEnabled: true })
      .enableSubsystem(SubsystemType.LIGHTING, { alwaysOn: true })
      .enableSubsystem(SubsystemType.ENERGY)
      .setSubsystemSettings(SubsystemType.SECURITY, { motionDetection: true, facialRecognition: true })
      .build();
  }
}
