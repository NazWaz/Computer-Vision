
# %%
def get_computer_choice(): 
    import random # imports random module
    computer_choice = random.choice(list(move_list.values()))
    print(move_list)
    print(computer_choice)
# %%
def get_user_choice():
    while True:
        user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.")
        print(user_choice)
        break
# %%
def get_winner(computer_choice, user_choice):
    if (user_choice == move_list["0"] and computer_choice == move_list["1"] 
    or user_choice == move_list["1"] and computer_choice == move_list["2"] 
    or user_choice == move_list["2"] and computer_choice == move_list["0"]):
        print("You have won!")
    elif user_choice == computer_choice:
        print("You have drawn!")
    else:
        print("You have lost!")
# %%

def play ():
    move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
    computer_choice = get_computer_choice
    user_choice = get_user_choice
    get_winner(computer_choice, user_choice)


# %%
play()


#%%
import random # imports random module

class Game:
    def __init__(self, move_list):
        self.move_list = move_list

    def get_computer_choice(self): 
        move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
        computer_choice = random.choice(list(move_list.values()))
        print(move_list)
        print(computer_choice)

    def get_user_choice(self):
        while True:
            user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.")
            print(user_choice)
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
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        break

# %%
play()

# %%
