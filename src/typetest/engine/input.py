# Grabs user key presses using the curses
import curses

def main(stdscr):
    curses.curs_set(1)
    stdscr.nodelay(False)

    text_buffer = []
    
    stdscr.addstr(0, 0, "Start Test (ESC to exit): ")
    stdscr.move(1, 0)

    while True:
        char = stdscr.getch()

        if char == 27:
            break

        elif char in (curses.KEY_BACKSPACE, 127, 8):
            if text_buffer:
                text_buffer.pop()

                y, x = stdscr.getyx()
                if x > 0:
                    stdscr.move(y, x-1)
                    stdscr.delch()

        # elif char in (curses.KEY_ENTER, 10, 13):
        #     text_buffer.append("\n")
        #     stdscr.addch("\n")

        elif 32 <= char <= 126:
            text_buffer.append(chr(char))
            stdscr.addch(char)

        stdscr.refresh()

curses.wrapper(main)
