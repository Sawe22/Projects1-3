import random


#A functions which prints out 'LAIR' in big letters
def you_lied():

    print('\033[0;31;40m')
    print("")
    print("")
    print("██╗░░░░░██╗░█████╗░██████╗░")
    print("██║░░░░░██║██╔══██╗██╔══██╗")
    print("██║░░░░░██║███████║██████╔╝")
    print("██║░░░░░██║██╔══██║██╔══██╗")
    print("███████╗██║██║░░██║██║░░██║")
    print("╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝")
    print("")
    print('\033[0;32;40m') 

#Function which has the computer guess numbers
def computerGuess(max):


    print('\033[0;32;40m') 
    min = 1
    print("")
    print("")
    print("") 
    print("░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗████████╗███████╗██████╗░")
    print("██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗")
    print("██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝")
    print("██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗")
    print("╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░╚██████╔╝░░░██║░░░███████╗██║░░██║")
    print("░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
    print("")
    print("░██████╗░██╗░░░██╗███████╗░██████╗░██████╗███████╗██████╗░")
    print("██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗")
    print("██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░█████╗░░██████╔╝")
    print("██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗")
    print("╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝███████╗██║░░██║")
    print("░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝")
    print("")
    print("")
    print("")
    print("")

#Makes user pick a valid number input
    while True:
        try:
            hidden_value = int(input(f"Pick a secret number between {min} and {max}: "))
            if hidden_value > max or hidden_value < min:
                print("Invalid Parameters")
            else:
                break

        except:
            print("Invalid input")

    user_Response = "Anything"

#Makes user answer computers questions and ensures that they correctly answer
    while user_Response != "C" or user_Response != "c":

        while user_Response != "C" or user_Response != "c":

            computer_Prediction = random.randint(min, max)

            user_Response = input((f"I guessed {computer_Prediction}, is this too low (L), too high(H), or correct (C)?: "))

            if user_Response == "L" or user_Response == "l":
                prev_Min = min

                min = computer_Prediction + 1

                #print (f"Min is {min}")

                if min > hidden_value:

                    you_lied()

                    min = prev_Min

                break

            elif user_Response == "H" or user_Response == "h":
                prev_Max = max
                max = computer_Prediction - 1

                #print (f"max is {max}")

                if max < hidden_value:
                    you_lied()
                    max = prev_Max
                break

            elif user_Response == "C" or user_Response == "c":

                if computer_Prediction == hidden_value:

                    print("")
                    print("")
                    print("")
                    print("Yay. I am good at guessing. Please play again.")
                    print("")
                    print("")
                    print("")

                    return 3
                else:
                    you_lied()
                    user_Response == "x"
            else:
                    print("I don't understand. Please give me a valid input")
def randomNumber(number):



    print('\033[2;32;40m') 

    print("")
    print("")
    print("")
    print("███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░")
    print("████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗")
    print("██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")
    print("██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")
    print("██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")
    print("╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")
    print("")
    print("░██████╗░██╗░░░██╗███████╗░██████╗░██████╗███████╗██████╗░")
    print("██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗")
    print("██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░█████╗░░██████╔╝")
    print("██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗")
    print("╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝███████╗██║░░██║")
    print("░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝")
    print("")
    print("")


    generated_Number = int(random.randint(1, number))
    predicted_Number = 0

    x = 3.141592

    while x != 7:
        try:
            predicted_Number = int(input (f"Guess a number between 1 and {number}: "))
            x = 7
        except:
            print("Invalid input")


    while generated_Number != predicted_Number:
        if predicted_Number > generated_Number:
            print ("Too high!!")
            while True:
                try:
                    predicted_Number = int(input (f"Guess a number between 1 and {number}: "))
                    break
                except:
                    print("Invalid Input")
        elif predicted_Number < generated_Number:
            print("Go higher")
            predicted_Number = int(input (f"Guess a number between 1 and {number}: "))
    print("")
    print("")
    print (f"Good job, you guessed the secret number: {generated_Number}. Please play again.")
    print("")
    print("")
while True:
    #Code which determines which game the user wants to play
    chosen_path = str(input("Press '1' if you want to guess a number. Press '2' if you want the computer to guess a number (q to quit): "))
    if chosen_path == "1":
        randomNumber(100)
    elif chosen_path == "2":
        computerGuess(100)
    elif chosen_path == "q":
        print("You have quit program")
        break
    else:
        print("Invalid input ")
