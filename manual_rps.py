
# %%
import random # imports random module

def get_computer_choice():
    move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
    computer_move = random.choice(list(move_list.values()))
    print(move_list)
    print(computer_move)
def get_user_choice():
    user_move = input("Enter 'Rock', 'Paper' or 'Scissors'.")
    print(user_move)

get_computer_choice()
get_user_choice()

    
# %%

# %%
