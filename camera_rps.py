import random 
import cv2 
from keras.models import load_model 
import numpy as np 
import time 

class Game:
    '''
    A Rock-Paper-Scissors game between the computer and user, played using a camera to detect the user's move.
    The game is replayable and lasts until the user or computer reaches 3 wins.

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
        '''
        Constructs all the neccessary attributes for the game object.
        '''

        self.move_list = {"0": "Rock", "1": "Scissors", "2": "Paper"}
        self.user_choice = ""  
        self.user_wins = 0 
        self.computer_wins = 0 

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
        Predicts the user's move using a previously trained model stored in the file "keras_model.h5".
        A window is opened up and displays the user's camera with a countdown timer in the top left corner.
        The timer counts down from 6 seconds giving the user some time to display their move.
        The user's move is detected and output based on predictions from the model:
        1. The move is rock if the first prediction value is highest
        2. The move is scissors if the second prediction value is highest
        3. The move is paper if the third prediction value is highest
        4. The move is nothing if the fourth prediction value is highest
        '''

        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0) 
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        end = time.time() + 6  
        while end > time.time(): 
            ret, frame = cap.read() 
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) 
            # resizes image (input image, size, interpolation)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image
            prediction = model.predict(data) 
            # the predicted values from the model in a matrix
            cv2.putText(frame, f"{int(end - time.time())}", (100,150), cv2.FONT_HERSHEY_DUPLEX, 4, (255,0,0), 3) 
            cv2.imshow('User Move', frame) 
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
            # Press q to close the window
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
             
        cap.release() 
        # After the loop release the cap object
        cv2.destroyAllWindows() 
        # Destroy all the windows
    
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
            print("You won the round!")
            self.user_wins += 1 
        elif self.user_choice == computer_choice: 
            print("You drew the round!")
        else: 
            self.computer_wins += 1 
            print("You lost the round!")
        print(f"The score is {self.user_wins} - {self.computer_wins}.") 

game = Game() 

def play():
    '''
    Plays the game and checks for 2 things:
    1. If the user and computer both have less than 3 wins
    - the get_computer_choice, get_user_choice and get_winner methods are called to play the game
    2. The user or computer reaches 3 wins
    - the game ends and the user is given a message to choose whether to replay the game 
    ''' 

    while True:
        if game.user_wins < 3 and game.computer_wins < 3:
            game.get_user_choice() 
            game.get_winner() 
        else:  
            if game.user_wins == 3:    
                print("You won the game!")
            elif game.computer_wins == 3:
                print("You lost the game!")
            game.replay_choice = input("Would you like to play? Choose 'y' or 'n'.") 
            break  

def play_replay(): 
    '''
    Plays the game and gives the user an option to replay also.
    The play function is called and when the game ends, the user is given the choice to replay.
    1. If the user selects "y" (yes)
    - the user's and computer's wins are reset to 0 and the play function is called again
    2. If the user selects "n" (no)
    - the game ends 
    '''

    play() 
    while True:
        if game.replay_choice == "y": 
            game.user_wins = 0 
            game.computer_wins = 0
            play() 
        elif game.replay_choice == "n": 
            print("Thanks for playing!") 
            break

play_replay()
