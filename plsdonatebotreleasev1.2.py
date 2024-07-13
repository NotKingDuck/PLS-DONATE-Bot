import random
import time
import keyboard
from termcolor import colored

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #
# PROJECT MADE BY KINGDUCK, TO RUN THIS PROPERLY, YOU NEED TO INSTALL KEYBOARD AND TERMCOLOR WITH THIS COMMAND "pip install keyboard termcolor" IN THE CMD.   #
# I DON'T HAVE A APPLE COMPUTER SO I DON'T KNOW HOW TO MAKE IT WORK HERE.                                                                                     #
# IF YOU PUT "ROBUX" OR WORDS LIKE THIS YOU MIGHT GET BANNED!                                                                                                 #
# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #

# SETTINGS
MESSAGES = [
    "MESSAGE 1",
    "MESSAGE 2",
    "MESSAGE 3",
    "MESSAGE 4",
    "MESSAGE 5",
    "MESSAGE 6",
    "MESSAGE 7",
    "MESSAGE 8",
    "MESSAGE 9",
    "MESSAGE 10",
]
# YOU CAN PUT MORE MESSAGES IF YOU WISH
MINSLEEP = 10  # PUT IN THE MIN OF SECONDS BEFORE SENDING A MESSAGE
MAXSLEEP = 20  # PUT IN THE MAX OF SECONDS BEFORE SENDING A MESSAGE
MESSAGESTOSEND = 10  # SET TO 0 FOR INFINITE, NUMBER OF MESSAGES BEFORE QUITTING THE SCRIPT
DELAYPERCHAR = 0.05  # NOT RECOMMENDED TO CHANGE, TIME BEFORE TYPING THE CHARACTER
DELAYAFTEROPENINGCHAT = 0.5  # NOT RECOMMENDED TO CHANGE, TIME BEFORE TYPING THE MESSAGE
# END OF SETTINGS

print(colored('Made by KingDuck, NotKingDuck on GitHub', 'white', 'on_cyan', ['bold', 'underline']))
print(colored('Script will start in 15 seconds!', 'white', 'on_yellow', ['bold', 'underline']))
time.sleep(10)
print(colored('5...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('4...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('3...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('2...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('1...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('Quit this window to end the script!', 'white', 'on_blue', ['bold']))
print()
print(colored('Logs:', 'white', 'on_green', ['bold', 'underline']))

messages_sent = 0

while MESSAGESTOSEND == 0 or messages_sent < MESSAGESTOSEND:
    try:
        message = random.choice(MESSAGES)
        keyboard.press_and_release('/')
        time.sleep(DELAYAFTEROPENINGCHAT)

        for char in message:
            keyboard.write(char)
            time.sleep(DELAYPERCHAR)

        keyboard.press_and_release('enter')
        print(colored("Sent Message:", 'green'), colored(message, 'yellow'))
        print()

        messages_sent += 1

        sleep_time = random.randint(MINSLEEP, MAXSLEEP)
        print(colored(f"Sleeping for {sleep_time} seconds...", 'blue'))
        print(colored("--------------------", 'magenta'))

        time.sleep(sleep_time)
    except Exception as e:
        print(colored(f"An error occurred: {e}", 'red'))
        break

print(colored('Script ended!', 'white', 'on_green', ['bold', 'underline']))
time.sleep(10)

# PLS DONATE BOT BY NOTKINGDUCK
