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

#print(score[0], score[1], score[2], score[3])

def title():
    """
    This is the title page with rules
    """
    print(f"\033[33m{title2}\033[0m")
    print("Here are the rules!")
    print("Here are the rules! Here are the rules!")
    print("Here are the rules! Here are the rules!")
    print("Here are the rules! Here are the rules!")
    print("Here are the rules! Here are the rules!")
    print("Here are the rules! Here are the rules!")
    print("Here are the rules! Here are the rules!")
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
        print("Choose your category:")
        select = input("Press 1 for Spells\nPress 2 for Magical Creatures and Beasts\nPress 3 for Dark Arts\n> ")
        if select == "1":
            category = "spells"
            os.system("clear")
            break
        elif select == "2":
            category = "beasts"
            os.system("clear")
            break
        elif select == "3":
            category = "dark"
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
    if category == "spells":
        list = spells
    elif category == "beasts":
        list = beasts
    elif category == "dark":
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
            #prints score
            print(nagini(tries))
            print("Didn't you try that one? Or it's already in there!")
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
                print(nagini(tries))
                print("Yep! It's in there!")
            else:
                tries -= 1       
                print(nagini(tries))
                print("Nope, not in there!")
        else:       
            if letter == word:
                print(nagini(tries))
                print("Yep! That's it!")
            else:
                tries -= 1     
                print(nagini(tries))
                print("Nope, not right!")

        
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
            print("I didn't understand that. Play again? y/n > ")
            os.system("clear")

start() 


