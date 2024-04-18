from constants import Color, Manufacturer, auto_dealers

class Auto:
    # Class variable
    wheels: int = 4
    
    # Constructor
    def __init__(self, color: Color, make: Manufacturer, model:str) -> None:
        # Instance variable
        self.color = color
        self.make = make
        self.model = model
    
    # Instance property
    @property
    def price(self) -> int:
        return (self.wheels * 10000)
    
    # Instance method    
    def get_details(self) -> None:
        print(f"Auto: {self.make} {self.color} {self.model} wheels: {self.wheels}")
    
    # Static method    
    @staticmethod
    def get_top_dealers(n: int) -> list:
        sorted_dealers = sorted(auto_dealers, key=lambda x: x["rating"], reverse=True)
        return sorted_dealers[:n]

    @classmethod
    def print_default_wheels(cls) -> None:
        print(f"Default number of Auto wheels: {cls.wheels}")

# Create instances            
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
    
print("-----")

# Class Method usage: Get the default wheels
Auto.print_default_wheels()

# Instance Property usage: Get the price
bmw = Auto(Color.BLACK, Manufacturer.BMW, "X5")
print(f"BMW Price: ${bmw.price}")