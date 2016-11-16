#hangman_evan.py
#Evan Budelmann
#10/20/16

import os
import random

def show_start_screen():
    print("""

      ,%%%%%%%%,
     %%o%%/%%%%%%
    %%%%\%%%<%%%%%
    %%>%%%/%%%%o%%
    %%%%%o%%\%%//%
    %\o%\%%/%o/%%'
     '%%\ `%/%%%'
       '%| |%|%'
         | | (O
         | | |\\
         | | >>
         | |
        /   \\
    ^^^^^^^^^^^^^^^^^""")


    print("""
 _,_  _, _, _  _, _, _  _, _, _
 |_| /_\ |\ | / _ |\/| /_\ |\ |
 | | | | | \| \ / |  | | | | \|
 ~ ~ ~ ~ ~  ~  ~  ~  ~ ~ ~ ~  ~
                               """)
    
def show_credits():
    print("""
 ___ _,_  _, _, _ _,_  _,   __,  _, __,   __, _,   _, , _ _ _, _  _,
  |  |_| /_\ |\ | |_/ (_    |_  / \ |_)   |_) |   /_\ \ | | |\ | / _
  |  | | | | | \| | \ , )   |   \ / | \   |   | , | |  \| | | \| \ /
  ~  ~ ~ ~ ~ ~  ~ ~ ~  ~    ~    ~  ~ ~   ~   ~~~ ~ ~   ) ~ ~  ~  ~ 
                                                       ~'
  By: Evan Budelmann                                                     """)

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + '/' + f

        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)
    choice = choice - 1
    return path + "/" + files[choice]

def get_puzzle(file):

    with open(file, 'r') as f:
        words = f.read().splitlines()
    
    return random.choice(words[1:]).upper()
      
def check(word, solved, correct):
    for i in range(len(word)):
            if word[i] in correct or not word[i].isalpha():
                solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():

    accept = False

    while accept == False:
        guess = input("Guess a letter: ")
        guess = guess.upper()
        if len(guess) == 1:
            accept = True
            return guess
        else:
            print("Please enter only 1 letter")
            accept = False
            
def display_board(solved, incorrect, strikes, word):
    if strikes == 0:
        print("""
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___""")
    elif strikes == 1:
        print("""
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___ """)
    elif strikes == 2:
        print("""
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___""")
    elif strikes == 3:
        print("""
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      
     |
    _|___""")
    elif strikes == 4:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___ """)
    elif strikes == 5:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___""")
    elif strikes == 6:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
""")
        print(word)
    print(solved + " [" + incorrect + "]")


def play_again():
    while True:
        again=input("Would you like to play again?")
        again = again.lower()
        if again == "yes" or again == "y":
            print()
            print("Ok! Restarting!")
            return True
        elif again == "no" or again == "n":
            return False
            print()
            print("GAME OVER!")
    
        print()
        print("I don't understand! Please type yes or no!")
        print()


def play():

    puzzle_dir = 'puzzles_evan'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)

    incorrect = ""
    correct = ""
    strikes = 0
    limit = 6

    solved = check(word, solved, correct)
    display_board(solved, incorrect, strikes, word)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            incorrect += letter

        else:
            correct +=letter
                
        solved = check(word, solved, correct)
        display_board(solved, incorrect, strikes, word)

    if word == solved:
        print("You win!")
    else:
        print("You lose!")

def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()
        
    show_credits()

# code execution begins here
if __name__ == "__main__":
    main()
