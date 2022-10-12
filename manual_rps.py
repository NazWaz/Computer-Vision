#%%
import random # imports random module

class Game:
    def __init__(self, move_list): # intialises parameters

        self.move_list = move_list # move list is given as an argument as a dictionary later
        self.computer_choice = "" # computer choice is given an empty string value
        self.user_choice = ""   # user choice is given an empty string value

    def get_computer_choice(self): # defines the computer choice function, passing only self as the argument
        self.computer_choice = random.choice(list(self.move_list.values())) # chooses random values from a dictionary converted into a list

    def get_user_choice(self): # defines the user choice function, passing only self as the argument
        while True: # makes the loop continuous
            self.user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.") # asks for user's input
            break # ends loop
    
    def get_winner(self, computer_choice, user_choice): # defines the winner function, using the previous choice functions and self as arguments
        if (user_choice == self.move_list["0"] and computer_choice == self.move_list["1"] 
        or user_choice == self.move_list["1"] and computer_choice == self.move_list["2"] 
        or user_choice == self.move_list["2"] and computer_choice == self.move_list["0"]): # condition where the user's choice beats the computer's choice
            print("You have won!")
        elif user_choice == computer_choice: # condition where the user's choice is equal to the computer's choice
            print("You have drawn!")
        else: 
            print("You have lost!")
# %%
def play():
    game = Game(move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}) # creates the game instance using the Game class
    while True:
        game.get_computer_choice() # calls the computer choice function
        game.get_user_choice() # calls the user choice function
        game.get_winner(game.computer_choice, game.user_choice) # calls the winner function, using the game instances' user and computer choices as arguments
        break
# %%
play()