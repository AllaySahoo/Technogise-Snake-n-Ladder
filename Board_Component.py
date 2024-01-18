from enum import Enum, auto

class Position(Enum):
    Snake = auto()
    Ladder = auto()
    
class Board_Component:
    def __init__(self) :
        self.start = 0
        self.end = 0
        self.type = Position()
    
