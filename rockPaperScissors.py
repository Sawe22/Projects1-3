import random
from re import X

win = 0
lose = 0


#A function which returns True if the user wins, or returns false if the user loses
def result(human, computer):



    print(f"Computer chose {computer}")

    if human == 'rock':
        if computer == 'scissors' or computer == 'lizard':
            return True
    elif human == 'paper':
        if computer == 'spock' or computer == 'rock':
            return True
    elif human == 'scissors':
        if computer == 'paper' or computer == 'lizard':
            return True
    elif human == 'spock':
        if computer == 'rock' or computer == 'scissors':
            return True
    elif human == 'lizard':
        if computer == 'spock' or computer == "paper":
            return True
    return False
 

def game():

    global win

    global lose

    human_Play = ""

    #prompts the user to chose a valid option. 

    while True:
        try:
            human_Play = input("Choose either 'rock', 'paper', scissors', lizard', 'spock': ")
            if human_Play == 'rock' or human_Play == 'paper' or human_Play == 'scissors' or human_Play == 'lizard' or human_Play == 'spock':
                break
            else:
                print("Invalid input. Please chose valid option.")
        except:
            print("Invalid Input")
    #Has computer chose random choice
    computer_Play = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

    if human_Play == computer_Play:

        return 'Tie Game!'
    #Uses function to determine whether or not player has won
    if result(human_Play, computer_Play):

        print("You managed to win!")
        win+=1


    else:

        print("You lost hahhahahahahahhahahahaa rip!")
        lose+=1

#Asks the player if they want to play or not
while True:

    continue_Game = input("Would you like to Play Rock, Paper, Scissors, Lizard, Spock?(Y/N): ")
    if continue_Game == "y" or continue_Game == "Y":
        game()
    elif continue_Game == "N" or continue_Game == "n":
        print(f"You won {win} games and you lost {lose} games")
        break
    else:
        print("Invalid input")
