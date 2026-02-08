# Grabs user key presses using the curses
import curses
from .timer import getTime, countDown
from ..stats.calculator import getStats

def startTyping(stdscr, targetWords):
    curses.noecho()
    stdscr.nodelay(False)

    text_buffer = []
    startTime = None
    keystrokes = 0
    
    stdscr.erase()
    stdscr.addstr(0, 0, "Start Test (ESC to exit): ")
    stdscr.addstr(1, 0, targetWords)
    stdscr.move(1, 0)

    while True:
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        for i, char in enumerate(targetWords):
            color = curses.color_pair(0)
            if i < len(text_buffer):
                if text_buffer[i] == char:
                    color = curses.color_pair(1)
                else:
                    color = curses.color_pair(2)

            stdscr.addch(1, i, char, color)

        stdscr.move(1, len(text_buffer))
        stdscr.refresh()

        current_input_str = "".join(text_buffer)
        if len(current_input_str) == len(targetWords):
            break
        
        try:
            key = stdscr.getch()
        except:
            continue

        if startTime is None and key != -1:
            startTime = getTime()

        if key in (curses.KEY_BACKSPACE, 127, 8):
            if len(text_buffer) > 0:
                text_buffer.pop()
                keystrokes += 1
        elif 32 <= key <= 126:
            if len(text_buffer) < len(targetWords):
                text_buffer.append(chr(key))
                keystrokes += 1
        elif key == 127:
            break

    stopTime = getTime()

    stats = getStats(current_input_str, targetWords, startTime, stopTime, keystrokes)
    return stats

    






