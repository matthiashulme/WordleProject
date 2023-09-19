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
    
    def enter_action(GuessWord):
        
        row = gw.get_current_row()
        GuessWord = GuessWord.lower()
        if GuessWord not in FIVE_LETTER_WORDS:
            gw.show_message("This is not a word")
        else:
            # set colors

            for i in range(0,5):
                print(GuessWord[i])
                print(ActualWord[i])
                if (GuessWord[i] == ActualWord[i]):
                    gw.set_square_color(row, i, CORRECT_COLOR)
                elif (GuessWord[i] in ActualWord):
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)

                

    

            if GuessWord.lower() == ActualWord.lower():
                gw.show_message("Correct you win")

            elif row == 5:
                gw.show_message("You lose. Correct word was " + ActualWord)

            else:
                gw.set_current_row(row + 1)






    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
