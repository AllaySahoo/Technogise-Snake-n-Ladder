from Models.Player import Player
from Services.Player_service import Player_Service

class Player_Controller:
    
    def __init__(self,player_id,player_name):
        player = Player(player_id,player_name,0)
        player_service = Player_Service()
        player_service.create_player_in_database(player)