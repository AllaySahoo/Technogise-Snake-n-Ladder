import psycopg2
from Models.Board_Component import Board_Component

class Board_Component_Table_Manager:
    
    def __init__(self,board_components):
        connection = psycopg2.connect(host="localhost",dbname="snake_ladder",user="postgres",password="postgres",port="5432")
        cur = connection.cursor()
        self.add_components_to_board_component_table(connection,cur,board_components)
        
    def add_components_to_board_component_table(sel,connection,cur,board_components):
            
        #query to insert each component
        
        cur.close()
        connection.close()