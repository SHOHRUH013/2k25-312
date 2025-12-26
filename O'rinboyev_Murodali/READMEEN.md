# 🧩 Lab Work №1
### Project: SmartCity System

---

## 📘 Assignment Description

SmartCity System is a console application that simulates the operation of an intelligent city management system.  
The system combines various subsystems responsible for lighting, transportation, security, energy saving, monitoring, and other urban infrastructure functions.

Each subsystem is implemented using design patterns that ensure architectural stability and extensibility of the project.

---

## 🧱 Main Requirements

1. The project must be implemented in **Any language* using **object-oriented programming**.  
2. The architecture must include **at least five design patterns** from the provided list.  
3. Each design pattern must have a functional purpose within the system.  
4. The system must be logically coherent and consist of interconnected components.  
5. User interaction is performed via the console interface.  
6. For each design pattern, a comment or docstring should indicate its usage and purpose.

---

## 🧩 Allowed Design Patterns

### Creational:
- Abstract Factory  
- Factory Method  
- Builder  
- Prototype  
- Singleton  

### Structural:
- Adapter  
- Bridge  
- Composite  
- Decorator  
- Facade  
- Flyweight  
- Proxy  

---

## ⚙️ Project Structure

The project is organized as a modular application.  
Recommended directory structure:

FIO/
├── main.py # Main application entry point
├── test.py # Test for system
├── core/ # Core system components
│ ├── controller.py # Central controller / Facade / Singleton
│ ├── factories/ # Creational patterns (Factory, Abstract Factory)
│ ├── builders/ # Builder for step-by-step object construction
│ ├── adapters/ # Adapter for external service integration
│ ├── proxy/ # Proxy for subsystem access control
│ └── singleton/ # Singleton for unique components
├── modules/ # Smart city subsystems
│ ├── transport/ # Transportation management
│ ├── lighting/ # Lighting management
│ ├── security/ # Security subsystem
│ └── energy/ # Energy saving and monitoring
└── README.md # Assignment description and project structure


---

## 🧮 Evaluation Criteria

| Criterion                                          | Points        |
|----------------------------------------------------|---------------|
| At least 5 design patterns from the list are used  | 5             |
| Meaningful application of patterns in architecture | 4             |
| Correct program execution and logical workflow     | 3             |
| Code quality, structure, readability               | 3             |
| Unit tests                                         | 5             |
| **Maximum:**                                       | **20 points** |
