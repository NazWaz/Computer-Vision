
# %%
import random # imports random module
move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}

def get_computer_choice():
    computer_choice = random.choice(list(move_list.values()))
    print(move_list)
    print(computer_choice)
def get_user_choice():
    user_choice = input("Enter 'Rock', 'Paper' or 'Scissors'.")
    print(user_choice)

get_computer_choice()
get_user_choice()

def get_winner(computer_choice, user_choice):
    if user_choice == move_list["0"] and computer_choice == move_list["1"]:
        print("You have won!")
    elif user_choice == move_list["1"] and computer_choice == move_list["2"]:
        print("You have won!")
    elif user_choice == move_list["2"] and computer_choice == move_list["0"]:
        print("You have won!")

get_winner()

    
# %%
def play():

# %%
import random # imports random module
move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
computer_choice = "Paper"
user_choice = "Paper"
def get_winner(computer_choice, user_choice):
    if (user_choice == move_list["0"] and computer_choice == move_list["1"] 
    or user_choice == move_list["1"] and computer_choice == move_list["2"] 
    or user_choice == move_list["2"] and computer_choice == move_list["0"]):
        print("You have won!")
    elif user_choice == computer_choice:
        print("You have drawn!")
    else:
        print("You have lost!")
    
get_winner(computer_choice, user_choice)
# %%
elif user_choice == move_list["1"] and computer_choice == move_list["2"]:
        print("You have won!")
    elif user_choice == move_list["2"] and computer_choice == move_list["0"]:
        print("You have won!")