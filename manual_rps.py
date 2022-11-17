#%%
import random 

class Game:
    '''
    A Rock-Paper-Scissors game between the computer and user, played using a camera to detect the user's move.
    The game is replayable and lasts until the user or computer reaches 3 wins.

    Parameters:
    ----------
    move_list: dictionary
        A list of possible moves in the game.

    Attributes:
    ----------
    user_choice: str
        The user's move.

    Methods:
    -------
    get_computer_choice
        Selects the move made by the computer.
    get_user_choice
        Asks the user for their move.
    get_winner
        Checks the result of the round between the computer and the user.
    '''
    def __init__(self, move_list):

        self.move_list = move_list 
        self.user_choice = ""   
        self.computer_choice = ""

    def get_computer_choice(self):
        '''
        Selects the move made by the computer randomly from a dictionary of moves:
        - rock
        - paper
        - scissors
        '''
        computer_choice = random.choice(list(self.move_list.values())) 
        return computer_choice

    def get_user_choice(self): 
        '''
        Asks the user to input their choice of move between:
        - rock
        - paper
        - scissors
        '''
        while True: 
            self.user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.") 
            break 
    
    def get_winner(self):
        '''
        Checks the result of the round with 3 different checks:
        1. If the user's move beats the computer's move
        - this means the user wins the round and gets 1 point added to their round wins (user_wins)
        2. If the user's move is identical to the computer's move
        - this means the round is a draw
        3. If the computer's move beats the user's move
        - this means the computer wins the round and gets 1 point added to their round wins (computer_wins)
        '''
        computer_choice = self.get_computer_choice()
        if (self.user_choice == self.move_list["0"] and computer_choice == self.move_list["1"] 
        or self.user_choice == self.move_list["1"] and computer_choice == self.move_list["2"] 
        or self.user_choice == self.move_list["2"] and computer_choice == self.move_list["0"]): 
            print("You have won!")
        elif self.user_choice == computer_choice: 
            print("You have drawn!")
        else: 
            print("You have lost!")
# %%
def play():
    '''
    Plays the game by calling the get_computer_choice, get_user_choice and get_winner methods.
    '''
    game = Game({"0": "Rock", "1": "Scissors", "2": "Paper"}) 
    while True:
        game.get_user_choice() 
        game.get_winner() 
        break
# %%
play()
# %%
