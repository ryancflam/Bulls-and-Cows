

# Bulls and Cows
**Bulls and Cows** - the classic paper-and-pencil logic game recreated in Python.

Want to improve your critical thinking skills? Play this game!

## What is Bulls and Cows?
**Bulls and Cows**, popularised as the board game **Mastermind**, is a code-breaking logic-based game where you try to guess a number that has been randomly generated by the program. the randomly generated number contains exactly four digits between 0 and 9 with no repeats.

Read more about Bulls and Cows here: https://en.wikipedia.org/wiki/Bulls_and_Cows

## Using the Module
First, you need to install the package.

```pip install bullsandcows```

Now in your project, import the package and create a new instance. We will be using ```game``` for this example, but you may use whatever name you want.

```
from bullsandcows import bullsandcows

game = bullsandcows()
```

This module has a feature that allows you to disable the anti-cheat *(prevents the user from getting the random number until the game stops)*, which is automatically enabled. You can send a boolean variable to the bullsandcows instance which determines whether the anti-cheat should be enabled or not. The first method below disables it upon instantiation.

```
game = bullsandcows(anticheat=False)
```

The second method below disables it post-instantiation, for whatever reason.

```
game.anticheat = False
```

```game.anticheat``` itself is a boolean value which you can use for other things such as displaying on the console. Once the anti-cheat is disabled, you may retrieve the random number as string using ```get_number()``` whenever you wish to.

Using ```get_number()``` without disabling the anti-cheat will raise an exception if the game is still in progress.

**```guess(value)```**:

Gets and verifies a user's guess. Requires the user to parse a ```value```, which must either be a four-digit number with no repeated digits such as 1234, or the following exit commands which are for forcibly stopping the game: 'exit', 'stop', 'halt', 'quit' *(case-insensitive)*.

Function returns two values in order: number of bulls *(integer)*, number of cows *(integer)*. Sample usage:

```
value = input("Guess a number: ")
bulls, cows = game.guess(value)
print("Bulls:",bulls)
print("Cows:",cows)
```

**```get_time()```**:

Gets the total time spent by the player and converts it to minutes and seconds.

Function returns two values in order: minutes *(integer)*, seconds *(integer; is reset to 0 every 60 seconds)*. Sample usage:

```
mins, secs = game.get_time()
print(f"Total time spent: {mins} min & {secs} sec.")
```

**Other Getters**:

```get_attempts()``` - Returns the total number of attempts used; integer value.

```get_stopped_bool()``` - Returns the game stopping indicator value; boolean value.

```get_won_bool()``` - Returns the game winning indicator value; boolean value.

## Gameplay
In the game, the player is asked to enter a four-digit number which is then compared to the randomly generated four-digit number; each individual digit entered by the player is compared to each digit within the randomly generated number. If a digit in the player's guess is in the randomly generated number and is in the **same position** in it as it was in their number, then it is scored as a **'bull'**. If that same digit is in a **different position**, then it is marked as a **'cow'**.

The objective of the game is to obviously find all four bulls in the shortest amount of time and using as few attempts as possible.

Example of a valid guess: 1234

Example of an invalid guess: 1244 *(the digit 4 has been used twice when it can only be used once)*

Another example of an invalid guess: 12345 *(five digits instead of four)*

**Example Guess**:

Randomly generated number: 1234

Your guess: 1324

Result: 2 bulls and 2 cows. *(bulls: 1 and 4; cows: 2 and 3)*
