# Bulls and Cows
Bulls and Cows - the classic pen-and-paper logic game recreated in Python.

## What is Bulls and Cows?
Bulls and Cows is a logic game where you try to guess a number that has been randomly generated by the programme. The randomly-generated number must contain exactly four digits between 0 and 9 with no duplicates.

Example of a valid number: 1234
Example of an invalid number: 1244 (The number 4 has been used twice when it can be only used once.)

In the game, you are asked to enter a four-digit number. This is then compared to the randomly-generated four-digit number. Each individual digit entered by you is compared to each digit within the randomly-generated number. If a digit is in the randomly-generated number and is in the same position in the randomly-generated number as it was in your number, you have found a bull. If the digit is in the randomly-generated number but is in a different position, then you have found a cow. The goal is to obviously find all four bulls.

**Example:

Randomly-generated number: 1234

Your guess: 1324

Result: 2 bulls and 2 cows. (Bulls: 1 and 4, cows: 2 and 3.)

*Made by CloroxEnergyDrink of 3CP Studios.
