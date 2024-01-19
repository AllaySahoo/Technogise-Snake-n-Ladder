# so...why de we need this class/model ? simple hai..like we ahev 
# player model joh i player details/properties  ko  carry kar rha hai
# similarly we have board_component modulejoh snake and ladder ko dyanmic banarha hai
# dono player and board_component dynamic hai...scalable hai...but jab snake bite karega,
# yah ladder encounter karega yah normally bhi move karega yah multi player game ho
# tab niche ke yeh list kaam ayenge


class Board:
    def __init__(self,snake,ladder,player):
        list_of_snakes = []
        list_of_ladders = []
        list_of_players = []
        
        list_of_snakes.append(snake)
        list_of_ladders.append(ladder)
        list_of_players.append(player)