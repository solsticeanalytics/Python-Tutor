from enum import Enum

class Color(Enum):
    WHITE = 1
    BLACK = 2
    SILVER = 3
    OTHER = 4
    
class Manufacturer(Enum):
    TOYOTA = 1
    HONDA = 2
    FORD = 3
    BMW = 4
    MERCEDES = 5,
    OTHER = 6
    
class Auto:
    wheels: int = 4
    
    def __init__(self, color: Color, make: Manufacturer, model:str):
        self.color = color
        self.make = make
        self.model = model
        
    def print(self):
        print(f"Auto: {self.make} {self.color} {self.model} wheels: {self.wheels}")
        
toyota = Auto(Color.WHITE, Manufacturer.TOYOTA, "Corolla")
honda = Auto(Color.BLACK, Manufacturer.HONDA, "Civic")

toyota.print()
honda.print()

# Set wheels to 6
Auto.wheels = 6

toyota.print()
honda.print()

# Set wheels to 8
toyota.wheels = 8

toyota.print()
honda.print()
