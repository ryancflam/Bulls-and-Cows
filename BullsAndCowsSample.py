"""
Bulls and Cows
Python 3.6
Requires bullsandcows (pip install bullsandcows)
"""

from time import sleep
from bullsandcows import bullsandcows


def display_time(game): # Appropriately displays the total time spent by the player. BullsAndCows() object is passed.
    minutes,seconds = game.get_time()
    print("\nTime spent: {} minute{} and {} second{}.\n".format(minutes,"" if minutes == 1 else "s",seconds,"" if seconds == 1 else "s"))

def main(): # Main game function.
    game = bullsandcows()
    print("\n. . .\n\n==  Bulls and Cows  ==")

    while not game.get_won_bool():
        value = input("\nAttempt {} - Guess a four-digit number (Enter 'exit' to quit): ".format(game.get_attempts()+1))
        try:
            bulls,cows = game.guess(value) # Submits a user's guess and checks for bulls and cows.
            if game.get_stopped_bool()and not game.get_won_bool(): # If the game has been manually stopped.
                print("\n. . .\n\nThe number was {}.\n\nTotal attempts: {}".format(game.get_number(),game.get_attempts()))
                display_time(game)
                sleep(3) # Waits 3 seconds before stopping the program so the user can view game statistics.
                return False
            print("\nResult: {} bull{} and {} cow{}.".format(bulls,"" if bulls == 1 else "s",cows,"" if cows == 1 else "s"))
        except Exception as e:
            print("\n[ERROR] {}".format(e)) # Any exception raised will be printed appropriately here.

    print("\n. . .\n\nCongratulations, you have guessed the number.\n\nTotal attempts: {}".format(game.get_attempts()))
    display_time(game)
    playAgain = input("Play again? (Enter '1' to play again): ")
    return True if str(playAgain) == "1" else False

# This piece of code will only run in this file and will not run if imported as an external source.
if __name__ == "__main__":
    inGame = True
    while inGame:
        inGame = main() # The function returns either True, if the player wishes to play the game again, or False, if not.
