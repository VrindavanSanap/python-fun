from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)   # Output: Color.RED
print(Color.GREEN) # Output: Color.GREEN
print(Color.BLUE)  # Output: Color.BLUE

