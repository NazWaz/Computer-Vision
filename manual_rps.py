#%%
import random # imports random module

class Game:
    def __init__(self, move_list):
        self.move_list = move_list
        self.computer_choice = ""
        self.user_choice = ""

    def get_computer_choice(self): 
        self.computer_choice = random.choice(list(self.move_list.values()))
        print(self.move_list)
        print(self.computer_choice)

    def get_user_choice(self):
        while True:
            self.user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.")
            print(self.user_choice)
            break
    
    def get_winner(self, computer_choice, user_choice):
        if (user_choice == self.move_list["0"] and computer_choice == self.move_list["1"] 
        or user_choice == self.move_list["1"] and computer_choice == self.move_list["2"] 
        or user_choice == self.move_list["2"] and computer_choice == self.move_list["0"]):
            print("You have won!")
        elif user_choice == computer_choice:
            print("You have drawn!")
        else:
            print("You have lost!")
# %%
def play():
    game = Game(move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"})
    while True:
        game.get_computer_choice()
        game.get_user_choice()
        game.get_winner(game.computer_choice, game.user_choice)
        break
# %%
play()