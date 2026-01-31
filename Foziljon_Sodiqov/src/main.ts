// SmartCity System - Main Entry Point
// Design Patterns: Singleton, Factory, Abstract Factory, Builder, Adapter, Proxy

import * as readline from 'readline';
import { 
  CityController, SystemConfigBuilder, ConfigDirector, SubsystemFactory,
  SimpleAccessControl, createSecureSubsystem, LegacyWeatherAdapter, 
  TrafficDataAdapter, SubsystemType
} from './core';
import { TransportModule, LightingModule, SecurityModule, EnergyModule } from './modules';

class SmartCityApp {
  private controller: CityController;
  private rl: readline.Interface;
  private accessControl: SimpleAccessControl;
  private isLoggedIn: boolean = false;
  private currentUsername: string = '';

  private transportModule: TransportModule;
  private lightingModule: LightingModule;
  private securityModule: SecurityModule;
  private energyModule: EnergyModule;

  private weatherAdapter: LegacyWeatherAdapter;
  private trafficAdapter: TrafficDataAdapter;

  constructor() {
    this.rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    this.controller = CityController.getInstance();
    this.accessControl = new SimpleAccessControl();

    this.transportModule = new TransportModule();
    this.lightingModule = new LightingModule();
    this.securityModule = new SecurityModule();
    this.energyModule = new EnergyModule();

    this.weatherAdapter = new LegacyWeatherAdapter('API-KEY-12345');
    this.trafficAdapter = new TrafficDataAdapter('https://traffic.api.example.com');
  }

  public async run(): Promise<void> {
    this.printWelcome();
    await this.initializeSystem();
    await this.mainMenu();
  }

  private printWelcome(): void {
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║   🏙️  SMARTCITY - Intelligent City Management System          ║
║                        Version 1.0.0                          ║
╚═══════════════════════════════════════════════════════════════╝
    `);
  }

  private async initializeSystem(): Promise<void> {
    console.log('\n🔧 Initializing SmartCity System...\n');

    // Builder pattern
    const configBuilder = new SystemConfigBuilder();
    const director = new ConfigDirector(configBuilder);
    const config = director.buildFullConfig('Tashkent Smart City');
    this.controller.setConfig(config);

    // Factory pattern
    this.transportModule.initialize();
    this.lightingModule.initialize();
    this.securityModule.initialize();
    this.energyModule.initialize();

    this.controller.registerSubsystem(this.transportModule);
    this.controller.registerSubsystem(this.lightingModule);
    this.controller.registerSubsystem(this.securityModule);
    this.controller.registerSubsystem(this.energyModule);

    // Adapter pattern
    await this.weatherAdapter.connect();
    await this.trafficAdapter.connect();

    console.log('\n✅ System initialization complete!\n');
  }

  private async mainMenu(): Promise<void> {
    while (true) {
      const choice = await this.showMainMenu();
      switch (choice) {
        case '1': await this.login(); break;
        case '2': this.showSystemStatus(); break;
        case '3': await this.transportMenu(); break;
        case '4': await this.lightingMenu(); break;
        case '5': await this.securityMenu(); break;
        case '6': await this.energyMenu(); break;
        case '7': await this.externalServicesMenu(); break;
        case '8': await this.systemControlMenu(); break;
        case '9': await this.demonstratePatterns(); break;
        case '0': await this.shutdown(); return;
        default: console.log('❌ Invalid option');
      }
    }
  }

  private showMainMenu(): Promise<string> {
    const loginStatus = this.isLoggedIn ? `🔓 ${this.currentUsername}` : '🔒 Not logged in';
    const systemStatus = this.controller.isSystemRunning() ? '🟢 Running' : '🔴 Stopped';

    console.log(`
╔═══════════════════════════════════════╗
║          SMARTCITY MAIN MENU          ║
╠═══════════════════════════════════════╣
║ ${loginStatus.padEnd(37)}║
║ System: ${systemStatus.padEnd(29)}║
╠═══════════════════════════════════════╣
║ 1. 🔐 Login / Logout                  ║
║ 2. 📊 System Status                   ║
║ 3. 🚗 Transport Management            ║
║ 4. 💡 Lighting Management             ║
║ 5. 🔒 Security Management             ║
║ 6. ⚡ Energy Management               ║
║ 7. 🌐 External Services               ║
║ 8. ⚙️  System Control                  ║
║ 9. 📖 Demonstrate Design Patterns     ║
║ 0. 🚪 Exit                            ║
╚═══════════════════════════════════════╝
    `);
    return this.prompt('Select option: ');
  }

  private async login(): Promise<void> {
    if (this.isLoggedIn) {
      console.log(`\n👋 Logging out ${this.currentUsername}...`);
      this.isLoggedIn = false;
      this.currentUsername = '';
      return;
    }
    console.log('\n🔐 Users: admin/admin123, operator/oper123, viewer/view123\n');
    const username = await this.prompt('Username: ');
    const password = await this.prompt('Password: ');
    const user = this.accessControl.authenticate(username, password);
    if (user) {
      this.isLoggedIn = true;
      this.currentUsername = user.username;
      console.log(`\n✅ Welcome, ${user.username}! (Role: ${user.role})`);
    } else {
      console.log('\n❌ Login failed');
    }
  }

  private showSystemStatus(): void {
    console.log(this.controller.getSystemStatus());
    this.controller.showAllSubsystemsStatus();
    console.log('\n📊 Module Reports:\n');
    console.log(this.transportModule.getModuleReport());
    console.log(this.lightingModule.getModuleReport());
    console.log(this.securityModule.getModuleReport());
    console.log(this.energyModule.getModuleReport());
  }

  private async transportMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║        TRANSPORT MANAGEMENT           ║
╠═══════════════════════════════════════╣
║ 1. 📊 View Status    4. 🚨 Emergency  ║
║ 2. 🚦 Traffic Lights 5. 🚧 Barrier    ║
║ 3. 📈 Monitor        0. ⬅️  Back       ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1': console.log(this.transportModule.getModuleReport()); break;
        case '2': this.transportModule.listTrafficLights(); break;
        case '3': this.transportModule.monitorTraffic(); break;
        case '4': 
          const em = await this.prompt('Enable emergency? (y/n): ');
          this.transportModule.setEmergencyMode(em.toLowerCase() === 'y'); 
          break;
        case '5':
          const bid = await this.prompt('Barrier ID: ');
          const lvl = await this.prompt('Open %: ');
          this.transportModule.controlBarrier(bid, parseInt(lvl) || 0);
          break;
        case '0': return;
      }
    }
  }

  private async lightingMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║         LIGHTING MANAGEMENT           ║
╠═══════════════════════════════════════╣
║ 1. 📊 Status     4. 🌙 Off All       ║
║ 2. 🗺️  Zones      5. 🔄 Auto Adjust   ║
║ 3. 💡 On All     0. ⬅️  Back          ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1': console.log(this.lightingModule.getModuleReport()); break;
        case '2': this.lightingModule.listZones(); break;
        case '3': this.lightingModule.turnOnAllLights(); break;
        case '4': this.lightingModule.turnOffAllLights(); break;
        case '5': this.lightingModule.autoAdjustBrightness(); break;
        case '0': return;
      }
    }
  }

  private async securityMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║         SECURITY MANAGEMENT           ║
╠═══════════════════════════════════════╣
║ 1. 📊 Status     5. 👁️  Scan Motion   ║
║ 2. 📹 Cameras    6. 🚨 Lockdown      ║
║ 3. 🔒 Arm        7. ✅ End Lockdown  ║
║ 4. 🔓 Disarm     0. ⬅️  Back          ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1': console.log(this.securityModule.getModuleReport()); break;
        case '2': this.securityModule.activateAllCameras(); break;
        case '3': this.securityModule.armAllAlarms(); break;
        case '4': this.securityModule.disarmAllAlarms(); break;
        case '5': this.securityModule.scanForMotion(); break;
        case '6': this.securityModule.activateLockdown(); break;
        case '7': this.securityModule.deactivateLockdown(); break;
        case '0': return;
      }
    }
  }

  private async energyMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║          ENERGY MANAGEMENT            ║
╠═══════════════════════════════════════╣
║ 1. 📊 Status     5. ☀️  Solar On      ║
║ 2. 📈 Monitor    6. 🌙 Solar Off     ║
║ 3. 🌱 Save On    7. ⚖️  Balance       ║
║ 4. ⚡ Save Off   0. ⬅️  Back          ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1': console.log(this.energyModule.getModuleReport()); break;
        case '2': this.energyModule.monitorConsumption(); break;
        case '3': this.energyModule.enableSavingMode(); break;
        case '4': this.energyModule.disableSavingMode(); break;
        case '5': this.energyModule.enableSolarPanels(); break;
        case '6': this.energyModule.disableSolarPanels(); break;
        case '7': this.energyModule.balanceLoad(); break;
        case '0': return;
      }
    }
  }

  private async externalServicesMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║         EXTERNAL SERVICES             ║
╠═══════════════════════════════════════╣
║ 1. 🌡️  Temperature  4. 🚗 Traffic     ║
║ 2. 💧 Humidity     5. 🚦 Congestion  ║
║ 3. 📊 Forecast     0. ⬅️  Back        ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1':
          const temp = await this.weatherAdapter.getTemperature();
          console.log(`\n🌡️  Temperature: ${temp}°C\n`);
          break;
        case '2':
          const hum = await this.weatherAdapter.getHumidity();
          console.log(`\n💧 Humidity: ${hum}%\n`);
          break;
        case '3':
          const fc = await this.weatherAdapter.getForecast();
          console.log(`\n📊 Forecast: ${fc.temperature}°C, ${fc.condition}\n`);
          break;
        case '4':
          const loc = await this.prompt('Location: ');
          const cnt = await this.trafficAdapter.getVehicleCount(loc);
          console.log(`\n🚗 Vehicles: ${cnt}\n`);
          break;
        case '5':
          const l = await this.prompt('Location: ');
          const cng = await this.trafficAdapter.getCongestionPercentage(l);
          console.log(`\n🚦 Congestion: ${cng}%\n`);
          break;
        case '0': return;
      }
    }
  }

  private async systemControlMenu(): Promise<void> {
    while (true) {
      console.log(`
╔═══════════════════════════════════════╗
║          SYSTEM CONTROL               ║
╠═══════════════════════════════════════╣
║ 1. 🚀 Start System                    ║
║ 2. 🛑 Stop System                     ║
║ 3. 📋 View Alerts                     ║
║ 0. ⬅️  Back                            ║
╚═══════════════════════════════════════╝
      `);
      const choice = await this.prompt('Select: ');
      switch (choice) {
        case '1': this.controller.startSystem(); break;
        case '2': this.controller.stopSystem(); break;
        case '3':
          const alerts = this.controller.getActiveAlerts();
          if (alerts.length === 0) console.log('\n✅ No active alerts\n');
          else alerts.forEach((a, i) => console.log(`${i + 1}. [${a.level}] ${a.message}`));
          break;
        case '0': return;
      }
    }
  }

  private async demonstratePatterns(): Promise<void> {
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║            DESIGN PATTERNS DEMONSTRATION                      ║
╠═══════════════════════════════════════════════════════════════╣
║ 1. SINGLETON  - CityController (bitta instance)              ║
║ 2. FACTORY    - SubsystemFactory (subsystem yaratish)        ║
║ 3. ABSTRACT FACTORY - DeviceFactory (qurilmalar oilasi)      ║
║ 4. BUILDER    - SystemConfigBuilder (konfiguratsiya)         ║
║ 5. ADAPTER    - WeatherAdapter (tashqi xizmatlar)            ║
║ 6. PROXY      - SecurityProxy (kirish nazorati)              ║
╚═══════════════════════════════════════════════════════════════╝
    `);

    // Singleton demo
    console.log('\n1️⃣ SINGLETON:');
    const c1 = CityController.getInstance();
    const c2 = CityController.getInstance();
    console.log(`   c1 === c2: ${c1 === c2}`);

    // Factory demo
    console.log('\n2️⃣ FACTORY METHOD:');
    const factory = new SubsystemFactory();
    factory.createSubsystem(SubsystemType.TRANSPORT);

    // Builder demo
    console.log('\n3️⃣ BUILDER:');
    const builder = new SystemConfigBuilder();
    builder.setCityName('Demo City').enableSubsystem(SubsystemType.TRANSPORT).preview();

    // Adapter demo
    console.log('\n4️⃣ ADAPTER:');
    const temp = await this.weatherAdapter.getTemperature();
    console.log(`   Adapted temperature: ${temp}°C`);

    // Proxy demo
    console.log('\n5️⃣ PROXY:');
    const { TransportSubsystem } = await import('./core/factories/SubsystemFactory');
    const sub = new TransportSubsystem();
    const secSub = createSecureSubsystem(sub, this.accessControl);
    console.log('   Without login:');
    try { secSub.start(); } catch (e) { console.log(`   ❌ ${(e as Error).message}`); }
    console.log('   With admin login:');
    secSub.login('admin', 'admin123');
    secSub.start();
    secSub.logout();

    await this.prompt('\nPress Enter to continue...');
  }

  private async shutdown(): Promise<void> {
    console.log('\n🛑 Shutting down...');
    this.controller.stopSystem();
    await this.weatherAdapter.disconnect();
    await this.trafficAdapter.disconnect();
    console.log('\n👋 Goodbye!\n');
    this.rl.close();
  }

  private prompt(question: string): Promise<string> {
    return new Promise(resolve => this.rl.question(question, resolve));
  }
}

const app = new SmartCityApp();
app.run().catch(console.error);
