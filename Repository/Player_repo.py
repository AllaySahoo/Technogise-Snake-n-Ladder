import psycopg2
from Models.Player import Player

class Player_Table_Manager:
    
    def __init__(self,player):
        connection = psycopg2.connect(host="localhost",dbname="snake_ladder",user="postgres",password="postgres",port="5432")
        cur = connection.cursor()
        self.add_player_to_player_table(connection,cur,player)
        
    def add_player_to_player_table(sel,connection,cur,player):
        #query to insert
        cur.close()
        connection.close()

    