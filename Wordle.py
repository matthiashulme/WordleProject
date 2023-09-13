# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    ActualWord = ""
    ActualWord = random.choice(FIVE_LETTER_WORDS)
    print(ActualWord)
    def enter_action(GuessWord):
        if GuessWord.lower() == ActualWord.lower():
            gw.show_message("Correct you win")
        else:
            # remove before submit
            gw.show_message("no " + ActualWord.lower() + " " + GuessWord.lower())





    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
