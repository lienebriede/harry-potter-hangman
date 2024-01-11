import random, os, time

def play():

    wordList = ["unicorn", "phoenix"]
    triedLetters =[]
    tries = 3

    #takes a random word from the list
    word = random.choice(wordList)

    print(f"You have {tries} tries to guess the word!")
    time.sleep(2)
    os.system("clear")

    print("Your word is:")
    print()

    #prints the word
    for i in word:
        print("_", end=" ")

    print()
    print()

    while True:
        letter = input("Guess a letter > ").lower()
        os.system("clear")
        
        if letter in triedLetters:
            print("You tried that one already!")
            continue

        #adds picked letters to the list    
        triedLetters.append(letter)

        if letter in word:
            print("Yep! It's in there!")
        else:
            print("Nope, not in there!")
            #takes off score
            tries -= 1

        #need this boolean to check if word is guessed and break out of the loop    
        gotAllLetters = True    
        
        #prints the guessed letters that are in the word
        for i in word:
            if i in triedLetters:
                print(i, end=" ")
            else:
                print("_", end=" ")
                gotAllLetters = False

        #breaks out of the loop, guessed word
        if gotAllLetters:
            print("You guessed the word!")
            break
        #breaks out of the loop, out of tries
        if tries <= 0:
            print(f"Too bad! No more tries left!")
            break
        else:
            if tries == 1:
                print(f"You've got only {tries} try left!!")
            else:
                print(f"You've got {tries} tries left!")

while True:
    again = input("Play again? y/n > ").lower()
    if again == "y":
        play()
    elif again == "n":
        print("OK! Hope you enjoyed it!")
        break
    else:
        print("I didn't understand that. Play again? y/n > ")  

