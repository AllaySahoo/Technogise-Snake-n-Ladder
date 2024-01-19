import random
import Repository.Game_repo import Player_Table_Manager

class Game_services:
    
    def get_player_current_position(self,id):
        current_position = fetch_position_from_player_table(id)
        
    
    # def roll_dice_for_number(self, position):
    #      numbers_on_dice = [1, 2, 3, 4, 5, 6]
    #      random_number_of_dice = random.choice(numbers_on_dice)
    #      return self.move_piece(position, random_number_of_dice)
     
    # def move_piece(self, position, random_number_of_dice):
    #     if self.check_if_more_than_100(position, random_number_of_dice):
    #         return position
    #     else:
    #         return position + random_number_of_dice
    
    # def check_if_more_than_100(self, position, random_number_of_dice):
    #     if position + random_number_of_dice > 100:
    #         return True
    #     else:
    #         return False
    
    # def snake_bit(self, new_position):
    #     for key in self.snake_mouth_positions.keys():
    #         if new_position == key:
    #             return self.snake_mouth_positions[key]
    #     return new_position

    # def ladder_encounter(self, new_position):
    #     for key in self.ladder_start_and_end.keys():
    #         if new_position == key:
    #             return self.ladder_start_and_end[key]
    #     return new_position