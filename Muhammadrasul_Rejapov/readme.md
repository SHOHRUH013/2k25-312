# SmartCity System

## 📖 Loyiha haqida

**SmartCity System** – bu konsol orqali ishlaydigan loyiha bo‘lib, u shahar infratuzilmasini boshqarish uchun mo‘ljallangan.  
Loyiha quyidagi modullarni o‘z ichiga oladi:  

- **Lighting (osveshcheniye)** – shahar chiroqlari va yo‘l yoritilishi.  
- **Transport** – transport tizimi va svetoforlar ishlashini boshqarish.  
- **Energy** – energiya sarfini monitoring qilish va optimizatsiya.  
- **Security** – xavfsizlik tizimi va kirishni nazorat qilish.

Har bir modul mustaqil ishlaydi, ammo **SmartCityController** orqali barchasi birlashtirilgan va boshqariladi.

## 🏗️ Loyiha tuzilmasi

smartcity/
├── SmartCity.App
│ ├── Controller
│ │ └── SmartCityController.cs
│ ├── Factories
│ │ └── ModuleFactory.cs
│ ├── Proxy
│ │ └── SecurityProxy.cs
│ ├── Program.cs
├── SmartCity.Core
│ └── IModule.cs
├── SmartCity.Modules.Lighting
│ └── LightingModule.cs
├── SmartCity.Modules.Transport
│ └── TransportModule.cs
├── SmartCity.Modules.Energy
│ └── EnergyModule.cs
├── SmartCity.Modules.Security
│ └── SecurityModule.cs
└── SmartCity.Tests
└── Tests
├── ControllerTests.cs
├── ModuleFactoryTests.cs
└── SecurityProxyTests.cs

## 🛠️ Ishlatilgan patternlar

Loyiha quyidagi **patternlar** orqali qurilgan:

### 1️⃣ Singleton
- **Qayerda**: `SmartCityController.cs`  
- **Qanday ishlatiladi**: `SmartCityController` yagona instansiyani yaratadi va barcha modullarni shu instansiya orqali boshqaradi.  
- **Nima uchun ishlatiladi**: barcha modul boshqaruvi yagona nuqtadan amalga oshiriladi, bir nechta controller yaratishning oldi olinadi.  
- **Kod misoli**:

<!-- public class SmartCityController
{
    private static SmartCityController _instance;
    private List<IModule> _modules = new List<IModule>();

    private SmartCityController() { }

    public static SmartCityController Instance
    {
        get
        {
            if (_instance == null)
                _instance = new SmartCityController();
            return _instance;
        }
    }

    public void RegisterModule(IModule module) => _modules.Add(module);
    public void ExecuteAll() { foreach(var m in _modules) m.Execute(); }
} -->

## 2️⃣ Factory Method

**Qayerda**: `ModuleFactory.cs`

**Qanday ishlatiladi**: modul nomiga qarab tegishli modulni yaratadi `LightingModule, TransportModule, EnergyModule, SecurityModule`.

**Nima uchun ishlatiladi**: modul yaratishni markazlashtirish va yangi modul qo‘shishni osonlashtirish.

**Kod misoli**:

<!-- public static class ModuleFactory
{
    public static IModule Create(string type)
    {
        return type.ToLower() switch
        {
            "lighting" => new LightingModule(),
            "transport" => new TransportModule(),
            "energy" => new EnergyModule(),
            "security" => new SecurityModule(),
            _ => throw new ArgumentException("Unknown module type")
        };
    }
} -->

## 3️⃣ Proxy

**Qayerda**: `SecurityProxy.cs`

**Qanday ishlatiladi**: SecurityModule ishlashiga ruxsat berish yoki rad etish.

**Nima uchun ishlatiladi**: xavfsizlikni oshirish va kirishni nazorat qilish.

**Kod misoli**:

<!-- public class SecurityProxy : IModule
{
    private SecurityModule _realModule = new SecurityModule();
    private bool _accessGranted = false;

    public void SetAccess(bool access) => _accessGranted = access;

    public void Execute()
    {
        if (_accessGranted)
            _realModule.Execute();
        else
            Console.WriteLine("❌ Access Denied!");
    }
} -->

## 4️⃣ Adapter

**Qayerda**: modul ichida har xil xizmatlar bilan integratsiya uchun ishlatiladi (masalan, transport tizimining tashqi trafik API bilan ishlashi).

**Nima uchun ishlatiladi**: har xil tashqi xizmatlar interfeysini yagona interfeysga moslashtirish.

**Kod misoli**:

<!-- public class TransportAdapter : IModule
{
    private ExternalTrafficAPI _api = new ExternalTrafficAPI();

    public void Execute() => _api.UpdateTrafficFlow();
} -->

## 5️⃣ Facade

**Qayerda**: `SmartCityController.cs`

**Qanday ishlatiladi**: barcha modulni bitta ExecuteAll() metodi orqali ishga tushirish.

**Nima uchun ishlatiladi**: foydalanuvchiga murakkab tizimni sodda interfeys bilan taqdim etish.

**Kod misoli**: `yuqoridagi ExecuteAll() metodi`.




## 🏙️ Modul vazifalari

| Modul     | Fayl                 | Vazifa                                                                |
| --------- | -------------------- | --------------------------------------------------------------------- |
| Lighting  | `LightingModule.cs`  | Shahar chiroqlarini va yoritishni vaqt va ob-havo sharoitiga moslash. |
| Transport | `TransportModule.cs` | Transport oqimini boshqarish, svetoforlar ishini sozlash.             |
| Energy    | `EnergyModule.cs`    | Energiya sarfini optimizatsiya qilish va monitoring.                  |
| Security  | `SecurityModule.cs`  | Xavfsizlikni ta’minlash, kirish ruxsatini tekshirish (Proxy orqali).  |



## ✅ Unit Testlar ro‘yxati (7 ta)

1. `ControllerTests.cs`

Singleton_InstanceIsSame

**Vazifa**: SmartCityController Singleton sifatida ishlashini tekshiradi.

**maqsad**: Controllerning barcha instance-lari bir xil obyektni ko‘rsatishini tekshiradi.

2. `ModuleFactoryTests.cs`

LightingModule_CreatedSuccessfully

**Vazifa**: LightingModule Factory orqali muvaffaqiyatli yaratilishini tekshiradi.

TransportModule_CreatedSuccessfully

**Vazifa**: TransportModule Factory orqali muvaffaqiyatli yaratilishini tekshiradi.

SecurityModule_CreatedSuccessfully

**Vazifa**: SecurityModule Factory orqali muvaffaqiyatli yaratilishini tekshiradi.

EnergyModule_CreatedSuccessfully

**Vazifa**: EnergyModule Factory orqali muvaffaqiyatli yaratilishini tekshiradi.

3. `SecurityProxyTests.cs`

AccessAllowed_ReturnsTrue

**Vazifa**: Ruxsatli foydalanuvchi (admin123) SecurityProxy orqali modulga kirishini tekshiradi.

AccessDenied_ReturnsFalse

**Vazifa**: Ruxsatsiz foydalanuvchi (guest) SecurityProxy orqali modulga kira olmasligini tekshiradi.

## 📌 Natija:

**Jami testlar**: 7

**Muvaffaqiyatli bajarilgan**: 7/7


## 🚀 Ilovani ishga tushirish

1. GitHub’dan yuklab olish

git clone <repository_url>
cd SmartCitySystem

2. Paketlarni tiklash

dotnet restore

3. Konsol orqali ishga tushirish

cd SmartCity.App
dotnet run

4. Faqat ma’lum modulni ishga tushirish

dotnet run -- Lighting

5. Unit testlarni ishga tushirish

cd SmartCity.Tests
dotnet test
