"""
Bulls and Cows
Python 3.6
"""

import random
import time

PLAYAGAIN=True


class BullsAndCows:
    """
    Object initialisation.
    Marks the starting unix timestamp, sets the number of attempts to 0, and calls the random number generation method.
    """
    def __init__(self):
        self.__start=time.time()
        self.attempts=0
        self.number=self.__random_number()

        # Only uncommented for testing purposes.
        # print(self.number)

    """
    Method for generating random numbers; automatically called upon object initialisation.
    Function variable returns in order:
    1. Four-digit number (str).
    """
    @staticmethod
    def __random_number():
        a,b=random.randint(0,9),random.randint(0,9)
        while b==a: # While the new digit is the same as the previous one. Same for the other while loops here.
            b=random.randint(0,9)
        c=random.randint(0,9)
        while c==a or c==b:
            c=random.randint(0,9)
        d=random.randint(0,9)
        while d==a or d==b or d==c:
            d=random.randint(0,9)
        return"{}{}{}{}".format(a,b,c,d)

    """
    Counts and returns the number of bulls and cows found in a player's guess.
    Function variable returns in order:
    1. Number of bulls (int),
    2. number of cows (int),
    3. if the player has won or not (bool).
    """
    def bull_counter(self,guess):
        if len(guess)!=4:
            raise ValueError("Number must contain exactly four digits.")
        bulls,cows=0,0
        try: # Tries to put each individual entered character into four separate int variables.
            aa,bb,cc,dd=int(guess[0]),int(guess[1]),int(guess[2]),int(guess[3])
            if aa==bb or aa==cc or aa==dd or bb==cc or bb==dd or cc==dd:
                raise ValueError("Duplicates found.")
            else:
                for i in guess:
                    for j in self.number:
                        if i==j:
                            if guess.index(i)==self.number.index(j):
                                bulls+=1
                            else:
                                cows+=1
            self.attempts+=1
            return bulls,cows,True if bulls==4 else False
        except ValueError: # If str-to-int conversion fails.
            raise ValueError("Invalid characters found.")

    """
    Prints the total time elapsed when called.
    Function variable returns in order:
    1. Minutes (int),
    2. seconds (int).
    """
    def display_time(self):
        seconds=int(time.time()-self.__start)
        minutes=int(seconds//60)
        seconds-=(minutes*60)
        return int(minutes),int(seconds)

"""
Main game function.
Function variable returns in order:
1. If the user wishes to play the game again or not (bool).
"""
def main():
    won,game=False,BullsAndCows()
    while not won:
        guess=input("\nAttempt {} - Guess a four-digit number (Enter 'exit' to quit): ".format(game.attempts+1))
        if str(guess).casefold()=="quit"or str(guess).casefold()=="exit"or str(guess).casefold()=="stop":
            print("\n. . .\n\nThe number was {}.\n\nTotal attempts: {}".format(game.number,game.attempts))
            minutes,seconds=game.display_time()
            print("\nTime spent: {} minute{} and {} second{}.".format(minutes,""if minutes==1 else"s",seconds,""if seconds==1 else"s"))
            return False
        else:
            try:
                bulls,cows,won=game.bull_counter(guess) # The returned values are assigned to these variables in order.
                print("\nResult: {} bull{} and {} cow{}.".format(bulls,""if bulls==1 else"s",cows,""if cows==1 else"s"))
            except Exception as e:
                print("\n[ERROR] {}".format(e))
    print("\n. . .\n\nCongratulations, you have guessed the number.\n\nTotal attempts: {}".format(game.attempts))
    minutes,seconds=game.display_time()
    print("\nTime spent: {} minute{} and {} second{}.".format(minutes,""if minutes==1 else"s",seconds,""if seconds==1 else"s"))
    playAgain=input("\nPlay again? (Enter '1' to play again): ")
    return True if playAgain else False

# This piece of code will only run in this file and will not run if imported as an external source.
if __name__=="__main__":
    while PLAYAGAIN:
        print("\n. . .\n\n== Bulls and Cows ==")
        PLAYAGAIN=main()
