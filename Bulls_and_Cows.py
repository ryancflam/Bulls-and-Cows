# Copyright (C) 3CP Studios.
print("\nStarting programme...\n\n. . .")
import random,time
time.sleep(1)
print("\nWelcome to Bulls and Cows.")
def randomnumber():
    global a,b,c,d
    a=random.randint(0,9)
    b=random.randint(0,9)
    while b==a:
        b=random.randint(0,9)
    c=random.randint(0,9)
    while c==a or c==b:
        c=random.randint(0,9)
    d=random.randint(0,9)
    while d==a or d==b or d==c:
        d=random.randint(0,9)
    number=str("{}{}{}{}".format(a,b,c,d))
    return number
def game():
    startTime=time.time()
    cows=0
    bulls=0
    number=str(randomnumber())
    count=1
    guess=str(input("\nGuess a four-digit number (Input 'exit' to exit, or 'help' for help): "))
    while guess!=number:
        if len(guess)!=4:
            print("\n[ERROR] You must input exactly four numbers.")
        if guess=="exit":
            seconds_in_minute=60
            seconds=int(time.time()-startTime)
            minutes=int(seconds//seconds_in_minute)
            seconds=int(seconds-(minutes*seconds_in_minute))
            print(f"\n. . .\n\nThe number was {number}.\n\nTotal attempts: {count-1}\n")
            if minutes==1 and seconds==1:
                print(f"Time spent: {minutes} minute and {seconds} second.\n\n. . .")
            if minutes!=1 and seconds!=1:
                print(f"Time spent: {minutes} minutes and {seconds} seconds.\n\n. . .")
            if minutes!=1 and seconds==1:
                print(f"Time spent: {minutes} minutes and {seconds} second.\n\n. . .")
            if minutes==1 and seconds!=1:
                print(f"Time spent: {minutes} minute and {seconds} seconds.\n\n. . .")
            print("\nThank you for playing Bulls and Cows.\n\nExiting in 3 seconds...\n\n.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\nStopping programme...\n")
            exit()
        if guess=="help":
            print("\n. . .\n\n== Bulls and Cows ==\n\nBulls and Cows is a number guessing game where you try to guess a number that has been\nrandomly generated.\n\nThe randomly generated number contains exactly four digits between 0 and 9\nwith no repeats.\n\nExample of a valid guess: 1234\nExample of an invalid guess: 1444 (The number 4 has been used three times when you\ncan only use it once.)\n\nIn the game, you are asked to enter a four-digit number which is then compared to the randomly\n-generated four-digit number. Each individual digit entered by you is compared to each digit\nwithin the randomly-generated number. If a digit is in the randomly-generated number and is in\nthe same position in the randomly-generated number as it was in your number, then you have\nfound a bull. If the digit is in the randomly-generated number but is in a different position,\nthen you have found a cow.\n\nYour goal is to find all four bulls in the shortest amount of time and using as little\nattempts as possible.\n\nExample:\nRandomly-generated number: 1234\nYour guess: 1324\nResult: 2 bulls and 2 cows. (Bulls: 1 and 4, cows: 2 and 3.)\n\n. . .")
            try:
                goback=input("\nEnter a number to go back: ")
                count-=1
            except:
                count-=1
                continue
        if len(guess)==4 and guess!="help":
            try:
                aa=int(guess[0])
                bb=int(guess[1])
                cc=int(guess[2])
                dd=int(guess[3])
                if aa==bb or aa==cc or aa==dd or bb==cc or bb==dd or cc==dd:
                    print("\n[ERROR] Duplicates found. Please try again.")
                else:
                    for xx in guess:
                        for yy in number:
                          if xx==yy:
                            if guess.index(xx)==number.index(yy):
                              bulls+=1
                            else:
                              cows+=1
                    print("")
                    if bulls==1 and cows!=1:
                        print(f"Result: {bulls} bull and {cows} cows.")
                    if cows==1 and bulls!=1:
                        print(f"Result: {bulls} bulls and {cows} cow.")
                    if cows==1 and bulls==1:
                        print(f"Result: {bulls} bull and {cows} cow.")
                    if cows!=1 and bulls!=1:
                        print(f"Result: {bulls} bulls and {cows} cows.")
                    cows=0
                    bulls=0
            except:
                print("\n[ERROR] Invalid characters. Please try again.")
        count+=1
        guess=str(input("\nGuess a four-digit number (Enter 'exit' to exit, or 'help' for help): "))
    seconds_in_minute=60
    seconds=int(time.time()-startTime)
    minutes=int(seconds//seconds_in_minute)
    seconds=int(seconds-(minutes*seconds_in_minute))
    print(f"\nResult: 4 bulls!\n\n. . .\n\nCongratulations, you have guessed the number.\n\nTotal attempts: {count}\n")
    if minutes==1 and seconds==1:
        print(f"Time spent: {minutes} minute and {seconds} second.\n\n. . .")
    if minutes!=1 and seconds!=1:
        print(f"Time spent: {minutes} minutes and {seconds} seconds.\n\n. . .")
    if minutes!=1 and seconds==1:
        print(f"Time spent: {minutes} minutes and {seconds} second.\n\n. . .")
    if minutes==1 and seconds!=1:
        print(f"Time spent: {minutes} minute and {seconds} seconds.\n\n. . .")
    playagain=int(input("\nWould you like to play again?\n\nEnter 1 to play again, or any other number to quit.\n\nYour choice: "))
    while playagain==1:
        print("\n. . .")
        game()
    print("\n. . .\n\nThank you for playing Bulls and Cows.\n\nExiting in 3 seconds...\n\n.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("\nStopping programme...\n")
    exit()
game()
