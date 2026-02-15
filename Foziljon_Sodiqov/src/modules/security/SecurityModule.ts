// Security Module - shahar xavfsizlik tizimi

import { DeviceStatus, AlertLevel } from '../../core/types';
import { SecuritySubsystem } from '../../core/factories/SubsystemFactory';
import { SecurityDeviceFactory, SecurityCamera, AlarmController, SecurityGate } from '../../core/factories/DeviceFactory';
import { CityController } from '../../core/singleton/CityController';

interface SecurityIncident {
  id: string;
  timestamp: Date;
  type: 'motion' | 'intrusion' | 'alarm' | 'access';
  location: string;
  description: string;
  resolved: boolean;
}

export class SecurityModule extends SecuritySubsystem {
  private deviceFactory: SecurityDeviceFactory;
  private cameras: Map<string, SecurityCamera> = new Map();
  private alarms: Map<string, AlarmController> = new Map();
  private gates: Map<string, SecurityGate> = new Map();
  private incidents: SecurityIncident[] = [];
  private lockdownMode: boolean = false;

  constructor() {
    super();
    this.deviceFactory = new SecurityDeviceFactory();
    this.name = 'City Security System';
  }

  public initialize(): void {
    console.log('\n🔒 Initializing Security Module...');
    this.createDefaultDevices();
    console.log('✅ Security Module initialized\n');
  }

  private createDefaultDevices(): void {
    this.addCamera('cam-main-1', 'Main Entrance Camera', 'City Hall Entrance');
    this.addCamera('cam-main-2', 'Lobby Camera', 'City Hall Lobby');
    this.addCamera('cam-park-1', 'Park Camera North', 'Central Park North');
    this.addCamera('cam-park-2', 'Park Camera South', 'Central Park South');
    this.addCamera('cam-parking', 'Parking Lot Camera', 'Underground Parking');
    this.addAlarm('alarm-main', 'Main Building Alarm', 'City Hall');
    this.addAlarm('alarm-park', 'Park Alarm', 'Central Park');
    this.addAlarm('alarm-parking', 'Parking Alarm', 'Underground Parking');
    this.addGate('gate-main', 'Main Gate', 'City Hall Main Entrance');
    this.addGate('gate-parking', 'Parking Gate', 'Underground Parking Entry');
    this.addGate('gate-service', 'Service Gate', 'Service Area');
  }

  public addCamera(id: string, name: string, location: string): SecurityCamera {
    const camera = this.deviceFactory.createSensor(id, name, location) as SecurityCamera;
    this.cameras.set(id, camera);
    this.addDevice(camera);
    return camera;
  }

  public addAlarm(id: string, name: string, location: string): AlarmController {
    const alarm = this.deviceFactory.createController(id, name, location) as AlarmController;
    this.alarms.set(id, alarm);
    this.addDevice(alarm);
    return alarm;
  }

  public addGate(id: string, name: string, location: string): SecurityGate {
    const gate = this.deviceFactory.createActuator(id, name, location) as SecurityGate;
    this.gates.set(id, gate);
    this.addDevice(gate);
    return gate;
  }

  public activateAllCameras(): void {
    console.log('\n📹 Activating all security cameras...');
    this.cameras.forEach(camera => camera.activate());
  }

  public armAllAlarms(): void {
    console.log('\n🔒 Arming all alarms...');
    this.alarms.forEach(alarm => { alarm.activate(); alarm.execute('arm'); });
  }

  public disarmAllAlarms(): void {
    console.log('\n🔓 Disarming all alarms...');
    this.alarms.forEach(alarm => alarm.execute('disarm'));
  }

  public activateLockdown(): void {
    console.log('\n🚨🔒 LOCKDOWN MODE ACTIVATED 🔒🚨');
    this.lockdownMode = true;
    this.gates.forEach(gate => { gate.activate(); gate.setValue(0); });
    this.armAllAlarms();
    this.activateAllCameras();
    const controller = CityController.getInstance();
    controller.createAlert('Security Module', 'LOCKDOWN MODE ACTIVATED', AlertLevel.CRITICAL);
  }

  public deactivateLockdown(): void {
    console.log('\n✅ Lockdown mode deactivated');
    this.lockdownMode = false;
    this.gates.forEach(gate => gate.setValue(100));
    this.disarmAllAlarms();
  }

  public scanForMotion(): SecurityIncident[] {
    console.log('\n👁️  Scanning for motion...');
    const detectedIncidents: SecurityIncident[] = [];

    this.cameras.forEach((camera, id) => {
      if (camera.getStatus() !== DeviceStatus.ACTIVE) camera.activate();
      if (camera.readValue() === 1) {
        const incident: SecurityIncident = {
          id: `INC-${Date.now()}-${Math.random().toString(36).substr(2, 5)}`,
          timestamp: new Date(),
          type: 'motion',
          location: camera.location,
          description: `Motion detected by ${camera.name}`,
          resolved: false
        };
        this.incidents.push(incident);
        detectedIncidents.push(incident);
        console.log(`🚨 Motion detected at ${camera.location}!`);
      }
    });

    if (detectedIncidents.length === 0) console.log('✅ No motion detected');
    return detectedIncidents;
  }

  public controlGate(gateId: string, openPercentage: number): boolean {
    if (this.lockdownMode && openPercentage > 0) {
      console.log('🚫 Cannot open gate during lockdown');
      return false;
    }
    const gate = this.gates.get(gateId);
    if (gate) { gate.activate(); gate.setValue(openPercentage); return true; }
    console.log(`❌ Gate not found: ${gateId}`);
    return false;
  }

  public getIncidents(resolved?: boolean): SecurityIncident[] {
    if (resolved === undefined) return [...this.incidents];
    return this.incidents.filter(i => i.resolved === resolved);
  }

  public resolveIncident(incidentId: string): boolean {
    const incident = this.incidents.find(i => i.id === incidentId);
    if (incident) { incident.resolved = true; console.log(`✅ Incident ${incidentId} resolved`); return true; }
    return false;
  }

  public getModuleReport(): string {
    const activeCameras = Array.from(this.cameras.values()).filter(c => c.getStatus() === DeviceStatus.ACTIVE).length;
    const unresolvedIncidents = this.incidents.filter(i => !i.resolved).length;
    return `
╔══════════════════════════════════════════╗
║         SECURITY MODULE REPORT           ║
╠══════════════════════════════════════════╣
║ Cameras: ${String(this.cameras.size).padEnd(30)}║
║ Active Cameras: ${String(activeCameras).padEnd(23)}║
║ Alarms: ${String(this.alarms.size).padEnd(31)}║
║ Gates: ${String(this.gates.size).padEnd(32)}║
║ Unresolved Incidents: ${String(unresolvedIncidents).padEnd(17)}║
║ Lockdown: ${(this.lockdownMode ? '🔒 ACTIVE' : '🔓 OFF').padEnd(29)}║
║ Status: ${(this.isActive ? '🟢 Active' : '🔴 Inactive').padEnd(31)}║
╚══════════════════════════════════════════╝`;
  }

  public listIncidents(): void {
    console.log('\n📋 Security Incidents:');
    console.log('─'.repeat(60));
    if (this.incidents.length === 0) { console.log('  No incidents recorded'); }
    else {
      this.incidents.forEach((incident, index) => {
        const status = incident.resolved ? '✅' : '🔴';
        console.log(`${index + 1}. ${status} [${incident.type.toUpperCase()}] ${incident.id}`);
        console.log(`      Location: ${incident.location} | ${incident.description}`);
      });
    }
    console.log('─'.repeat(60) + '\n');
  }
}
