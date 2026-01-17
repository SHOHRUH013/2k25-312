// SecurityProxy - Proxy pattern
// Kirish nazorati va logging

import { 
  ISubsystem, 
  IDevice, 
  SubsystemType, 
  IUser, 
  UserRole,
  IAccessControl
} from '../types';

// Access control implementation
export class SimpleAccessControl implements IAccessControl {
  private users: Map<string, { user: IUser; password: string }> = new Map();
  private permissions: Map<UserRole, Set<string>> = new Map([
    [UserRole.ADMIN, new Set(['read', 'write', 'delete', 'configure', 'start', 'stop'])],
    [UserRole.OPERATOR, new Set(['read', 'write', 'start', 'stop'])],
    [UserRole.VIEWER, new Set(['read'])]
  ]);

  constructor() {
    this.registerUser('admin', 'admin123', UserRole.ADMIN);
    this.registerUser('operator', 'oper123', UserRole.OPERATOR);
    this.registerUser('viewer', 'view123', UserRole.VIEWER);
  }

  registerUser(username: string, password: string, role: UserRole): void {
    const user: IUser = {
      id: `user-${Date.now()}-${Math.random().toString(36).substr(2, 5)}`,
      username,
      role
    };
    this.users.set(username, { user, password });
  }

  authenticate(username: string, password: string): IUser | null {
    const userData = this.users.get(username);
    if (userData && userData.password === password) {
      console.log(`✅ User '${username}' authenticated successfully`);
      return userData.user;
    }
    console.log(`❌ Authentication failed for '${username}'`);
    return null;
  }

  authorize(user: IUser, action: string): boolean {
    const allowedActions = this.permissions.get(user.role);
    if (allowedActions?.has(action)) return true;
    console.log(`🚫 User '${user.username}' not authorized for action '${action}'`);
    return false;
  }

  hasPermission(user: IUser, resource: string): boolean {
    if (user.role === UserRole.ADMIN) return true;
    return true;
  }
}

// Protection Proxy
export class SubsystemProtectionProxy implements ISubsystem {
  private realSubsystem: ISubsystem;
  private accessControl: IAccessControl;
  private currentUser: IUser | null = null;
  private accessLog: Array<{ timestamp: Date; user: string; action: string; allowed: boolean }> = [];

  public name: string;
  public type: SubsystemType;
  
  get isActive(): boolean {
    return this.realSubsystem.isActive;
  }

  constructor(subsystem: ISubsystem, accessControl: IAccessControl) {
    this.realSubsystem = subsystem;
    this.accessControl = accessControl;
    this.name = `Protected[${subsystem.name}]`;
    this.type = subsystem.type;
  }

  public login(username: string, password: string): boolean {
    this.currentUser = this.accessControl.authenticate(username, password);
    return this.currentUser !== null;
  }

  public logout(): void {
    if (this.currentUser) {
      console.log(`👋 User '${this.currentUser.username}' logged out`);
      this.currentUser = null;
    }
  }

  public getCurrentUser(): IUser | null {
    return this.currentUser;
  }

  public start(): void {
    if (!this.checkAccess('start')) {
      this.logAccess('start', false);
      throw new Error('Access denied: Cannot start subsystem');
    }
    this.logAccess('start', true);
    console.log(`🔐 Proxy: Authorized access to start ${this.realSubsystem.name}`);
    this.realSubsystem.start();
  }

  public stop(): void {
    if (!this.checkAccess('stop')) {
      this.logAccess('stop', false);
      throw new Error('Access denied: Cannot stop subsystem');
    }
    this.logAccess('stop', true);
    console.log(`🔐 Proxy: Authorized access to stop ${this.realSubsystem.name}`);
    this.realSubsystem.stop();
  }

  public getStatus(): string {
    if (!this.checkAccess('read')) {
      this.logAccess('read', false);
      return 'Access denied';
    }
    this.logAccess('read', true);
    return this.realSubsystem.getStatus();
  }

  public getDevices(): IDevice[] {
    if (!this.checkAccess('read')) {
      this.logAccess('read', false);
      return [];
    }
    this.logAccess('read', true);
    return this.realSubsystem.getDevices();
  }

  public addDevice(device: IDevice): void {
    if (!this.checkAccess('write')) {
      this.logAccess('write', false);
      throw new Error('Access denied: Cannot add device');
    }
    this.logAccess('write', true);
    console.log(`🔐 Proxy: Authorized access to add device to ${this.realSubsystem.name}`);
    this.realSubsystem.addDevice(device);
  }

  public removeDevice(deviceId: string): void {
    if (!this.checkAccess('delete')) {
      this.logAccess('delete', false);
      throw new Error('Access denied: Cannot remove device');
    }
    this.logAccess('delete', true);
    console.log(`🔐 Proxy: Authorized access to remove device from ${this.realSubsystem.name}`);
    this.realSubsystem.removeDevice(deviceId);
  }

  private checkAccess(action: string): boolean {
    if (!this.currentUser) {
      console.log('🚫 Proxy: No user logged in');
      return false;
    }
    return this.accessControl.authorize(this.currentUser, action);
  }

  private logAccess(action: string, allowed: boolean): void {
    this.accessLog.push({
      timestamp: new Date(),
      user: this.currentUser?.username || 'anonymous',
      action,
      allowed
    });
  }

  public getAccessLog(): Array<{ timestamp: Date; user: string; action: string; allowed: boolean }> {
    return [...this.accessLog];
  }

  public getUnderlyingSubsystem(): ISubsystem | null {
    if (this.currentUser?.role === UserRole.ADMIN) return this.realSubsystem;
    console.log('🚫 Proxy: Only admin can access underlying subsystem');
    return null;
  }
}

// Logging Proxy
export class SubsystemLoggingProxy implements ISubsystem {
  private realSubsystem: ISubsystem;
  private logs: Array<{ timestamp: Date; method: string; args?: unknown }> = [];

  public name: string;
  public type: SubsystemType;
  
  get isActive(): boolean {
    return this.realSubsystem.isActive;
  }

  constructor(subsystem: ISubsystem) {
    this.realSubsystem = subsystem;
    this.name = `Logged[${subsystem.name}]`;
    this.type = subsystem.type;
  }

  private log(method: string, args?: unknown): void {
    const entry = { timestamp: new Date(), method, args };
    this.logs.push(entry);
    console.log(`📝 [${entry.timestamp.toISOString()}] ${this.realSubsystem.name}.${method}(${args ? JSON.stringify(args) : ''})`);
  }

  public start(): void {
    this.log('start');
    this.realSubsystem.start();
  }

  public stop(): void {
    this.log('stop');
    this.realSubsystem.stop();
  }

  public getStatus(): string {
    this.log('getStatus');
    return this.realSubsystem.getStatus();
  }

  public getDevices(): IDevice[] {
    this.log('getDevices');
    return this.realSubsystem.getDevices();
  }

  public addDevice(device: IDevice): void {
    this.log('addDevice', { deviceId: device.id, deviceName: device.name });
    this.realSubsystem.addDevice(device);
  }

  public removeDevice(deviceId: string): void {
    this.log('removeDevice', { deviceId });
    this.realSubsystem.removeDevice(deviceId);
  }

  public getLogs(): Array<{ timestamp: Date; method: string; args?: unknown }> {
    return [...this.logs];
  }

  public clearLogs(): void {
    this.logs = [];
    console.log('🗑️  Logs cleared');
  }

  public printLogs(): void {
    console.log('\n📜 Subsystem Logs:');
    console.log('═'.repeat(60));
    this.logs.forEach((log, index) => {
      console.log(`${index + 1}. [${log.timestamp.toISOString()}] ${log.method}`);
      if (log.args) console.log(`   Args: ${JSON.stringify(log.args)}`);
    });
    console.log('═'.repeat(60) + '\n');
  }
}

// Caching Proxy
interface CacheEntry<T> {
  data: T;
  timestamp: number;
  ttl: number;
}

export class SubsystemCachingProxy implements ISubsystem {
  private realSubsystem: ISubsystem;
  private cache: Map<string, CacheEntry<unknown>> = new Map();
  private defaultTTL: number = 60000;

  public name: string;
  public type: SubsystemType;
  
  get isActive(): boolean {
    return this.realSubsystem.isActive;
  }

  constructor(subsystem: ISubsystem, ttlMs: number = 60000) {
    this.realSubsystem = subsystem;
    this.defaultTTL = ttlMs;
    this.name = `Cached[${subsystem.name}]`;
    this.type = subsystem.type;
  }

  private getFromCache<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) return null;
    const now = Date.now();
    if (now - entry.timestamp > entry.ttl) {
      this.cache.delete(key);
      console.log(`⏰ Cache expired: ${key}`);
      return null;
    }
    console.log(`📦 Cache hit: ${key}`);
    return entry.data as T;
  }

  private setCache<T>(key: string, data: T, ttl: number = this.defaultTTL): void {
    this.cache.set(key, { data, timestamp: Date.now(), ttl });
    console.log(`💾 Cached: ${key} (TTL: ${ttl}ms)`);
  }

  public start(): void {
    this.invalidateCache();
    this.realSubsystem.start();
  }

  public stop(): void {
    this.invalidateCache();
    this.realSubsystem.stop();
  }

  public getStatus(): string {
    const cacheKey = 'status';
    const cached = this.getFromCache<string>(cacheKey);
    if (cached !== null) return cached;
    const status = this.realSubsystem.getStatus();
    this.setCache(cacheKey, status, 5000);
    return status;
  }

  public getDevices(): IDevice[] {
    const cacheKey = 'devices';
    const cached = this.getFromCache<IDevice[]>(cacheKey);
    if (cached !== null) return cached;
    const devices = this.realSubsystem.getDevices();
    this.setCache(cacheKey, devices, 30000);
    return devices;
  }

  public addDevice(device: IDevice): void {
    this.invalidateCache('devices');
    this.realSubsystem.addDevice(device);
  }

  public removeDevice(deviceId: string): void {
    this.invalidateCache('devices');
    this.realSubsystem.removeDevice(deviceId);
  }

  public invalidateCache(key?: string): void {
    if (key) {
      this.cache.delete(key);
      console.log(`🗑️  Cache invalidated: ${key}`);
    } else {
      this.cache.clear();
      console.log('🗑️  All cache invalidated');
    }
  }

  public getCacheStats(): { entries: number; keys: string[] } {
    return { entries: this.cache.size, keys: Array.from(this.cache.keys()) };
  }
}

// Combined proxy factory
export function createSecureSubsystem(
  subsystem: ISubsystem,
  accessControl: IAccessControl,
  enableLogging: boolean = true,
  enableCaching: boolean = false,
  cacheTTL: number = 60000
): SubsystemProtectionProxy {
  let proxiedSubsystem: ISubsystem = subsystem;
  if (enableLogging) proxiedSubsystem = new SubsystemLoggingProxy(proxiedSubsystem);
  if (enableCaching) proxiedSubsystem = new SubsystemCachingProxy(proxiedSubsystem, cacheTTL);
  return new SubsystemProtectionProxy(proxiedSubsystem, accessControl);
}
