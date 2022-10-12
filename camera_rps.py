# %%
import random # imports random module
import cv2
from keras.models import load_model
import numpy as np
import time

class Game:
    def __init__(self, move_list): # intialises parameters

        self.move_list = move_list # move list is given as an argument as a dictionary later
        self.computer_choice = "" # computer choice is given an empty string value
        self.user_choice = ""   # user choice is given an empty string value

    def get_computer_choice(self): # defines the computer choice function, passing only self as the argument
        self.computer_choice = random.choice(list(self.move_list.values())) # chooses random values from a dictionary converted into a list
        print(self.computer_choice)

    def get_user_choice(self): # defines the user choice function, passing only self as the argument
        start = time.time()
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif np.argmax(prediction) == 0 and time.time() - start == 30:
                self.user_choice = "Rock"
                break
            elif np.argmax(prediction) == 1 and time.time() - start == 30:
                self.user_choice = "Scissors"
                break
            elif np.argmax(prediction) == 2 and time.time() - start == 30:
                self.user_choice = "Paper" 
                break
            elif np.argmax(prediction) == 3 and time.time() - start == 30:
                self.user_choice = "Nothing"  
                break
            print(f"You chose {self.user_choice}.") 
             
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
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
# %%
