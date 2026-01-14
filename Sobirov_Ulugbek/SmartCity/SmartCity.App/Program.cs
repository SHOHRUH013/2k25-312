// SmartCity.App/Program.cs
using SmartCity.Core.Controller;

namespace SmartCity.App;

/// <summary>
/// SmartCity - Aqlli Shahar Boshqaruv Tizimi
/// 
/// Design Patterns:
/// 1. Singleton - CityController (faqat bitta instance)
/// 2. Facade - CityController (murakkab subsistemalarni sodda interfeys orqali boshqarish)
/// 3. Builder - Transport obyektlarini yaratish
/// 4. Abstract Factory - Qurilmalar oilasini yaratish (Light, Camera)
/// 5. Factory Method - To'g'ri factory turini tanlash
/// 6. Adapter - Eski energiya tizimini yangi tizimga ulash
/// 7. Proxy - Xavfsizlik tizimiga kirish nazorati
/// </summary>
class Program
{
    static void Main(string[] args)
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("╔════════════════════════════════════════╗");
        Console.WriteLine("║   🏙️  SMARTCITY BOSHQARUV TIZIMI  🏙️   ║");
        Console.WriteLine("╚════════════════════════════════════════╝");
        
        // Singleton pattern - Faqat bitta controller
        var controller = CityController.Instance;
        
        // Shaharni ishga tushirish
        controller.InitializeCity();
        
        bool running = true;
        
        while (running)
        {
            ShowMenu();
            var choice = Console.ReadLine();
            
            Console.WriteLine();
            
            switch (choice)
            {
                case "1":
                    controller.ControlLighting(true);
                    break;
                    
                case "2":
                    controller.ControlLighting(false);
                    break;
                    
                case "3":
                    controller.ManageTraffic();
                    break;
                    
                case "4":
                    controller.StartTransport();
                    break;
                    
                case "5":
                    // Adapter pattern - Eski tizimdan ma'lumot olish
                    controller.MonitorEnergy();
                    break;
                    
                case "6":
                    // Proxy pattern - Ruxsatli foydalanuvchi
                    controller.AccessSecurity("admin");
                    break;
                    
                case "7":
                    // Proxy pattern - Ruxsatsiz foydalanuvchi
                    controller.AccessSecurity("guest");
                    break;
                    
                case "8":
                    controller.DisplayStatus();
                    break;
                    
                case "9":
                    running = false;
                    Console.WriteLine("👋 Dastur tugatildi. Xayr!");
                    break;
                    
                default:
                    Console.WriteLine("❌ Noto'g'ri tanlov!");
                    break;
            }
            
            if (running)
            {
                Console.WriteLine("\n▶ Davom etish uchun Enter bosing...");
                Console.ReadLine();
                Console.Clear();
            }
        }
    }
    
    static void ShowMenu()
    {
        Console.WriteLine("\n┌─────────────────────────────────┐");
        Console.WriteLine("│         📋 MENYU                │");
        Console.WriteLine("├─────────────────────────────────┤");
        Console.WriteLine("│ 1. 💡 Chiroqlarni yoqish       │");
        Console.WriteLine("│ 2. 💡 Chiroqlarni o'chirish     │");
        Console.WriteLine("│ 3. 🚦 Svetoforlarni boshqarish  │");
        Console.WriteLine("│ 4. 🚌 Transportni ishga tushir  │");
        Console.WriteLine("│ 5. ⚡ Energiya monitoringi      │");
        Console.WriteLine("│ 6. 🔐 Xavfsizlik (Admin)        │");
        Console.WriteLine("│ 7. 🔐 Xavfsizlik (Mehmon)       │");
        Console.WriteLine("│ 8. 📊 Shahar holati             │");
        Console.WriteLine("│ 9. 🚪 Chiqish                   │");
        Console.WriteLine("└─────────────────────────────────┘");
        Console.Write("Tanlovingiz: ");
    }
}