# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, ROYAL_COLOR, NAVY_COLOR, N_COLS, N_ROWS




def wordle():
    ActualWord = ""
    ActualWord = random.choice(FIVE_LETTER_WORDS)
    print(ActualWord)

    PreviousHardMode = False
    PreviousByuMode = False
    GreenLetters = ['','','','','']
    YellowLetters = []


    def changeColor():
        for i in range(0,5):
            for x in range(0,5):
                color = gw.get_square_color(i,x)
                if color == CORRECT_COLOR:
                    gw.set_square_color(i,x, NAVY_COLOR)
                elif color == NAVY_COLOR:
                    gw.set_square_color(i,x, CORRECT_COLOR)
                elif color == PRESENT_COLOR:
                    gw.set_square_color(i,x, ROYAL_COLOR)
                elif color == ROYAL_COLOR:
                    gw.set_square_color(i,x, PRESENT_COLOR)
                elif color == MISSING_COLOR:
                    gw.set_square_color(i,x, MISSING_COLOR)
        # else:
        #     for i in range(0,5):
        #         for x in range(0,5):
        #             color = gw.get_square_color(i,x)
        #             if color == DARK_BLUE:
        #                 gw.set_square_color(i,x, CORRECT_COLOR)
        #             elif color == SKY_BLUE:
        #                 gw.set_square_color(i,x, PRESENT_COLOR)
        #             elif color == MISSING_COLOR:
        #                 gw.set_square_color(i,x, MISSING_COLOR)
        
                    
    def enter_action(GuessWord):

        nonlocal PreviousByuMode
        nonlocal PreviousHardMode
        HardMode = gw.get_hardmode()
        ByuMode = gw.get_byumode()
        if ByuMode != PreviousByuMode:
            changeColor()
            gw.show_message("Color has changed to Byu Mode")
        if HardMode != PreviousHardMode:
            gw.show_message("You are on hard mode")
        PreviousByuMode = ByuMode
        PreviousHardMode = HardMode



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
            # if byuColor:
            #     byuColor = False
            #     changeColor()
            # else:
            #     byuColor = True
            #     changeColor()
            for i in range(0,5):
                if (GuessWord[i] == ActualWord[i]):
                    if ByuMode:
                        gw.set_square_color(row, i, NAVY_COLOR)
                    else:
                         gw.set_square_color(row, i, CORRECT_COLOR)
                    GreenLetters[i] = GuessWord[i]
                    counterMap[GuessWord[i]] -= 1
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
            for i in range(0,5):
                if (GuessWord[i] in ActualWord and counterMap[GuessWord[i]] > 0):
                    if ByuMode:
                        gw.set_square_color(row, i, ROYAL_COLOR)
                    else:
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
