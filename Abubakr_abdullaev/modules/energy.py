class EnergySystem:
    """Подсистема энергосбережения"""
    
    def __init__(self):
        self.consumption = 1250  # кВт⋅ч
    
    def current_consumption(self):
        return self.consumption
    
    def show_stats(self):
        print("\nЭнергосбережение")
        print(f"Текущее потребление: {self.consumption} кВт⋅ч")
        print("• Освещение: 480 кВт⋅ч (38%)")
        print("• Транспорт: 320 кВт⋅ч (26%)")
        print("• Безопасность: 200 кВт⋅ч (16%)")
        print("• Прочее: 250 кВт⋅ч")
        
        save = input("\nВключить режим максимального энергосбережения? (y/n): ")
        if save.lower() == "y":
            self.consumption = 780
            print("Режим энергосбережения активирован! Потребление снижено до 780 кВт⋅ч")