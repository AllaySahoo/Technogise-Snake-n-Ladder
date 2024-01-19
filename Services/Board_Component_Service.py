from  Repository.Board_Component_repo import Board_Component_Table_Manager

class Board_Component_Service:
    
     def create_snakes_and_ladder_in_database(self,board_component):
        Board_Component_Table_Manager(board_component)