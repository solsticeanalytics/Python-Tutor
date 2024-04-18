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

auto_dealers = [
    {"name": "Dealer 1", "rating": 4.5},
    {"name": "Dealer 2", "rating": 3.8},
    {"name": "Dealer 3", "rating": 4.2},
    {"name": "Dealer 4", "rating": 4.9},
    {"name": "Dealer 5", "rating": 3.7},
    # Add more dealers here...
]    