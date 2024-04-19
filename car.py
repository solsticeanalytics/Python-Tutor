from dataclasses import dataclass

@dataclass
class Car:
    make: str
    model: str
    year: int
    mileage: int
    fuel_type: str
    fuel_efficiency: float = None
    features: list = None

    def __post_init__(self):
        if self.mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        if self.fuel_efficiency is not None and self.fuel_efficiency <= 0:
            raise ValueError("Fuel efficiency must be a positive number.")

    def get_fuel_cost(self, price_per_gallon):
        if self.fuel_type == "gasoline":
            return self.fuel_efficiency * price_per_gallon / 30
        elif self.fuel_type == "electric":
            return self.fuel_efficiency * price_per_gallon / 40
        else:
            return "Invalid fuel type."

# Create an instance of the Car class
car = Car("Toyota", "Camry", 2020, 50000, "gasoline", 20.0, ["Navigation", "Sunroof"])

# Modify an attribute
car.mileage = 60000

# Calculate fuel cost
price_per_gallon = 3.00
fuel_cost = car.get_fuel_cost(price_per_gallon)

# Print the updated car object
print(car)