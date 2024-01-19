from Models.Board_Component import Board_Component
from Services.Board_Component_Service import Board_Component_Service

class Board_Component_controller:
    def __init__(self,snake_mouth_and_tail,ladder_start_and_end):
        
        board_component_service = Board_Component_Service()
        
        for key,value in snake_mouth_and_tail:
            start = key
            end = value 
            sanke_as_board_component = Board_Component(start,end,1)
            Board_Component_Service.create_snakes_and_ladder_in_database(sanke_as_board_component)
            
        for key,value in ladder_start_and_end:
            start = key
            end = value 
            ladder_as_board_components = Board_Component(start,end,2)
            Board_Component_Service.create_snakes_and_ladder_in_database(ladder_as_board_components)