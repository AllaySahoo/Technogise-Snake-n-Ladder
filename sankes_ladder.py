import random

position = 0

# def change_position(position):
    
#     num = give_random_num()    
#     position = position + num
    
#     if(position > 100):
#         position = position - num
#         return position
#     else:
#         return position
    
# def give_random_num():
#     list1 = [1, 2, 3, 4, 5, 6]
#     num = random.choice(list1)
#     return num

    
# def check(position):
    
#     if (position==15):
#         print("Wow!!!! Ladder.....")
#         position=36
#         return position
#     elif (position==33):
#         print("Wow!!!! Ladder.....")
#         position=59
#         return position
#     elif (position==52):
#         print("Wow!!!! Ladder.....")
#         position=61
#         return position
#     elif (position==75):
#         print("Wow!!!! Ladder.....")
#         position=96
#         return position
        
#     elif (position==37):
#         print("Aouchhhh.....Snake")
#         position=25
#         return position
#     elif (position==64):
#         print("Aouchhhh.....Snake")
#         position=42
#         return position
#     elif (position==88):
#         print("Aouchhhh.....Snake")
#         position=1
#         return position
#     elif (position==99):
#         print("Aouchhhh.....Snake")
#         position=56
#         return position
    
#     elif (position==100):
#         print("Congratulations, You Win!!!!!")
#         position = 0
#         return position
    
#     else:
#         return position
    
# def display(position):
#     print("You are on : ",position)
    
class Snake:
    
    bite_positions = []
    
    def __init__(self,count_of_snakes):
        self.count_of_snakes = count_of_snakes
        
    def ask_Bite_Position(x):
        return input("Enter bite position of snake number:",x)
        
    def set_Snake_Bite():
        count_of_snakes = int(count_of_snakes)
       
        for x in range(count_of_snakes):
            user_input = ask_Bite_Position(x)
            bite_positions.append(x)
     
    def snake_bite_check()      
            
        
    
class Ladder:
    
    


def main():
    while(True):
        answer = input("Enter the corresponding Number of the option you want to choose: 1 - Play , 0 - Exit")
    print("You have chosen : ",answer)
    if(answer=='1'):
        count_of_snakes = input("Enter the number of snakes")
        count_of_ladders = input("Enter the number of ladders")
        
        snake_object = Snake(count_of_snakes)
        snake_object.set_Snake_Bite()
    elif(answer=='0'):
        print("Exit!!!")
        break
    else:
        print("Entered wrong value, Enter again")
        continue
    
    
if __name__=="__main__": 
    main()
    
