# %%
import random # imports random module
import cv2 # imports opencv library
from keras.models import load_model # imports keras library using model
import numpy as np # imports numpy module
import time # imports time module

class Game:
    def __init__(self): # intialises parameters

        self.move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"} # move list is given as an argument as a dictionary later
        self.computer_choice = "" # computer choice is given an empty string value
        self.user_choice = ""   # user choice is given an empty string value
        self.user_wins = 0 # user wins is given a zero interger value
        self.computer_wins = 0 # computer wins is given a zero integer value
        self.count = 3
        self.replay_choice = ""

    def get_computer_choice(self): # defines the computer choice function, passing only self as the argument
        self.computer_choice = random.choice(list(self.move_list.values())) # chooses random values from a dictionary converted into a list
        print(self.computer_choice)

    def get_user_choice(self): # defines the user choice function, passing only self as the argument
        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        start = time.time()
        end = time.time() + 6  
        while end > time.time(): # loop continues for 10 seconds
            ret, frame = cap.read() # reads the video from the camera frame by frame
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # resizes image(input image, size, interpolation)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.putText(frame, f"{int(end - time.time())}", (100,150), cv2.FONT_HERSHEY_DUPLEX, 4, (255,0,0), 3) # prints countdown timer
            cv2.imshow('User Move', frame) # displays video in a window called User Move
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
                break

        if np.argmax(prediction) == 0:
                self.user_choice = "Rock"
        elif np.argmax(prediction) == 1:
                self.user_choice = "Scissors"
        elif np.argmax(prediction) == 2:
                self.user_choice = "Paper" 
        elif np.argmax(prediction) == 3:
                self.user_choice = "Nothing"  
        print(f"You chose {self.user_choice}.") 
             
        cap.release()# After the loop release the cap object
        cv2.destroyAllWindows()# Destroy all the windows
    
    def get_winner(self, computer_choice, user_choice): # defines the winner function, using the previous choice functions and self as arguments
        if (user_choice == self.move_list["0"] and computer_choice == self.move_list["1"] 
        or user_choice == self.move_list["1"] and computer_choice == self.move_list["2"] 
        or user_choice == self.move_list["2"] and computer_choice == self.move_list["0"]): # condition where the user's choice beats the computer's choice
            print("You have won!")
            self.user_wins += 1 # adds 1 to user's score
        elif user_choice == computer_choice: # condition where the user's choice is equal to the computer's choice
            print("You have drawn!")
        else: 
            self.computer_wins += 1 # adds 1 to computer's score
            print("You have lost!")
        print(f"The score is {self.user_wins} - {self.computer_wins}.") # prints the game's score


# %%
game = Game() # creates the game instance using the Game class
def replay():    
    while True:
        if game.user_wins < 3 and game.computer_wins < 3:
            game.get_computer_choice() # calls the computer choice function
            game.get_user_choice() # calls the user choice function
            game.get_winner(game.computer_choice, game.user_choice) # calls the winner function, using the game instances' user and computer choices as arguments
        else:  
            game.replay_choice = input("Would you like to play? Choose 'y' or 'n'.")
            break  

def play():
    replay()
    while True:
                if game.replay_choice == "y":
                    game.user_wins = 0
                    game.computer_wins = 0
                    replay()
                elif game.replay_choice == "n":
                    print("Thanks for playing!")
                    break
    if game.user_wins == 3:    
        print("You have won the game!")
    elif game.computer_wins == 3:
        print("You have lost the game!")
# %%
play()
# %%
