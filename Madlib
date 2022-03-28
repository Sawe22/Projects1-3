#These are global variable declarations
noun = ""
adjective = ""
pluralNoun = ""
partOfBody = ""
number = ""
aPlace = ""
ingVerb = ""

#A function which asks the user to input values into the above global variables
def ask():
    global noun, number, adjective, pluralNoun, partOfBody, aPlace, ingVerb 
    noun = input("Noun: ")
    adjective = input("adjective: ")
    pluralNoun = input("Plural Noun: ")
    partOfBody = input("Part of Body: ")
    number = input("Number: ")
    aPlace = input("A Place: ")
    ingVerb = input("A Verb Ending In 'ing': ")

#Below are three methods of creating functions which incorporate the global variables.
def storyLine1():
    print(f"The creature left not a single {noun} behind. It massacred {aPlace} and its {adjective} {partOfBody} siezed the souls of many innocent \
people; leaving only {number} survivors. Certainly, they will be left to {ingVerb} for the rest of eternity; having only {pluralNoun} to accompany them.")
def storyLine2():
    print("Nobody could stand the " + noun + ". As a result, the " + partOfBody +\
        " of some " + adjective + " guy started " + ingVerb + ", so he had to go to " + aPlace + " to get that sorted out." +\
        " Forutnately, he found many " + pluralNoun + " there and he died happy.")
def storyLine3():
    print("{}".format(number) + " people are {}".format(ingVerb) + " as a result of the {}".format(adjective) + " {}".format(pluralNoun + " which \
were found in "+"{}".format(aPlace) + ". Currently, everyone had decided to discard of every {}".format(noun\
        )) + " in thier homee, and as a result of emotional damage, they are making sure that thier {}".format(partOfBody) + " is fully functioning.")
#A series of if statements which asks the user for valid input until is given
while True:
    storyLine = str(input("Which story do you want to play ('1', '2', '3'. 'q' to quit)?: "))
    if storyLine == "1":
        ask()
        break
    elif storyLine == "2":
        ask()
        break
    elif storyLine == "3":
        ask()
        break
    elif storyLine == "q":
        print("You quit")
        break
    else:
        print ("Invalid input. Select '1', '2' or '3'")

#If statements which play a function definition based on user input
if storyLine == "1":
    storyLine1()
elif storyLine == "2":
    storyLine2()
elif storyLine == "3":
    storyLine3()
