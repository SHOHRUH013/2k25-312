// ExternalServiceAdapter - Adapter pattern
// Tashqi xizmatlar bilan integratsiya

import { IWeatherService, WeatherForecast, IExternalService } from '../types';

// Legacy Weather API (tashqi xizmat)
export class LegacyWeatherAPI {
  private apiKey: string;
  private connected: boolean = false;

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  connectToServer(): boolean {
    console.log(`🌐 Legacy Weather API: Connecting with key ${this.apiKey.substring(0, 4)}****`);
    this.connected = true;
    return true;
  }

  disconnectFromServer(): void {
    console.log('🌐 Legacy Weather API: Disconnected');
    this.connected = false;
  }

  fetchCurrentTemperatureCelsius(): number {
    if (!this.connected) throw new Error('Not connected to weather server');
    return Math.floor(Math.random() * 35) - 5;
  }

  fetchCurrentHumidityPercent(): number {
    if (!this.connected) throw new Error('Not connected to weather server');
    return Math.floor(Math.random() * 60) + 30;
  }

  fetchWeatherForecastData(): { date: string; temp: number; hum: number; cond: string } {
    if (!this.connected) throw new Error('Not connected to weather server');
    const conditions = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy'];
    return {
      date: new Date(Date.now() + 86400000).toISOString(),
      temp: Math.floor(Math.random() * 35) - 5,
      hum: Math.floor(Math.random() * 60) + 30,
      cond: conditions[Math.floor(Math.random() * conditions.length)]
    };
  }
}

// Modern Weather REST API
export class ModernWeatherREST {
  private endpoint: string;
  private isOnline: boolean = false;

  constructor(endpoint: string) {
    this.endpoint = endpoint;
  }

  async initialize(): Promise<{ success: boolean; message: string }> {
    console.log(`🌐 Modern Weather REST: Initializing at ${this.endpoint}`);
    this.isOnline = true;
    return { success: true, message: 'Connected' };
  }

  async shutdown(): Promise<void> {
    console.log('🌐 Modern Weather REST: Shutting down');
    this.isOnline = false;
  }

  async getWeatherData(): Promise<{
    temperature: { value: number; unit: 'C' | 'F' };
    humidity: { value: number; unit: '%' };
    forecast: { timestamp: number; temp: number; humidity: number; weather: string };
  }> {
    if (!this.isOnline) throw new Error('Service not initialized');
    const conditions = ['Clear', 'Partly Cloudy', 'Rain', 'Snow', 'Fog'];
    return {
      temperature: { value: Math.floor(Math.random() * 35) - 5, unit: 'C' },
      humidity: { value: Math.floor(Math.random() * 60) + 30, unit: '%' },
      forecast: {
        timestamp: Date.now() + 86400000,
        temp: Math.floor(Math.random() * 35) - 5,
        humidity: Math.floor(Math.random() * 60) + 30,
        weather: conditions[Math.floor(Math.random() * conditions.length)]
      }
    };
  }
}

// Adapter for Legacy Weather API
export class LegacyWeatherAdapter implements IWeatherService {
  private legacyApi: LegacyWeatherAPI;
  private _isConnected: boolean = false;

  constructor(apiKey: string) {
    this.legacyApi = new LegacyWeatherAPI(apiKey);
  }

  async connect(): Promise<boolean> {
    try {
      const result = this.legacyApi.connectToServer();
      this._isConnected = result;
      console.log('✅ LegacyWeatherAdapter: Connection adapted');
      return result;
    } catch (error) {
      console.error('❌ LegacyWeatherAdapter: Connection failed');
      return false;
    }
  }

  async disconnect(): Promise<void> {
    this.legacyApi.disconnectFromServer();
    this._isConnected = false;
    console.log('✅ LegacyWeatherAdapter: Disconnection adapted');
  }

  isConnected(): boolean {
    return this._isConnected;
  }

  async getTemperature(): Promise<number> {
    const temp = this.legacyApi.fetchCurrentTemperatureCelsius();
    console.log(`🌡️  Adapter: Temperature adapted: ${temp}°C`);
    return temp;
  }

  async getHumidity(): Promise<number> {
    const humidity = this.legacyApi.fetchCurrentHumidityPercent();
    console.log(`💧 Adapter: Humidity adapted: ${humidity}%`);
    return humidity;
  }

  async getForecast(): Promise<WeatherForecast> {
    const legacyData = this.legacyApi.fetchWeatherForecastData();
    const forecast: WeatherForecast = {
      date: new Date(legacyData.date),
      temperature: legacyData.temp,
      humidity: legacyData.hum,
      condition: legacyData.cond
    };
    console.log('📊 Adapter: Forecast data adapted');
    return forecast;
  }
}

// Adapter for Modern Weather REST
export class ModernWeatherAdapter implements IWeatherService {
  private modernApi: ModernWeatherREST;
  private connected: boolean = false;

  constructor(endpoint: string) {
    this.modernApi = new ModernWeatherREST(endpoint);
  }

  async connect(): Promise<boolean> {
    const result = await this.modernApi.initialize();
    this.connected = result.success;
    console.log('✅ ModernWeatherAdapter: Connection adapted');
    return this.connected;
  }

  async disconnect(): Promise<void> {
    await this.modernApi.shutdown();
    this.connected = false;
    console.log('✅ ModernWeatherAdapter: Disconnection adapted');
  }

  isConnected(): boolean {
    return this.connected;
  }

  async getTemperature(): Promise<number> {
    const data = await this.modernApi.getWeatherData();
    console.log(`🌡️  Adapter: Temperature adapted: ${data.temperature.value}°C`);
    return data.temperature.value;
  }

  async getHumidity(): Promise<number> {
    const data = await this.modernApi.getWeatherData();
    console.log(`💧 Adapter: Humidity adapted: ${data.humidity.value}%`);
    return data.humidity.value;
  }

  async getForecast(): Promise<WeatherForecast> {
    const data = await this.modernApi.getWeatherData();
    const forecast: WeatherForecast = {
      date: new Date(data.forecast.timestamp),
      temperature: data.forecast.temp,
      humidity: data.forecast.humidity,
      condition: data.forecast.weather
    };
    console.log('📊 Adapter: Forecast data adapted');
    return forecast;
  }
}

// Traffic API
export class ExternalTrafficAPI {
  private url: string;
  private active: boolean = false;

  constructor(url: string) {
    this.url = url;
  }

  open(): void {
    console.log(`🌐 Traffic API: Opening connection to ${this.url}`);
    this.active = true;
  }

  close(): void {
    console.log('🌐 Traffic API: Closing connection');
    this.active = false;
  }

  getVehicleCount(sectorId: string): number {
    if (!this.active) return 0;
    return Math.floor(Math.random() * 500);
  }

  getAverageSpeed(sectorId: string): number {
    if (!this.active) return 0;
    return Math.floor(Math.random() * 60) + 20;
  }

  getCongestionLevel(sectorId: string): 'low' | 'medium' | 'high' | 'critical' {
    if (!this.active) return 'low';
    const levels: ('low' | 'medium' | 'high' | 'critical')[] = ['low', 'medium', 'high', 'critical'];
    return levels[Math.floor(Math.random() * levels.length)];
  }
}

// Traffic service interface
export interface ITrafficService extends IExternalService {
  getVehicleCount(location: string): Promise<number>;
  getAverageSpeed(location: string): Promise<number>;
  getCongestionPercentage(location: string): Promise<number>;
}

// Traffic adapter
export class TrafficDataAdapter implements ITrafficService {
  private externalApi: ExternalTrafficAPI;
  private connected: boolean = false;

  constructor(apiUrl: string) {
    this.externalApi = new ExternalTrafficAPI(apiUrl);
  }

  async connect(): Promise<boolean> {
    this.externalApi.open();
    this.connected = true;
    console.log('✅ TrafficDataAdapter: Connected');
    return true;
  }

  async disconnect(): Promise<void> {
    this.externalApi.close();
    this.connected = false;
    console.log('✅ TrafficDataAdapter: Disconnected');
  }

  isConnected(): boolean {
    return this.connected;
  }

  async getVehicleCount(location: string): Promise<number> {
    const count = this.externalApi.getVehicleCount(location);
    console.log(`🚗 Adapter: Vehicle count for ${location}: ${count}`);
    return count;
  }

  async getAverageSpeed(location: string): Promise<number> {
    const speed = this.externalApi.getAverageSpeed(location);
    console.log(`🚗 Adapter: Average speed for ${location}: ${speed} km/h`);
    return speed;
  }

  async getCongestionPercentage(location: string): Promise<number> {
    const level = this.externalApi.getCongestionLevel(location);
    const percentageMap: Record<string, number> = { 'low': 25, 'medium': 50, 'high': 75, 'critical': 95 };
    const percentage = percentageMap[level] || 0;
    console.log(`🚗 Adapter: Congestion for ${location}: ${percentage}% (${level})`);
    return percentage;
  }
}

// Emergency system
export class LegacyEmergencySystem {
  private systemId: string;
  private online: boolean = false;

  constructor(systemId: string) {
    this.systemId = systemId;
  }

  powerOn(): boolean {
    console.log(`🚨 Emergency System ${this.systemId}: Powering on`);
    this.online = true;
    return true;
  }

  powerOff(): void {
    console.log(`🚨 Emergency System ${this.systemId}: Powering off`);
    this.online = false;
  }

  sendAlertCode(code: number, message: string): boolean {
    if (!this.online) return false;
    console.log(`🚨 Emergency Alert [Code ${code}]: ${message}`);
    return true;
  }

  requestBackup(type: 'police' | 'fire' | 'medical', location: string): string {
    if (!this.online) return 'SYSTEM_OFFLINE';
    const ticket = `EM-${Date.now()}`;
    console.log(`🚨 Backup requested: ${type} to ${location} [${ticket}]`);
    return ticket;
  }
}

// Emergency service interface
export interface IEmergencyService extends IExternalService {
  sendAlert(level: string, message: string): Promise<boolean>;
  requestAssistance(type: string, location: string): Promise<string>;
}

// Emergency adapter
export class EmergencyServiceAdapter implements IEmergencyService {
  private legacySystem: LegacyEmergencySystem;
  private connected: boolean = false;

  constructor(systemId: string) {
    this.legacySystem = new LegacyEmergencySystem(systemId);
  }

  async connect(): Promise<boolean> {
    this.connected = this.legacySystem.powerOn();
    console.log('✅ EmergencyServiceAdapter: Connected');
    return this.connected;
  }

  async disconnect(): Promise<void> {
    this.legacySystem.powerOff();
    this.connected = false;
    console.log('✅ EmergencyServiceAdapter: Disconnected');
  }

  isConnected(): boolean {
    return this.connected;
  }

  async sendAlert(level: string, message: string): Promise<boolean> {
    const codeMap: Record<string, number> = { 'low': 100, 'medium': 200, 'high': 300, 'critical': 999 };
    const code = codeMap[level.toLowerCase()] || 100;
    const result = this.legacySystem.sendAlertCode(code, message);
    console.log(`📢 Adapter: Alert sent with code ${code}`);
    return result;
  }

  async requestAssistance(type: string, location: string): Promise<string> {
    const typeMap: Record<string, 'police' | 'fire' | 'medical'> = {
      'security': 'police', 'fire': 'fire', 'medical': 'medical', 'accident': 'police', 'emergency': 'medical'
    };
    const legacyType = typeMap[type.toLowerCase()] || 'police';
    const ticket = this.legacySystem.requestBackup(legacyType, location);
    console.log(`📢 Adapter: Assistance requested, ticket: ${ticket}`);
    return ticket;
  }
}
