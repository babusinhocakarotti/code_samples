`cd C:\Users\Coskun\Desktop\Courses\2025-26_Winter\Object Based Programming\code_samples\ooplabspytest -v`

or
`pytest -s`

or 

`pytest -v -s`


```text
ooplabs/
│   __init__.py
│   config.py                       # Central configuration & environment setup (logging level, paths, etc.).
│                                       # Environment vars, Pathlib, modular settings
│
├── utils/
│   __init__.py
│   logging.py                       # Logging setup (configurable, used project-wide). Unified logger with console/file & rotation
│                                       # Dependency Injection, reuse, configuration
│   events.py                        # Implements Observer/EventBus pattern. Observer pattern for decoupled event handling
│                                       # Encapsulation, static methods, error handling
│
├── vehicles/
│   __init__.py
│   base.py                          # Abstract base classes (Vehicle, Engine, Driveable).
│   vehicles.py                      # Concrete classes: Car, Bicycle, ElectricCar
│   mechanic.py                      # Mechanic class (Factory + repair logic)
│   behaviors.py                     # Strategy pattern for drive behaviors
│   exceptions.py                    # Custom exception hierarchy
│
└── tests/
    test_car.py
    test_wheels.py
    test_bicycle.py
    test_my_car.py
```


|  |  |  |
| - | - | - |
|  |  |  |
|  |  |  |

---

| Concept                               | Implemented In                   | Description                                               |
| ------------------------------------- | -------------------------------- | --------------------------------------------------------- |
| **Encapsulation & Abstraction** | `base.py`, `vehicles.py`     | Abstract base class `Vehicle`, protected attrs          |
| **Inheritance & Polymorphism**  | `vehicles.py`                  | `Car` and `Bicycle` inherit from `Vehicle`          |
| **Composition & Aggregation**   | `vehicles.py`, `mechanic.py` | `Vehicle` uses `Engine` and `Mechanic` compositions |
| **Factory Pattern**             | `mechanic.py`                  | Creates objects dynamically                               |
| **Strategy Pattern**            | `behaviors.py`                 | Plug‑and‑play drive strategies                          |
| **Observer Pattern**            | `events.py`                    | Logs and mechanics subscribe to events                    |
| **Custom Exceptions**           | `exceptions.py`                | Domain‑specific error management                         |
| **Logging (Configurable)**      | `logging.py`, `config.py`    | Controlled through environment or config                  |
| **Unit Testing**                | `tests/*.py`                   | Full pytest support with printed + logged output          |

---
