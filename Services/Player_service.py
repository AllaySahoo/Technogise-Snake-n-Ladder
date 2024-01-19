from Repository.Player_repo import Player_Table_Manager

class Player_Service:
    
    def create_player_in_database(self,player):
        Player_Table_Manager(player)
                  
   
        