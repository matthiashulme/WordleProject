# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, N_COLS, N_ROWS


def wordle():
    ActualWord = ""
    ActualWord = random.choice(FIVE_LETTER_WORDS)
    print(ActualWord)

    HardMode = False
    GreenLetters = ['','','','','']
    YellowLetters = []
    
    def enter_action(GuessWord):
        
        HardMode = gw.get_hard_mode()
        ByuMode = gw.get_byumode()

        row = gw.get_current_row()
        GuessWord = GuessWord.lower()

        counterMap = {}
        for i in range(0,5):
            if (ActualWord[i] in counterMap):
                counterMap[ActualWord[i]] += 1
            else:
                counterMap[ActualWord[i]] = 1

        if GuessWord not in FIVE_LETTER_WORDS:
            gw.show_message("This is not a Word!")
        elif (HardModeCheck(GuessWord) == False and HardMode != False):
            gw.show_message("Must Include Previous Hints in Guess!")
        else:
            for i in range(0,5):
                if (GuessWord[i] == ActualWord[i]):
                    gw.set_square_color(row, i, CORRECT_COLOR)
                    GreenLetters[i] = GuessWord[i]
                    counterMap[GuessWord[i]] -= 1
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
            for i in range(0,5):
                if (GuessWord[i] in ActualWord and counterMap[GuessWord[i]] > 0):
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    YellowLetters.append(GuessWord[i])
                    counterMap[GuessWord[i]] -= 1
    
            if GuessWord.lower() == ActualWord.lower():
                gw.show_message("Correct you win!")

            elif row == 5:
                gw.show_message("You lose. Correct word was " + ActualWord)

            else:
                gw.set_current_row(row + 1)






    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)


    def HardModeCheck(guess):
        for letter in YellowLetters:
            if letter not in guess:
                return False
        for i in range(0,5):
            if GreenLetters[i] != guess[i] and GreenLetters[i] != '':
                return False

# Startup code

if __name__ == "__main__":
    wordle()
