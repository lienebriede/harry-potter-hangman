#librairies
import random
import os
import time

#other files
from spellsList import spells
from beastsList import beasts
from darkArtsList import darkArts
from title2 import title2
from score import nagini


def title():
    """
    This is the title page with rules
    """
    print(f"\033[33m{title2}\033[0m")
    print("Here are the rules!")
    print("Guess the given word either letter by letter or the whole word at once!")
    print("There are 3 categories you can choose from.")
    print("The first letter is always given (and if that same letter repeats in the word,")
    print("that is given too)!")
    print("You're only allowed 3 wrong guesses before Nagini wakes up and you lose.")
    print("Don't know what Nagini is? Well, good luck then!")
    print("Have fun!")
    while True:
        enter = input("Press enter to start the game...")
        if enter == "":
            os.system("clear")
            break
        else:
            continue

def chooseCategory():
    """
    Allows user to choose a word 
    from 3 different categories
    """
    while True:
        print()
        print("Choose your category:")
        select = input("Press 1 for Spells\nPress 2 for Magical Creatures and Beasts\nPress 3 for Dark Arts\n> ")
        if select == "1":
            category = "Spells"
            os.system("clear")
            break
        elif select == "2":
            category = "Magical Creatures and Beasts"
            os.system("clear")
            break
        elif select == "3":
            category = "Dark Arts"
            os.system("clear")
            break
        else:
            os.system("clear")
            print("I didn't understand that. Try again!")
            
    return category

def randomWord(category):
    """
    Takes a random word from a list
    from a category that user chose to play
    """
    if category == "Spells":
        list = spells
    elif category == "Magical Creatures and Beasts":
        list = beasts
    elif category == "Dark Arts":
        list = darkArts 

    word = random.choice(list)
    return word

def play():
    """
    This is the game code, provides a random word,
    checks user input, keeps score
    """
    
    triedLetters =[]
    tries = 3

    #categories
    category = chooseCategory()

    #score at 0 position
    print(nagini(tries))

    #gives random word
    word = randomWord(category)

    #reveals the first letter (and others if the same)
    triedLetters.append(word[0])


    print(f"\033[36mCategory '{category}'\033[0m")
    print()

    #prints the word
    for i in word:
        if i in triedLetters or word in triedLetters:
            print(i, end=" ")
        else:
            print("_", end=" ")
    
    print()
    print()
    print(f"\033[31m{tries} wrong tries and Nagini wakes up!\033[0m")
    print()

    while True:
        letter = input("Guess a letter or the word!\n> ").lower()
        os.system("clear")
        
        if letter in triedLetters:
            #prints score
            print(nagini(tries))
            print("Didn't you try that one? Or maybe it's already in there?!")
            print()
            #prints the word
            for i in word:
                if i in triedLetters or word in triedLetters:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print()
            print()
            continue
        #adds picked letters to the list    
        triedLetters.append(letter)
        
        #checks both - input letter and input word
        if len(letter) == 1:
            if letter in word:  
                print(nagini(tries))
                print("Yep! It's in there!")
                print()
            else:
                tries -= 1       
                print(nagini(tries))
                print("Nope, not in there!")
                print()
        else:       
            if letter == word:
                print(nagini(tries))
                print("Yep! That's it!")
                print()
            else:
                tries -= 1     
                print(nagini(tries))
                print("Nope, not right!")
                print()

        
        #need this boolean to check if word is guessed and break out of the loop    
        gotAllLetters = True    
        
        #prints the guessed letters that are in the word
        for i in word:
            if i in triedLetters or word in triedLetters:
                print(i, end=" ")
            else:
                print("_", end=" ")
                gotAllLetters = False
        print()
        print()

        #breaks out of the loop, guessed word
        if gotAllLetters:
            print("You guessed the word!")
            print()
            break
        #breaks out of the loop, out of tries
        if tries <= 0:
            print(f"Too bad! No more tries left!\nThe word was \033[36m{word}\033[0m.")
            print()
            break
        else:
            if tries == 1:
                print(f"\033[31mOnly {tries} wrong try and Nagini wakes up!!!\033[0m")
                print()
            else:
                print(f"\033[31m{tries} wrong tries and Nagini wakes up!\033[0m")
                print()
           

def start():
    """
    Starts the game and after finishing
    user chooses to play another word or stop
    """
    title()
    play()
    while True:
        again = input("Play again? y/n > ").lower()
        if again == "y":
            os.system("clear")
            play()
        elif again == "n":
            os.system("clear")
            print("OK! Hope you enjoyed it!")
            break
        else:
            os.system("clear")
            print("I didn't understand that.")
            

start() 


