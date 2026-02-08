# Is the main function for the program typetest engine

import curses
from .text import getWordsList
from .input import startTyping

def runner(wordsCount):
    wordsList = getWordsList(wordsCount)
    # print(wordsList)
    stats = curses.wrapper(startTyping, wordsList)

    print(f"wpm: {stats["wpm"]}")
    print(f"Raw wpm: {stats["raw wpm"]}")
    print(f"Accuracy: {stats["accuracy"]}")
    print(f"Time: {stats["time"]}")
    print(f"Key strokes: {stats["keystrokes"]}")


