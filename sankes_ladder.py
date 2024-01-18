import random

class Model:
    def __init__(self, snake_count, snake_mouth_and_tail, ladder_count, ladder_start_and_end):
        self.board = Board(snake_count, snake_mouth_and_tail, ladder_count, ladder_start_and_end)

    def play(self, piece_position):
        new_position = self.board.roll_dice_for_number(piece_position)
        new_position = self.board.snake_bit(new_position)
        new_position = self.board.ladder_encounter(new_position)
        return new_position

class Board:
    def __init__(self, snake_count, snake_mouth_and_tail, ladder_count, ladder_start_and_end):
        self.snake_count = snake_count
        self.snake_mouth_positions = snake_mouth_and_tail
        self.ladder_count = ladder_count
        self.ladder_start_and_end = ladder_start_and_end

    def roll_dice_for_number(self, position):
        numbers_on_dice = [1, 2, 3, 4, 5, 6]
        random_number_of_dice = random.choice(numbers_on_dice)
        return self.move_piece(position, random_number_of_dice)

    def move_piece(self, position, random_number_of_dice):
        if self.check_if_more_than_100(position, random_number_of_dice):
            return position
        else:
            return position + random_number_of_dice

    def check_if_more_than_100(self, position, random_number_of_dice):
        if position + random_number_of_dice > 100:
            return True
        else:
            return False

    def snake_bit(self, new_position):
        for key in self.snake_mouth_positions.keys():
            if new_position == key:
                return self.snake_mouth_positions[key]
        return new_position

    def ladder_encounter(self, new_position):
        for key in self.ladder_start_and_end.keys():
            if new_position == key:
                return self.ladder_start_and_end[key]
        return new_position
    
class View:
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)
        
class Controller:   
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_input(self):
        return self.view.get_user_input("True / False?")

    def start_game(self):
        piece_position = 0
        want_to_play = True

        while want_to_play:
            piece_position = self.model.play(piece_position)
            self.view.display_message("New position: {}".format(piece_position))
            want_to_play = self.get_user_input()

def main():
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

    model = Model(snake_count, snake_mouth_and_tail, ladder_count, ladder_start_and_end)
    view = View()
    controller = Controller(model, view)

    controller.start_game()

if __name__ == "__main__":
    main()
