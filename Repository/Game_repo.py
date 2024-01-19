import psycopg2
from Models.Player import Player

class Player_Table_Manager:
    def __init__(self,id):
        connection = psycopg2.connect(host="localhost",dbname="snake_ladder",user="postgres",password="postgres",port="5432")
        cur = connection.cursor()
        self.fetch_position_from_player_table(connection,cur,id)
        
    def fetch_position_from_player_table(sel,connection,cur,id):
        #query to insert
        cur.close()
        connection.close()