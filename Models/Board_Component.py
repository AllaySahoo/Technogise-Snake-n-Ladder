from enum import Enum, auto

class Board_Component_Type(Enum):
    Snake = auto()
    Ladder = auto()
    
class Board_Component:
    def __init__(self,id,start,end,type_num) :
        
        self.start = start
        self.end = end
        self.type = Board_Component_Type(type_num).name


