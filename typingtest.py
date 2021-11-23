"""
Program to test typing speed.
Uses "curses" module for styling.
Uses "random" for picking up random lines from
pre existing text.
"""
import curses
from curses import wrapper
import time
import random

#Function start_screen is called to show welcome screen

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test.")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()

#Function to overlay text and change color of character.

def display_text(stdscr, target, current, wpm = 0):

    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"Words per minute: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]

        if char != correct_char:
            color = curses.color_pair(2)
        else:
            color = curses.color_pair(1)

        stdscr.addstr(0, i, char, color)

#Function load_text generates random peices of text

def load_text():
    with open("romeo.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

#Function wpm_test gets the characters typed in by the user.

def wpm_test(stdscr):
    target_text = load_text()
    current_text =[]
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:

        time_elapsed = max(time.time() - start_time, 1)
        #Assuming that each word is 5 characters long:
        wpm = round((len(current_text)/(time_elapsed/60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        #
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

#The main function: Where the magic begins

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

#Gracefully ending the program:

    while True:

        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You have completed the test. Press any key to play again.")
        stdscr.addstr(3, 0, "Press Escape key to quit.")
        try:
            key = stdscr.getkey()
        except:
            break

        if ord(key) == 27:
            break

wrapper(main)
