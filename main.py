from Controllers.Player_controller import Player_Controller
from Controllers.Board_Component_controller import Board_Component_controller
from Controllers.Game_controller import Game_Controller

def main():
    
    player_name = input("Player name?")
    player_id = int(input("Player id?"))
    
    snake_count = int(input("Enter the number of snakes: "))
    ladder_count = int(input("Enter the number of ladders: "))
    snake_mouth_and_tail = {}
    ladder_start_and_end = {}
    snake_dictionary_index = 0
    ladder_dictionary_index = 0

    while snake_dictionary_index < snake_count:
        snake_mouth = int(input("Enter the position for snake mouth for snake number {}: ".format(snake_dictionary_index + 1)))
        snake_tail = int(input("Enter the position for snake tail for snake {}: ".format(snake_dictionary_index + 1)))
        if snake_mouth > snake_tail:
            snake_dictionary_index += 1
        else:
            print("Enter a value lesser than snake mouth value!!!")
            snake_dictionary_index -= 1
        snake_mouth_and_tail[snake_mouth] = snake_tail

    while ladder_dictionary_index < ladder_count:
        ladder_start = int(input("Enter the position for start of ladder number {}: ".format(ladder_dictionary_index + 1)))
        ladder_end = int(input("Enter the position for end of ladder number {}: ".format(ladder_dictionary_index + 1)))
        if ladder_start < ladder_end:
            ladder_dictionary_index += 1
        else:
            print("Enter a value greater than ladder start value!!!")
            ladder_dictionary_index -= 1
        ladder_start_and_end[ladder_start] = ladder_end
        
    player = Player_Controller(player_id,player_name)
    board_component_controller = Board_Component_controller(snake_mouth_and_tail,ladder_count,ladder_start_and_end)
    game = Game_Controller(player_id)
    
    print("Current Position: ",game)

if __name__ == "__main__":
    main()

