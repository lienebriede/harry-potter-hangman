import random
import os
import time
from wordlist import wordList
from title2 import title2

print(f"\033[33m{title2}\033[0m")
def randomWord():
    """
    Takes a random word from the list
    """
    word = random.choice(wordList)
    return word

def play():
    """
    This is the game code, provides a random word,
    checks user input, keeps score
    """
    
    triedLetters =[]
    tries = 3

    
    word = randomWord()
    #reveals the first letter
    triedLetters.append(word[0])

    print(f"You have {tries} tries to guess the word!")
    #time.sleep(2)
    #os.system("clear")

    print("Your word is:")
    print()

    #prints the word
    for i in word:
        if i in triedLetters or word in triedLetters:
            print(i, end=" ")
        else:
            print("_", end=" ")

    print()
    print()

    while True:
        letter = input("Guess a letter > ").lower()
        os.system("clear")
        
        if letter in triedLetters:
            print("You tried that one already!")
            #prints the word
            for i in word:
                if i in triedLetters or word in triedLetters:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            continue

        #adds picked letters to the list    
        triedLetters.append(letter)

        #checks both - input letter and input word
        if len(letter) == 1:
            if letter in word:
                print("Yep! It's in there!")
            else:
                print("Nope, not in there!")
                #takes off score
                tries -= 1
        else:
            if letter == word:
                print("Yep! That's it!")
            else:
                print("Nope, not right!")
                #takes off score
                tries -= 1

        #need this boolean to check if word is guessed and break out of the loop    
        gotAllLetters = True    
        
        #prints the guessed letters that are in the word
        for i in word:
            if i in triedLetters or word in triedLetters:
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
            print(f"Too bad! No more tries left! The word was {word}.")
            break
        else:
            if tries == 1:
                print(f"You've got only {tries} try left!!")
            else:
                print(f"You've got {tries} tries left!")
           

def start():
    """
    Starts the game and after finishing
    user chooses to play another word or stop
    """
    play()
    while True:
        again = input("Play again? y/n > ").lower()
        if again == "y":
            play()
        elif again == "n":
            print("OK! Hope you enjoyed it!")
            break
        else:
            print("I didn't understand that. Play again? y/n > ") 

start() 


