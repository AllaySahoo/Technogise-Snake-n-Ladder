import random

class Board:
      
    def roll_dice_for_number(self,position):
        numbers_on_dice = [1,2,3,4,5,6]
        random_number_of_dice = random.choice(numbers_on_dice)
        return self.move_piece(position , random_number_of_dice)        
    
    
    def move_piece(self,position , random_number_of_dice):
        if(self.check_if_more_than_100(position, random_number_of_dice)):
            return position
        else:
            return position + random_number_of_dice
            
    
    def check_if_more_than_100(self,position , random_number_of_dice):
        if(position + random_number_of_dice > 100):
            return True
        else:
            return False
        
    def display():
        return "Roll Again"
    
    
class Ladder(Board):
    
   def ladder_encounter(self, new_position, ladder_start_and_end):
        for key in ladder_start_and_end.items():
            if new_position == key:
                return ladder_start_and_end[key]  
        return new_position
    
    # def display():
    #     return "Wow...ladder!!"
           


class Snake(Board):      
    
    def snake_bit(self, new_position, snake_mouth_and_tail):
        for key in snake_mouth_and_tail.items():
            if new_position == key:
                return snake_mouth_and_tail[key]  
        return new_position         
    
    # def display():
    #     return "ohh no Snake!!"
        
class Play(Snake,Ladder):
    
    
    
    def __init__(self,snake_count ,snake_mouth_and_tail,ladder_count,ladder_start_and_end):
        self.snake_count = snake_count
        self.snake_mouth_positions = snake_mouth_and_tail  
        self.ladder_count = ladder_count
        self.ladder_start_and_end = ladder_start_and_end   
        
        
    def playing(self,piece_positon):
        self.piece_positon = piece_positon
        new_position = self.roll_dice_for_number(self.piece_positon)
        new_position = self.snake_bit(new_position,self.snake_mouth_positions)
        new_position = self.ladder_encounter(new_position,self.ladder_start_and_end)
        return new_position       
        
        
    
def main():  
    
    piece_positon = 0
    
    snake_count = int(input("Enter the number of snakes: "))
   
    ladder_count = int(input("Enter the number of ladders: "))
   
    snake_mouth_and_tail = {}
   
    ladder_start_and_end = {}
   
    snake_dictionary_index = 0
   
    ladder_dictionary_index = 0
   
    while (snake_dictionary_index < snake_count):
       snake_mouth = int(input("enter the position for snake mouth for snake number "+ str(snake_dictionary_index + 1) + ": "))
       snake_tail = int(input("enter the position for snake tail for snake "+ str(snake_dictionary_index + 1) + ": "))
       if(snake_mouth > snake_tail):
           snake_dictionary_index+=1
       else:
           print("enter a value lesser than snake mouth value!!!")
           snake_dictionary_index-=1
           
       snake_mouth_and_tail[snake_mouth]=snake_tail
       
       
    while (ladder_dictionary_index < ladder_count):
        ladder_start = int(input("enter the position for start of laddder number " + str(ladder_dictionary_index+1) + ":"))
        ladder_end = int(input("enter the position for end of ladder number "+ str(ladder_dictionary_index+1) + ":"))
        if(ladder_start < ladder_end):
           ladder_dictionary_index+=1
        else:
           print("enter a value greater than ladder start value!!!")
           ladder_dictionary_index-=1
           
        ladder_start_and_end[ladder_start]=ladder_end
       
    play = Play(snake_count,snake_mouth_and_tail,ladder_count,ladder_start_and_end)
    
    print(snake_mouth_and_tail)
    print(ladder_start_and_end)
    
    want_to_play = True
    
    while(want_to_play):
        piece_positon = play.playing(piece_positon)
        print("new position" , piece_positon)
        want_to_play = input("True / False?")
        if(want_to_play=="False"):
            return 0
    

if __name__ == "__main__":
    main()