import random
from random import randint
from time import sleep
userScore = 0
compScore = 0
ties = 0
rounds = 0
game = True
play1 = randint(0, 5)
play2 = randint(0, 5)

#captalize(input)
if(play1 == play2):
    print("404: Page Not Found")
    game = False
else:
    print("Congrats! Your game didn't glitch this time!")
    print("\nLet's play rock, paper, scissors!\n")
while(game):
    choice = str.lower(input("Pick Rock, Paper, or Scissors. "))
    compChoice = random.choice(["Rock", "Paper", "Scissors"])
    userChoice = ""
    good = False
    if(("rock" in choice)):
        userChoice = "Rock"
        good = True
    elif(("paper" in choice)):
        userChoice = "Paper"
        good = True
    elif(("scissors" in choice)):
        userChoice = "Scissors"
        good = True
    else:
        print("Invalid input. Please check your spelling and ensure you have inputted either rock, paper, or scissors.")

    if(good):
        print(f"Computer chose {compChoice}\n")
        sleep(2)
        print("Doing immense calculations...")
        sleep(2)
        print("Thinking very hard...")
        sleep(2)
        #print("Collecting large amounts of data...")
        #sleep(2)
        print("Loading...\n")
        sleep(1)

        if(compChoice == "Rock" and userChoice == "Rock"):
            print("Rock and Rock tie.")
            ties += 1
        elif(compChoice == "Rock" and userChoice == "Paper"):
            print("Paper beats Rock. User wins.")
            userScore += 1
        elif(compChoice == "Rock" and userChoice == "Scissors"):
            print("Rock beats Scissors. Computer wins.")
            compScore += 1
        elif(compChoice == "Paper" and userChoice == "Rock"):
            print("Paper beats Rock. Computer wins.")
            compScore += 1
        elif(compChoice == "Paper" and userChoice == "Paper"):
            print("Paper and Paper tie.")
            ties += 1
        elif(compChoice == "Paper" and userChoice == "Scissors"):
            print("Scissors beats Paper. User wins.")
            userScore += 1
        elif(compChoice == "Scissors" and userChoice == "Rock"):
            print("Rock beats Scissors. User wins.")
            userScore += 1
        elif(compChoice == "Scissors" and userChoice == "Paper"):
            print("Scissors beats Paper. Computer wins.")
            compScore += 1
        elif(compChoice == "Scissors" and userChoice == "Scissors"):
            print("Scissors and Scissors tie.")
            ties += 1

        rounds += 1

        print(f"Computer: {compScore} Player: {userScore}")
        print(f"Round played: {rounds}")
        print(f"Ties: {ties}")

        sleep(2)

        print("\nPlay again?")
        goAgain = str.lower(input(""))

        if(("yes" in goAgain)):
            print("Great!")
        elif(("no" in goAgain)):
            print("Thanks for playing! Come back again!")
            print(f"Final Score\nComputer: {compScore} Player: {userScore}")
            game = False
