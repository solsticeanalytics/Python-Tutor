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
    MERCEDES = 5
    OTHER = 6
    
class Auto:
    # Class variable
    wheels: int = 4
    
    # Constructor
    def __init__(self, color: Color, make: Manufacturer, model:str):
        # Instance variable
        self.color = color
        self.make = make
        self.model = model
    
    # Instance method    
    def get_details(self):
        print(f"Auto: {self.make} {self.color} {self.model} wheels: {self.wheels}")
    
    # Static method    
    @staticmethod
    def get_top_dealers(n):

        auto_dealers = [
            {"name": "Dealer 1", "rating": 4.5},
            {"name": "Dealer 2", "rating": 3.8},
            {"name": "Dealer 3", "rating": 4.2},
            {"name": "Dealer 4", "rating": 4.9},
            {"name": "Dealer 5", "rating": 3.7},
            # Add more dealers here...
        ]    
        sorted_dealers = sorted(auto_dealers, key=lambda x: x["rating"], reverse=True)
        
        return sorted_dealers[:n]

            
toyota = Auto(Color.WHITE, Manufacturer.TOYOTA, "Corolla")
honda = Auto(Color.BLACK, Manufacturer.HONDA, "Civic")

toyota.get_details()
honda.get_details()

# Set wheels to 6
Auto.wheels = 6

toyota.get_details()
honda.get_details()

# Set wheels to 8
toyota.wheels = 8

toyota.get_details()
honda.get_details()

# Class usage: Get the top 3 dealers
top_dealers = Auto.get_top_dealers(3)
for dealer in top_dealers:
    print(dealer["name"], "- Rating:", dealer["rating"])

print("-----")
   
# Instance usage: Get the top 3 dealers
top_dealers = toyota.get_top_dealers(3)
for dealer in top_dealers:
    print(dealer["name"], "- Rating:", dealer["rating"])    