# %%
import random 
import cv2 
from keras.models import load_model 
import numpy as np 
import time 

class Game:
    '''
        A Rock-Paper-Scissors game 

        Attributes:
        ----------
        move_list: dictionary
            A list of possible moves in the game.
        user_choice: str
            The user's move.
        user_wins: int
            The number of round wins for the user.
        computer_wins: int
            The number of round wins for the computer.

        Methods:
        -------
        get_computer_choice
            Selects the move made by the computer.
        get_user_choice
            Predicts the user's move using a camera and trained model.
        get_winner
            Checks the result of the round between the computer and the user.
        '''
    def __init__(self):

        self.move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
        self.user_choice = ""   
        self.user_wins = 0 
        self.computer_wins = 0 

    def get_computer_choice(self):
        '''
        Selects the move made by the computer randomly from a dictionary of viable moves and they can be:
        - rock
        - paper
        - scissors
        '''
        computer_choice = random.choice(list(self.move_list.values())) 

    def get_user_choice(self): 
        '''
        Predicts the user's move using a previously trained model
        
        '''
        # defines the user choice function, passing only self as the argument
        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0) # captures the webcam video frame by frame and set as cap object - 0 is the first camera
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        end = time.time() + 6  
        while end > time.time(): # loop continues for 6 seconds
            ret, frame = cap.read() # reads the video from the camera frame by frame
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # resizes image(input image, size, interpolation)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data) # the predicted values from the model in a matrix
            cv2.putText(frame, f"{int(end - time.time())}", (100,150), cv2.FONT_HERSHEY_DUPLEX, 4, (255,0,0), 3) # prints countdown timer
            cv2.imshow('User Move', frame) # displays video in a window called User Move
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
                break

        if np.argmax(prediction) == 0:
                self.user_choice = "Rock" # if first prediction is highest, choice is Rock
        elif np.argmax(prediction) == 1:
                self.user_choice = "Scissors" # if second prediction is highest, choice is Scissors
        elif np.argmax(prediction) == 2:
                self.user_choice = "Paper" # if third prediction is highest, choice is Paper
        elif np.argmax(prediction) == 3:
                self.user_choice = "Nothing" # if fourth prediction is highest, choice is Nothing
        print(f"You chose {self.user_choice}.") 
             
        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
    
    def get_winner(self, computer_choice): 
        '''
        Checks the result of the round with 3 different checks:
        1. If the user's move beats the computer's move
        - this means the user wins the round and gets 1 point added to their round wins (user_wins)
        2. If the user's move is identical to the computer's move
        - this means the round is a draw
        3. If the computer's move beats the user's move
        - this means the computer wins the round and gets 1 point added to their round wins (computer_wins)
        Paramters:
        ---------
        computer_choice: str
            The computer's move.
        '''
        if (self.user_choice == self.move_list["0"] and computer_choice == self.move_list["1"] 
        or self.user_choice == self.move_list["1"] and computer_choice == self.move_list["2"] 
        or self.user_choice == self.move_list["2"] and computer_choice == self.move_list["0"]): 
            print("You won the round!")
            self.user_wins += 1 
        elif self.user_choice == computer_choice: 
            print("You drew the round!")
        else: 
            self.computer_wins += 1 
            print("You lost the round!")
        print(f"The score is {self.user_wins} - {self.computer_wins}.") 


# %%
game = Game() # creates the game instance using the Game class
def play(): # defines the function that plays the game   
    while True:
        if game.user_wins < 3 and game.computer_wins < 3: # game runs until user or computer reaches 3 wins
            game.get_computer_choice() # calls the computer choice function
            game.get_user_choice() # calls the user choice function
            game.get_winner(game.computer_choice, game.user_choice) # calls the winner function, using the game instances' user and computer choices as arguments
        else:  
            if game.user_wins == 3:    
                print("You won the game!")
            elif game.computer_wins == 3:
                print("You lost the game!")
            game.replay_choice = input("Would you like to play? Choose 'y' or 'n'.") # choice given to user to replay the game
            break  

def play_replay(): # defines the function used to replay the game 
    play() # calls the play function
    while True:
        if game.replay_choice == "y": # checks to see if the input is y (yes)
            game.user_wins = 0 # resets wins of both user and computer to 0
            game.computer_wins = 0
            play() # recalls the play function
        elif game.replay_choice == "n": # ends loop if input is n (no)
            print("Thanks for playing!") 
            break
# %%
play_replay()
# %%
