// CityController - Singleton pattern
// Markaziy boshqaruv tizimi

import { 
  ISubsystem, 
  ISystemConfig, 
  SubsystemType, 
  IAlert, 
  AlertLevel,
  IEvent 
} from '../types';

export class CityController {
  private static instance: CityController | null = null;
  private subsystems: Map<SubsystemType, ISubsystem> = new Map();
  private config: ISystemConfig | null = null;
  private alerts: IAlert[] = [];
  private eventLog: IEvent[] = [];
  private isRunning: boolean = false;

  private constructor() {
    console.log('🏙️  CityController initialized');
  }

  // Singleton instance
  public static getInstance(): CityController {
    if (!CityController.instance) {
      CityController.instance = new CityController();
    }
    return CityController.instance;
  }

  public static resetInstance(): void {
    CityController.instance = null;
  }

  // Tizimni ishga tushirish
  public startSystem(): void {
    if (this.isRunning) {
      console.log('⚠️  System is already running');
      return;
    }

    console.log('\n🚀 Starting SmartCity System...\n');
    
    this.subsystems.forEach((subsystem, type) => {
      try {
        subsystem.start();
        console.log(`✅ ${type} subsystem started`);
      } catch (error) {
        console.log(`❌ Failed to start ${type} subsystem`);
        this.createAlert(type, `Failed to start ${type} subsystem`, AlertLevel.HIGH);
      }
    });

    this.isRunning = true;
    console.log('\n🏙️  SmartCity System is now running!\n');
  }

  // Tizimni to'xtatish
  public stopSystem(): void {
    if (!this.isRunning) {
      console.log('⚠️  System is not running');
      return;
    }

    console.log('\n🛑 Stopping SmartCity System...\n');
    
    this.subsystems.forEach((subsystem, type) => {
      try {
        subsystem.stop();
        console.log(`⏹️  ${type} subsystem stopped`);
      } catch (error) {
        console.log(`❌ Error stopping ${type} subsystem`);
      }
    });

    this.isRunning = false;
    console.log('\n🏙️  SmartCity System stopped\n');
  }

  // Tizim holatini olish
  public getSystemStatus(): string {
    const status = this.isRunning ? '🟢 Running' : '🔴 Stopped';
    const subsystemCount = this.subsystems.size;
    const activeAlerts = this.alerts.filter(a => !a.acknowledged).length;

    return `
╔════════════════════════════════════════╗
║         SMARTCITY SYSTEM STATUS        ║
╠════════════════════════════════════════╣
║ Status: ${status.padEnd(30)}║
║ City: ${(this.config?.cityName || 'Not configured').padEnd(32)}║
║ Subsystems: ${String(subsystemCount).padEnd(26)}║
║ Active Alerts: ${String(activeAlerts).padEnd(23)}║
╚════════════════════════════════════════╝
    `;
  }

  // Barcha subsystemlar holatini ko'rsatish
  public showAllSubsystemsStatus(): void {
    console.log('\n📊 Subsystems Status:\n');
    console.log('─'.repeat(50));
    
    if (this.subsystems.size === 0) {
      console.log('No subsystems registered');
      return;
    }

    this.subsystems.forEach((subsystem, type) => {
      const status = subsystem.isActive ? '🟢 Active' : '🔴 Inactive';
      const deviceCount = subsystem.getDevices().length;
      console.log(`${type.toUpperCase()}`);
      console.log(`  Status: ${status}`);
      console.log(`  Devices: ${deviceCount}`);
      console.log('─'.repeat(50));
    });
  }

  // Subsystem qo'shish
  public registerSubsystem(subsystem: ISubsystem): void {
    this.subsystems.set(subsystem.type, subsystem);
    this.logEvent({
      id: this.generateId(),
      timestamp: new Date(),
      source: 'CityController',
      type: 'SUBSYSTEM_REGISTERED',
      data: { subsystemType: subsystem.type, name: subsystem.name }
    });
    console.log(`📦 Registered subsystem: ${subsystem.name}`);
  }

  public getSubsystem(type: SubsystemType): ISubsystem | undefined {
    return this.subsystems.get(type);
  }

  public getAllSubsystems(): ISubsystem[] {
    return Array.from(this.subsystems.values());
  }

  // Konfiguratsiya
  public setConfig(config: ISystemConfig): void {
    this.config = config;
    console.log(`⚙️  Configuration set for city: ${config.cityName}`);
  }

  public getConfig(): ISystemConfig | null {
    return this.config;
  }

  // Alert management
  public createAlert(source: string, message: string, level: AlertLevel): void {
    const alert: IAlert = {
      id: this.generateId(),
      timestamp: new Date(),
      source,
      type: 'ALERT',
      data: {},
      level,
      message,
      acknowledged: false
    };
    
    this.alerts.push(alert);
    this.printAlert(alert);
  }

  public acknowledgeAlert(alertId: string): boolean {
    const alert = this.alerts.find(a => a.id === alertId);
    if (alert) {
      alert.acknowledged = true;
      return true;
    }
    return false;
  }

  public getActiveAlerts(): IAlert[] {
    return this.alerts.filter(a => !a.acknowledged);
  }

  public getAllAlerts(): IAlert[] {
    return [...this.alerts];
  }

  // Event logging
  public logEvent(event: IEvent): void {
    this.eventLog.push(event);
  }

  public getEventLog(): IEvent[] {
    return [...this.eventLog];
  }

  // Helper methods
  private generateId(): string {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  private printAlert(alert: IAlert): void {
    const icons: Record<AlertLevel, string> = {
      [AlertLevel.LOW]: '📢',
      [AlertLevel.MEDIUM]: '⚠️',
      [AlertLevel.HIGH]: '🚨',
      [AlertLevel.CRITICAL]: '🆘'
    };
    
    console.log(`\n${icons[alert.level]} [${alert.level.toUpperCase()}] ${alert.message}`);
    console.log(`   Source: ${alert.source} | Time: ${alert.timestamp.toISOString()}\n`);
  }

  public isSystemRunning(): boolean {
    return this.isRunning;
  }
}
