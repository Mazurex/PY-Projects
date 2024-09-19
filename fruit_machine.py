# Libraries
from random import *
from time import *
# Creating a function
def roll ():

    # The user decides the amount of betting money
    try:
        cash = int(input("ENTER MONEY: "))
    except ValueError:
        print ("You can only input a number!")
        return


    # All possible outcomes
    reel = ["🍒", "🔔", "🔥"]

    # Repeat until user runs out of cash
    while cash >0:

        # Subtract 1 from cash
        cash = cash - 1

        # Create 4 random options
        reel1 = choice(reel)
        reel2 = choice(reel)
        reel3 = choice(reel)
        reel4 = choice(reel)

        # Print the results
        print(reel1, "  ", reel2, "  ", reel3, "  ", reel4, "  ")
        sleep (1)

        # Check if the user has jackpot
        if (reel1) == (reel2) and (reel1) == (reel3) and (reel1) == (reel4):
            print("\n🎉🎉 JACKPOT!! 🎉🎉")
            cash = cash + 10
            if (reel1) == ("🍒") and (reel2) == ("🍒") and (reel3) == ("🍒") and (reel4) == ("🍒"):
                print("4 CHERRIES = 5 EXTRA CREDITS")
                cash = cash + 5
                sleep (0.5)
            if (reel1) == ("🔔") and (reel2) == ("🔔") and (reel3) == ("🔔") and (reel4) == ("🔔"):
                print("4 BELLS = 10 EXTRA CREDITS")
                cash = cash + 10
                sleep (0.5)
            if (reel1) == ("🔥") and (reel2) == ("🔥") and (reel3) == ("🔥") and (reel4) == ("🔥"):
                print("4 LEMONS = 15 EXTRA CREDITS")
                cash = cash + 15
                sleep (0.5)
            print()
            print()
            
                
        # Print remaining cash
        print("💰 CASH LEFT", cash)
        print()
        print()

    print ("NO CREDITS LEFT...")

    # Ask if the user wants to play again
    print("Play again? Y/N")
    answer = input()
    if (answer == "Y"):
        roll()
    else:
        print("Thank you for playing! Please Gamble responsibly!")
roll()